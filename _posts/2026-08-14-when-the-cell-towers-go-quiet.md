---
layout: post
title: "When the Cell Towers Go Quiet"
description: "Cell service dies first in a real emergency. Here is how two off-grid radio networks, MeshCore and Meshtastic, fill the gap, and where each one fits a backup plan."
audio: /audio/posts/when-the-cell-towers-go-quiet.mp3
image: /images/mesh/three-network-shapes.png
---

![Two small LoRa mesh radio boards held up at a workbench, with the Meshtastic logo in a thought bubble overhead]({{ '/images/mesh/meshtastic-nodes-in-hand.png' | relative_url }})

Think about the last time your phone showed "No Service." Maybe a bad storm rolled through. Maybe the power went out for a whole neighborhood. For a few minutes you could not call, text, or look anything up. Now stretch that out. Picture it lasting three days, across your whole county.

That is the quiet part of most disasters that nobody plans for. The wind and the water get all the attention. But the thing that fails first, and hurts the most, is talking to each other.

Cell service goes down fast in a real emergency, and it stays down. So a backup plan needs a way to send messages that does not lean on the phone company at all. The good news is that cheap radios can do this now. The trick is understanding that these radios come in different shapes, and each shape is good at a different job.

## Three shapes of a network

Back in 1964, an engineer named Paul Baran drew a picture that still explains everything. He sketched three ways to connect a bunch of points together.

![Three ways to shape a network: centralized, decentralized, and distributed]({{ '/images/mesh/three-network-shapes.png' | relative_url }})

The first shape is **centralized**. One point sits in the middle, and everything else connects only to that middle point. This is your cell network. Your phone talks to a tower, and the tower talks to everything else.

> **Centralized:** one hub in the middle that everything depends on. Cut the hub and the whole network goes dark.

That middle point is the problem. When the tower loses power, or the lines behind it get cut, every phone that leaned on it goes silent at once. Centralized networks are fast and simple on a normal day. On a bad day they are a single thing that can break and take everyone down with it. That is all we need to say about cell towers. They are the shape to move away from when the lights go out.

The other two shapes are the interesting ones, and both of them are things you can build yourself.

## The building block: a mesh

Before we get to the other two shapes, one idea ties them together. Both are a kind of **mesh**.

> **Mesh network:** a group of radios that pass messages along for each other. Your message hops from radio to radio until it reaches the person you are trying to reach. No tower needed.

Each radio in the mesh is called a **node**. Every time your message jumps from one node to the next, that jump is called a **hop**. If one node goes offline, the message can often find another path around it. That is the whole point. There is no single tower to knock out.

These radios use a technology called LoRa, which is short for Long Range. LoRa sends tiny amounts of data, text and location, not video, but it sends them surprisingly far on very little power. A node can run for days on a small battery, or forever on a little solar panel. The gear is cheap. A basic node costs about the price of a couple of pizzas.

Two big open-source projects build these mesh networks. They both run on the same kind of radio. But they take almost opposite approaches, and that is exactly Baran's second and third shapes.

## MeshCore: the decentralized shape

The second shape Baran drew is **decentralized**. It is not one hub. It is a handful of hubs, spread out, each serving the nodes near it, with the hubs linked together into a backbone.

> **Decentralized:** several strong hubs spread across an area, tied together. No single one is the whole network, but the network is built on purpose around them.

This is how **MeshCore** works. In a MeshCore network, most radios are quiet. Your handheld does not shout your message to everyone in range. Instead, a few special nodes called **repeaters** do the heavy lifting. You put repeaters up high, on rooftops, grain elevators, water towers, and hills, and give them good power and solar. Your message goes to the nearest repeater, then travels repeater to repeater across the backbone until it drops down to the person you want.

Because only the repeaters relay traffic, the network stays calm and can grow huge. A message can make up to 64 hops across that backbone. That is enough to cross a whole region. MeshCore can even hold onto messages for you. A "room server" node keeps group messages so a friend who was offline can still read them when they turn their radio back on.

This is the shape you build when you have time to plan. And that is exactly what folks here in Nebraska are doing.

**[Nebraska Mesh](https://www.nebraskamesh.net/)** is a volunteer group building a statewide MeshCore network, one repeater at a time. They are the real-world version of Baran's decentralized drawing: strong nodes placed on purpose, on good high sites, tied into a backbone that covers the state. They have put together clear guides for the rest of us, including a one-pager for asking a property owner to host a repeater, a do's-and-don'ts sheet for placing one, and a flyer that walks a newcomer through the gear and the standard Nebraska radio settings. If you want to help build a backup that could serve a whole county, their [resources page](https://www.nebraskamesh.net/resources.html) is where to start. Credit to that crew. This is the patient, unglamorous work that pays off on the worst day.

## Meshtastic: the distributed shape

Baran's third shape is **distributed**. There are no special hubs at all. Every point is equal, and every point passes messages along for its neighbors.

> **Distributed:** every node is the same and every node relays. No backbone, no plan, no hierarchy. The web holds itself together.

This is **Meshtastic**. In a Meshtastic network, every single radio is a relay. You send a message, and every node that hears it repeats it to every node it can reach, and so on, until it arrives. There are no dedicated repeaters to set up. Nothing to plan. You hand a radio to five friends, turn them on, and you have a network.

That openness is the strength. If one radio dies, nobody cares, because the others are already echoing your message down other paths. The web heals itself as people move around. The trade-off is that all that echoing gets noisy, so Meshtastic keeps its reach short on purpose. Messages travel only about three hops by default, up to seven at most. It is built for a small group in the same general area, not a whole state.

Meshtastic is the grab-and-go shape. It shines when there is no backbone, no plan, and no time to make one. A search team spread across a few square miles. A family checking in across a flooded town. A neighborhood that decides on Tuesday it wants a way to talk by Friday.

## Where each one fits

Here is the part that matters. These two are not rivals fighting over the same job. They are different layers of the same backup plan.

![The backup continuum: cell for daily use, MeshCore for a planned regional layer, Meshtastic for grab-and-go]({{ '/images/mesh/emergency-continuum.png' | relative_url }})

On a normal day, you use the centralized network. Cell service is fast and easy, right up until it is gone.

For the layer under that, the county or regional layer, you want MeshCore. It takes planning and volunteers and good high sites. But once it is up, it is a real backbone that can carry messages across a whole area, hold them for people who are offline, and keep running on solar long after the grid quits. That is the layer Nebraska Mesh is building right now.

For the layer under *that*, the layer you can throw together with your own hands and no infrastructure at all, you want Meshtastic. Keep a few radios charged in a drawer. When everything else is down and you just need to reach the people right around you, you turn them on and you have a net in minutes.

A good backup is not one radio. It is a stack. The planned backbone catches the whole region. The grab-and-go mesh catches the block you are standing on. Together they cover the gap that opens the moment the towers go quiet.

You do not have to build the whole thing this weekend. Pick one radio. Turn it on. Send a message to a friend across town with no cell signal in the loop at all. Once you have felt that work, the rest of the plan makes sense on its own.
