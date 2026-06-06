---
layout: post
title: "Reach Your Whole Home Lab From Anywhere: Tailscale on a UniFi Dream Machine Pro"
---

*Turn your UDM Pro into a Tailscale subnet router so every device on your LAN is reachable from anywhere — no port forwarding, no public exposure.*

## Why do this on the router instead of each device?

You *could* install Tailscale on every machine you want to reach. But installing it **on the UDM Pro as a subnet router** is the power move: one install advertises your entire LAN onto your private Tailscale network. After that, any of your Tailscale devices (laptop, phone) can talk to *anything* on your home network — a NAS, a local LLM server, a Pi, a printer — using its normal LAN IP, from anywhere in the world.

Crucially, **nothing is exposed to the public internet.** No ports are forwarded. Tailscale builds an encrypted WireGuard tunnel that only your own devices can join, and it punches through NAT automatically — so this works even if your ISP has you behind carrier-grade NAT where port forwarding is impossible.

**The catch:** Tailscale isn't official Ubiquiti software. We use the excellent community installer [`SierraSoftworks/tailscale-unifi`](https://github.com/SierraSoftworks/tailscale-unifi), which is widely used and handles the tricky part — surviving reboots and firmware updates. You're modifying your edge router, so go slow and read each step.

## Prerequisites

- A UniFi gateway running **UniFi OS 2.x or later** (UDM Pro, UDM SE, UDR, Cloud Gateway, etc.). *Not* supported: UniFi OS 1.x, Cloud Key Gen 1, the old USG, or BusyBox-based devices.
- A free [Tailscale account](https://tailscale.com) (personal use is free for up to 100 devices).
- Admin access to your UniFi console and a few minutes of SSH time.

> **Worked example used throughout:** my LAN is `192.168.1.0/24` and my gateway (the UDM Pro) is `192.168.1.1`. **Substitute your own values** — find yours under *UniFi Network → Settings → Networks*, or on a Mac with `route -n get default | grep gateway`.

## Step 1 — Enable SSH on the UDM Pro

1. Open your UniFi console (e.g. `https://192.168.1.1` or `unifi.ui.com`).
2. Go to **UniFi OS → Settings → System → Advanced**.
3. Toggle **SSH** on, and **set a strong root password** (this is the password you'll use to log in as `root`).

## Step 2 — SSH into the gateway

From your computer:

```bash
ssh root@192.168.1.1
```

Enter the SSH password you just set. You're now on the gateway.

## Step 3 — Install Tailscale

Run the community installer:

```bash
curl -sSLq https://raw.githubusercontent.com/SierraSoftworks/tailscale-unifi/main/install.sh | sh
```

This installs `tailscaled` as a systemd service under `/data/tailscale/`, and adds a boot hook in `/data/on_boot.d/` so it **persists across reboots and firmware upgrades** (UniFi OS otherwise wipes non-persistent storage on update).

Verify the install:

```bash
tailscale status
```

## Step 4 — Bring it up as a subnet router

This is the line that advertises your LAN. **Replace the CIDR with your own subnet.**

```bash
tailscale up \
  --advertise-routes="192.168.1.0/24" \
  --snat-subnet-routes=false \
  --accept-routes
```

What the flags do:

| Flag | Purpose |
|------|---------|
| `--advertise-routes=...` | Offers your LAN subnet to your tailnet so remote devices can reach it. |
| `--snat-subnet-routes=false` | Preserves the *original* client IP for traffic crossing the tunnel (nicer for logging/ACLs). |
| `--accept-routes` | Lets the UDM also use routes other subnet routers advertise. Optional. |

Want the UDM to double as an **exit node** (route *all* your internet traffic through home when you're traveling)? Add `--advertise-exit-node`.

When you run this, Tailscale prints a login URL. Open it in a browser and authenticate to attach the UDM to your tailnet.

> Subnet routing needs IP forwarding, which is **already enabled by default** on UniFi OS gateways — no extra sysctl tweaks required.

## Step 5 — Approve the device and routes in the admin console

The advertised routes don't go live until you approve them:

1. Open the [Tailscale admin console → **Machines**](https://login.tailscale.com/admin/machines).
2. Find your UDM Pro in the list.
3. Click it → **Edit route settings** → **enable** the subnet route(s) you advertised (and the exit node, if you added it).
4. **Strongly recommended:** also **disable key expiry** for the UDM. Otherwise the node's auth key expires (default ~180 days) and your remote access silently dies until you re-authenticate on the router.

## Step 6 — Test it

Install Tailscale on a phone or laptop, sign in with the **same account**, then — from a coffee shop, on cellular, anywhere — hit a device on your home LAN by its normal IP. For example, a local web service on your LAN:

```bash
curl http://192.168.1.50:8080/
```

If that responds from off-network, you're done. 🎉

## Day-2 operations

**Update Tailscale:**

```bash
/data/tailscale/manage.sh update
```

**Restart the service:**

```bash
systemctl restart tailscaled
```

**Check status / your tailnet IP:**

```bash
tailscale status
tailscale ip -4
```

**Uninstall cleanly:**

```bash
/data/tailscale/manage.sh uninstall
```

## Troubleshooting

- **Routes not working from remote devices?** Re-check Step 5 — unapproved subnet routes are the #1 cause. The route must show as enabled in the admin console.
- **Access died after a few months?** Key expiry. Disable it on the UDM node (Step 5) and run `tailscale up ...` again to re-auth.
- **Gone after a firmware update?** The installer's boot hook normally handles this; if not, re-run the Step 3 install command — it's idempotent.
- **`tailscale: command not found` after SSH?** Use the full path `/data/tailscale/tailscale`, or log out and back in to pick up the PATH.

## Security notes

- Tailscale exposes your LAN **only to devices in your own tailnet** — it is not a public hole in your firewall. But that also means *every* device you connect from must run Tailscale and be signed into your account.
- For finer control (e.g. "my laptop can reach the LLM server but not the whole LAN"), use [Tailscale ACLs](https://tailscale.com/kb/1018/acls) to scope what each device may reach.
- This is third-party software on your edge router. It's well-maintained and popular, but it's not Ubiquiti-supported — keep that in mind for a device your whole network depends on.

---

*Installer credit: [SierraSoftworks/tailscale-unifi](https://github.com/SierraSoftworks/tailscale-unifi).*
