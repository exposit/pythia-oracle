### Pythia only runs under Python 2.7 with Kivy2.

**If you are installing on Windows, be sure to select the "set environment paths automatically" option in the Python installer (more [here](#how-do-i-install-this)). You will need to scroll down to see it!**

### Pythia-Oracle 1.5.0

Project page is [here](https://exposit.github.io/pythia-oracle/). My blog is [here](https://exposit.github.io/katamoiran/). A guide is in this repository, in [help.md](https://github.com/exposit/pythia-oracle/blob/master/HELP.md).

Table of Contents
=================

* [What is it?](#what-is-it)
* [Solo Roleplaying\! How does that even work?](#solo-roleplaying-how-does-that-even-work)
* [How do I install this?](#how-do-i-install-this)
* [Upgrading from 1\.2\.0 &amp; earlier](#upgrading-from-120--earlier)
* [Upgrading from an older version](#upgrading-from-an-older-version)
* [Customization/Setup](#customizationsetup)
* [Wait, I want more tables\!](#wait-i-want-more-tables)

###### Created with [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

#### What is it?

Pythia is a tool to run solo adventures and to generate content for sandbox campaigns. It uses Python 2.7 and Kivy and will probably run on any platform they will. I wrote it with two goals in mind; first, I wanted to be able to generate content on the fly for my group sandbox campaign while keeping track of that content and second, I wanted to be able to run solo characters through adventures that would surprise me.

Pythia doesn't replace systems like Mythic GM Emulator or Scarlet Heroes or your favorite random chart -- it just makes it easier to use them.

#### Solo Roleplaying! How does that even work?

The easiest way to get a handle on it is to read actual plays; there are a whole bunch using lots of different systems and formats on the [Lone Wolf Roleplaying](https://plus.google.com/communities/116965157741523529510) g+ group. And you can see APs using Pythia on my blog.

The basic procedure I use is pick an RPG system (usually Scarlet Heroes), make a character, fire this program up, and start asking questions. Type in a question like "Am I in a cave?" and hit the "???" button. If the answer is yes, hit the "what do I see" button and interpret. If no, maybe the hero is in a castle. Or a spaceship. Or in a forest. Ask again to find out!

... or don't. You can play however you want to! Pythia just seeks to facilitate that play.

#### How do I install this?

**Basically:**

Install Kivy, following the [installation instructions](https://kivy.org/doc/stable/installation/installation-windows.html) for your OS and Python 2.7. The instructions are very comprehensive and cover pretty much everything you'll need, step by step. They will get you through installing Python 2.7 (or identifying if it's already installed) and through installing Kivy.

If you want to use the Pythy panel (which is very rudimentary) you will also need [markovify](https://github.com/jsvine/markovify) and [TextBlob](https://textblob.readthedocs.io/en/dev/install.html).

**More Detailed:**

I strongly suggest you use the method listed above under "Basically" -- the Kivy people know what they're talking about. But here's what I'd tell you to try first off if you ran into trouble.

Open up a terminal (command prompt) and type "python --version". If you get a "not found" response, go to [python.org](https://www.python.org/downloads/) and install the latest 2.7 version (**not 3**) for your operating system. While installing, use the default settings if you can; HOWEVER, if it asks what components you want, be sure to make sure the "set environment paths" option is enabled (you may need to scroll down to see it in the install window). Otherwise you'll need to set the paths manually and that's, while easy, annoying.

Open up a terminal (command prompt) and type "python --version". If you get a "not found" response, try rebooting and check the version again. If necessary, set the environment path and reboot again.

Now go to the [kivy installation page](https://kivy.org/docs/installation/installation.html) for your OS (stable version) and either install the application from a release (download the file, double click on it, etc.) or copy-paste the given lines as directed, waiting in between each as necessary. Read any errors carefully and address them.

If you want to use the Pythy panel, you'll also need to install markovify and TextBlob.

`pip install markovify`

`pip install -U textblob`

`python -m textblob.download_corpora lite`

**Running Pythia**

Once that's all done, you'll need to clone or download this repository. If you know how to use git, you're good to go, clone away. Otherwise, click the green 'clone or download' button on the main pythia-oracle github page, and select 'download zip'. Unzip this archive somewhere easy to find (desktop, Documents folder).

You have two options now. Easiest (in Windows) is to double-click on the 'pythia.py' file to launch the program or (on Mac) right click 'pythia.py' and select 'open with' and 'Python Launcher 2.7.X'. You can also run from the command line.

Run pythia with:

`python pythia.py`

unless you installed the kivy app in your application folder, in which case it's:

`kivy pythia.py`

You might see (if debug is on) a bunch of messages scroll by, largely complaining that the layout is too small, and then the program will appear. Note that unless the game actually crashes, you can ignore all error messages.

You should be good to go! Be sure to play around in the quicksave before you start a 'real' game, and save (and back up your save folder) frequently. Also read over the customization section in this file.

### Upgrading from 1.2.0 & earlier

From now on Pythia should handled changes to the base config file more gracefully; you shouldn't need to do anything special to upgrade, except back up your save and backup folders as usual.

If you experience formatting issues, you will need to either retag each block in Pythia or do so in the main.txt file.

__I strongly suggest that you use a [json editor](https://github.com/josdejong/jsoneditor) when editing save game files. Just unzip the release, then open the "04_load_and_save" file in the examples directory in a modern browser.__

If you decide to edit main.txt directly, be sure to set the "manual_edit_mode" flag in config.py to True first.

After saving, load it up in Pythia. If everything loads correctly, close Pythia down, change the "manual_edit_mode" flag back to "False", and you're ready to start playing again.

Read the other sections on upgrading as well!

#### Upgrading from an older version

Move your saves folder and your backups folder to another directory completely outside the pythia directory structure. I would also zip up a copy and put it in a third location just in case at this point.

Double check that you have a saved copy of your saves folder and backups folder somewhere else, then delete your existing pythia-oracle folder.

Grab a fresh download, unzip, then copy (don't move) your save folder in. Things should just work from here.

#### Customization/Setup

Read the HELP.MD file! Also read the config.py file; it is pretty well documented.

You'll find your save games in the pythia folder under 'saves'. Backup zips are saved in the backups folder. The config.py file contains all the important variables and parts of it are saved on a "per game" basis.

I recommend playing around in the quicksave a bit until you figure out what kind of output the various buttons generate and what kind of input they expect. To reset the quicksave, just delete the entire quicksave folder in the saves folder, then remake it at the title screen.

MAKE BACKUPS BEFORE EDITING FILES MANUALLY. It takes two seconds to right click on your save folder and 'compress' or 'save as zip' then drag and drop the zip somewhere else. Pythia makes backups automatically but common sense can save you a lot of stress.

#### Wait, I want more tables!

Please let me know if you have any suggestions!

If you need more tables *right now*, you can use the "pick one" buttons to get weighted answers from a copy-pasted, comma separated list on the fly, or you can add in whatever tables you like in the code in your own user panels. Pythia is designed to be modular and extensible. I've included a sample panel in panels/oracles as a guide, and you can look at the included core panels to see how they work.

If you have created content you'd like included (or you have permission from the original author), drop me a line and I'll add them as panels as I can. Or I'd be happy to link to/add any panels you make, as long as I can follow the code. I've made a separate repository for non-core panels here:

[panel repo](https://github.com/exposit/pythia-oracle-panels)

Any questions please let me know as an issue here or on my blog.

Happy Solo Gaming!
