---
layout: default
---

[Pythia Oracle](https://github.com/exposit/pythia-oracle) is a tool to make solo RPG gaming easier. It's written in Python and Kivy, cross-platform, extensible, and freely available on github.

If you're new to solo gaming, Pythia Oracle is likely all you need to get started -- it has a built-in oracle for yes and no questions, a number of how much/how many/how's it going random generators, plenty of space to track any information you want to track, and a nice, clean, readable output if you want to show off your adventures on your blog.

## Features

* main text is saved to multiple output formats (markdown, html, simplejson)
* generates blog-ready play logs
* user-extensible oracle and generator panels
* existing oracle panel is based on FU's core dice mechanic (and/but/- structure)
* a ton of random generators
* built-in trackers for threads and actors, a key/value tracker & an active/inactive tracker
* 'pick one' quick buttons that let you weight options on the fly
* dice roller using standard notation & dice presets
* five different view/edit/play modes
* supports user-created CYOA/Gamebook-style scenarios (very beta)
* tutorial/sample dungeon included (very basic)
* built-in diagram mapping (very beta)

### Screenshots

<a href="{{site.baseurl}}img/screenshot1.png"><img src="{{site.baseurl}}img/screenshot1.png" alt="title screen" height="100" width="200"></a>
<a href="{{site.baseurl}}img/screenshot2.png"><img src="{{site.baseurl}}img/screenshot2.png" alt="main screen" height="100" width="200"></a>

### Things to watch out for

Pythia Oracle is a one-person project and designed for my own use and playstyle. It's a little quirky. Adding in panels isn't trivial. I'll likely be updating and tweaking and changing stuff frequently. I'm a total neophyte at [Kivy](https://kivy.org/#home) and the aesthetics could be more pleasing.

Please back up any text you enter into it frequently. It would be a huge bummer if you put a whole campaign in and the lone save file ended up corrupted or somehow deleted! The save directory (./saves) is located in the root directory alongside the main scripts. (Now backed up as a zip every time you run the program.)

Not much else to say right now. Go check it out! If you want to contribute, let me know at github.
