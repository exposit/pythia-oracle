---
layout: default
---

[Pythia Oracle](https://github.com/exposit/pythia-oracle) is a tool to make solo RPG gaming easier and to generate content for sandbox RPGs. It's written in Python and Kivy, cross-platform, extensible, and freely available on github.

If you're new to solo gaming (or just want to generate some random content), Pythia Oracle is likely all you need to get started -- it has a built-in oracle for yes and no questions, a number of how much, how many, why, and how's it going random generators, plenty of space to track any information you want to track, and a nice, clean, readable output if you want to show off your adventures on your blog.

It also plays well with just about any oracle or random content table; you can extend your own panels (if you know a little Python or can copy existing files) or just use the dice roller with your own pdfs.

## Features

* core oracle panel is based on FU's core dice mechanic (and/but/- structure)
* dice roller using (basically) standard notation & lots of common dice preset buttons
* a ton of one click random generators for actors and world content
* 'pick one' quick buttons that let you weight options on the fly
* generates markdown, html, json and javascript/html play logs
* user-extensible oracle, generator, and map panels
* trackers for [Mythic-style](http://www.drivethrurpg.com/product/16173/Mythic-Role-Playing?it=1) threads and actors, a general key/value tracker & an active/inactive tracker
* five different view/edit/play modes
* map panel inspired by [Scarlet Heroes'](http://www.drivethrurpg.com/product/127180/Scarlet-Heroes) diagram dungeon method (very beta)
* supports user-created Pythia-style CYOA/Gamebook scenarios (very beta)
* tutorial dungeon that demonstrates features (very basic) based on part of [Oracle's Decree](http://blog.trilemma.com/2015/10/the-oracles-decree.html) (which is a much better dungeon than I've implemented, ha)

### Screenshots

<a href="{{site.baseurl}}img/screenshot1.png"><img src="{{site.baseurl}}img/screenshot1.png" alt="title screen" height="100" width="200"></a>
<a href="{{site.baseurl}}img/screenshot2.png"><img src="{{site.baseurl}}img/screenshot2.png" alt="main screen" height="100" width="200"></a>

### Things to watch out for

Pythia Oracle is a one-person project and designed for my own use and playstyle. It's a little quirky. Adding in panels isn't trivial. I'll likely be updating and tweaking and changing stuff frequently. I'm a total neophyte at [Kivy](https://kivy.org/#home) and the aesthetics could be more pleasing.

Please back up any text you enter into it frequently. It would be a huge bummer if you put a whole campaign in and the lone save file ended up corrupted or somehow deleted! The save directory (./saves) is located in the root directory alongside the main scripts. (Now backed up as a zip every time you run the program.)

Not much else to say right now. Go check it out! If you want to contribute, let me know at github.
