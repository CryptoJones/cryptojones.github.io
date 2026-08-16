---
layout: post
title: "The Army Built a Phone Company in a War Zone"
description: "A 1966 Army film shows the gear that wired a country with no front line: scatter radio bounced off the sky, microwave hops, teletype, punch cards, and an early satellite link."
audio: /audio/posts/The-Army-Built-a-Phone-Company-in-a-War-Zone.mp3
---

A film from 1966 does not sound like a technology briefing. This one is. Staff Film Report 66-43B was made by the Department of Defense to show how the Army wired South Vietnam. Watch it as a network engineer instead of a history buff and it turns into something else. It is a record of the moment the Army stopped building radio links and started building a network.

<div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; margin-bottom:1rem;">
  <iframe src="https://www.youtube.com/embed/zreruf3s8R0" title="Staff Film Report 66-43B U.S. Army Communications Vietnam" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute; top:0; left:0; width:100%; height:100%;"></iframe>
</div>

<div style="margin-bottom:1.5rem;"><strong><a href="https://www.youtube.com/watch?v=zreruf3s8R0">Watch Staff Film Report 66-43B on YouTube</a></strong></div>

## The problem was the map, not the radio

In a conventional war, an army moves from point A to point B and holds the ground behind it. Signal troops can then place a radio on each hilltop along the way and hand the message down the line. That is line of sight radio.

> **Line of sight radio:** a link that works only when the two antennas can "see" each other, with no hill or curve of the earth in the way.

Vietnam broke that assumption, and the film says so directly. The Army might hold point A and point B and hold none of the land in between. Every hilltop relay would need troops to guard it. There were never going to be enough troops for that.

So the Army stopped trying to go around the terrain and went over it instead.

## Bouncing signals off the sky

The workaround was tropospheric scatter.

> **Tropospheric scatter:** aiming a very strong radio beam at the lower atmosphere so that a small part of it scatters back down to a receiver far past the horizon.

Most of that beam is wasted. That is the point. You throw an enormous amount of power at the sky and collect the crumbs that fall back down, which is why these stations ran transmitters rated in the thousands of watts and used antennas the size of billboards.

The payoff was not only distance. It was capacity. The film puts the numbers side by side. The high frequency radios at the big Saigon complex each carried four voice channels, and they reached other countries on transmitters rated at 8,000 watts toward the Philippines, 10,000 watts toward Bangkok, and 30,000 watts toward Okinawa. A single scatter system carried as many as 72 channels. That gap is the whole story of the buildup. Channel count was the currency, and scatter radio bought a lot of it.

## A backbone, then layers under it

The long haul network in the film is the Integrated Wideband Communications System. Its terminals were mobile scatter sets that lived in air conditioned vans, each one self contained with its own receivers, transmitters, multiplexers, and generators. One set shown in the film was originally installed by the Air Force, ran 10,000 watts, and fed its dish antennas through waveguide.

> **Waveguide:** a metal pipe that carries very high frequency radio energy to the antenna with much less loss than an ordinary cable.

In mid 1966 those Air Force sites came under Army control. That is why the 1st Signal Brigade shows up in the film. It was formed in April 1966 because somebody had to own the whole thing centrally.

Under the backbone sat shorter links. A mountain station near Da Lat ran medium range scatter sets holding 48 channels to Pleiku and another 48 to Saigon. The film notes those circuits held frequency to within one cycle in ten million and could lift a signal of 50 millionths of a watt up to a full 1,000 watts. Closer in, short microwave hops carried 45 channels on 10 watt line of sight beams across about 30 kilometers. Below that came tactical sets on 45 foot masts good for roughly 40 miles, and below those the small FM radios riding in trailers and in the back of jeeps.

Core, distribution, access. The names are new. The shape is not.

## The half that was not radio at all

The film spends its second half on the parts people forget. Saigon's long distance switchboards handled somewhere between 15,000 and 17,000 calls a day, and direct dialing was on the way. A tape relay station cut duplicate message tapes at 1,200 words per minute, which is store and forward messaging built out of paper and machinery. Punch card readers pushed logistics data at up to 200 cards per minute so that replacements, pay, and supplies landed in the right place at the right time.

Then a satellite terminal went live in mid 1966. It added circuits to Hawaii and Thailand, plus a hop by way of an early Syncom satellite to a station in Asmara, Ethiopia. A country with no reliable front line had a satellite link before most of the world had color television.

## Read it with the volume down

This is a service film, so it shows a system that works. There are no outage numbers, no costs, and no failures. One honest detail does survive the polish. The narrator says the network ran with the help of contractor technicians, and the closing lines thank the American electronics industry. The Army did not build this alone, and that dependence never went away.

The lesson holds up anyway. The problem was a place where you could not count on holding the ground between two points. The answer was layers of radio with different ranges and different capacities, plus people watching a board for failed circuits. That same problem shows up in a much smaller way whenever [the cell towers go quiet]({{ site.baseurl }}/when-the-cell-towers-go-quiet/), and the answer still rhymes.
