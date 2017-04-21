---
layout: default
---

[Pythia Oracle](https://github.com/exposit/pythia-oracle) is a desktop-based tool to facilitate solo roleplaying and to generate random content for sandbox RPGs. It's written in Python and Kivy, cross-platform, extensible, and freely available on github.

If you're new to solo gaming, Pythia Oracle is all you need to get started -- it has a text logging area, oracles, random generators, plenty of space to track information, and automatic markdown and html logs if you want to show off your adventures on your blog.

## Features

* robust text logging area with separate, tagged mechanic and narrative blocks
* multiple oracles, including [FU-based](http://perilplanet.com/fu-rpg/) and [Mythic](http://www.drivethrurpg.com/product/16173/Mythic-Role-Playing?it=1)
* flexible dice roller using standard notation, with presets & list-pickers
* 50-ish random generators for creating instant dungeon, npc, plot, and world content
* separate trackers for threads, actors, general information, and character sheets
* markdown and html play logs are generated automatically; customize output templates supported
* diagram and grid-based dungeon map support
* automatic backups and everything stored in json text files

Take a look at the [help](https://github.com/exposit/pythia-oracle/blob/master/HELP.md) for a comprehensive overview of everything Pythia can do. My [blog](https://exposit.github.io/katamoiran/) has some actual play logs, all generated with Pythia. And the [readme](https://github.com/exposit/pythia-oracle/blob/master/README.md) will walk you through the installation process.

### Screenshots

<a href="{{site.baseurl}}img/screenshot1.png"><img src="{{site.baseurl}}img/screenshot1.png" alt="title screen" height="100" width="200"></a>
<a href="{{site.baseurl}}img/screenshot2.png"><img src="{{site.baseurl}}img/screenshot2.png" alt="oracle screen" height="100" width="200"></a>
<a href="{{site.baseurl}}img/screenshot3.png"><img src="{{site.baseurl}}img/screenshot3.png" alt="generator screen" height="100" width="200"></a>
<a href="{{site.baseurl}}img/screenshot4.png"><img src="{{site.baseurl}}img/screenshot4.png" alt="map screen" height="100" width="200"></a>

### Things to watch out for

Pythia Oracle is a one-person project and designed for my own use and play style. It's a little quirky. Scenario support is still in there but virtually unsupported at this point. Little tiny annoying bugs are probably lurking. I have crammed in way more buttons and text than is sensible or user-friendly.

It's probably more than a little overwhelming at first glance.

Please keep an eye on your saves and verify that your logs look the way you expect them to, frequently. The saves and backup directories are located in the root directory alongside the main scripts. Automatic backups are made unless you explicitly disable them; check the config.py file for details.

Not much else to say right now. If you need me, let me know at github (for a somewhat speedy response) or on my extremely quiet [blog](https://exposit.github.io/katamoiran/) (for an eventual one).
