---
layout: default
---

[Pythia Oracle](https://github.com/exposit/pythia-oracle) is a tool to make solo RPG gaming easier. It's written in Python and Kivy, cross-platform, extensible, and freely available on github.

If you're new to solo gaming, Pythia Oracle is likely all you need to get started -- it has a built-in oracle for yes and no questions, a number of how much/how many/how's it going random generators, plenty of space to track any information you want to track, and a nice, clean, readable output if you want to show off your adventures on your blog.

## Features

* main text is saved to multiple output formats (markdown, html, simplejson)
* user-extensible oracle and generator panels
* existing oracle panel is based on FU's core dice mechanic (and/but/- structure)
* built-in trackers for threads and actors
* two key/value trackers
* 'pick one' quick buttons that let you weight options
* dice roller using standard notation
* four different view/play modes
* did I mention it's extensible?

### Screenshot

<a href="{{site.baseurl}}img/screenshot1.png"><img src="{{site.baseurl}}img/screenshot1.png" alt="title screen" height="100" width="200"></a>
<a href="{{site.baseurl}}img/screenshot2.png"><img src="{{site.baseurl}}img/screenshot2.png" alt="main screen" height="100" width="200"></a>

### Things to watch out for

Pythia Oracle is a one-person project and designed for my own use and playstyle. It's a little quirky. Adding in panels isn't trivial. I'll likely be updating and tweaking and changing stuff frequently. I'm a total neophyte at [Kivy](https://kivy.org/#home) and the aesthetics could be more pleasing.

Please back up any text you enter into it frequently. It would be a huge bummer if you put a whole campaign in and the save file ended up corrupted or somehow deleted! The save directory (./saves) is located in the root directory alongside the main scripts.

Not much else to say right now. Go check it out! If you want to contribute, let me know at github.
