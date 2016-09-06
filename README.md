### Be sure to make a separate back up of your saves folder before upgrading to a new version!!!

### Pythia-Oracle 0.2.0
Project page is [here](https://exposit.github.io/pythia-oracle/). My blog is [here](https://exposit.github.io/katamoiran/). Eventually I'll make a more detailed project page. Likely, anyway.

#### What is it?

Pythia is a framework to run solo adventures. It uses Python 2.7 and Kivy and will probably run on any platform they will. I wrote it with two goals in mind; first, I wanted to be able to generate content on the fly for my multi-player sandbox campaign while keeping track of that content and second, I wanted to be able to run solo characters through adventures that would surprise me. There are many great GM emulating tools out there, software and print. This is what works for me.

#### Solo RPG Gaming! How does that even work?

The basic procedure I use is pick a system, make a character, fire this program up, and start asking questions. Type in a question like "Am I in a room?" and hit the "???" button. If the answer is yes, type in a room description. If no, maybe the hero is in a cave. Or a spaceship. Or in a forest. Ask again to find out!

... or don't. You can play however you want to! Pythia just seeks to facilitate that play. You can also use it to generate random content for a multi-player campaign.

#### How do I install this?

**Basically:**

Install Kivy, following the [installation instructions](https://kivy.org/docs/installation/installation.html) for your OS and Python 2.7. The instructions are very comprehensive and cover pretty much everything you'll need, step by step. They will get you through installing Python (or identifying if it's already installed) and through installing Kivy.

Pip install simplejson, then run pythia with

`python pythia.py --size 1280x725`

You should see a bunch of messages scroll by, largely complaining that the layout is too small, and then the program will appear.

**Windows/more detailed:**

Go to [python.org](https://www.python.org/downloads/) and install the latest 2.7 version. I've got 32 bit installed on my Windows machine. While installing, use the default settings if you can; HOWEVER, when it asks what components you want, be sure to make sure the "set environment paths" option is enabled (you may need to scroll down to see it in the install window). Otherwise you'll need to set the paths manually and that's, while easy, annoying.

Open up a terminal (command prompt) and type "python --version". If you get a "not found" response, try rebooting and check the version again.

Now go to the [kivy installation page](https://kivy.org/docs/installation/installation.html) for your OS (stable version) and copy-paste the given lines as directed, waiting in between each as necessary.

Once that's all done, you'll need to clone or download this repository. If you know how to use git, you're good to go, clone away. Otherwise, click the green 'clone or download' button on the main pythia-oracle github page, and select 'download zip'. Unzip this archive somewhere easy to find (desktop, Documents folder, etc).

You have two options now. Easiest is to double-click on the 'pythia.py' file to launch the program. However, it is really best viewed in widescreen; to get this, navigate to the folder containing "pythia.py" and type

`python pythia.py --size 1280x725`

You should be good to go! Be sure to play around in the quicksave before you start a 'real' game, and save (and back up your save folder) frequently.

#### Upgrading from an older version

Move your saves folder to another directory. I zip up a copy and put it in a separate archive folder just in case at this point.

Double check you have a saved copy of your saves folder. Delete your existing pythia-oracle folder.

Grab a fresh download, unzip, then copy (don't move) your save folder in. Run the program; if you get any errors, read them. Some file names may have changed. New variables might have been added to the config file. You can compare your game's config.txt against the default quicksave to see.

If all else fails, delete the contents of the save folder and make a new game. Then copy your save game files into the new game directory, overwriting as prompted. You can also skip overwriting the config.txt file, leaving it in the new game generated state, and just set your variable manually by opening the file up in a text editor or setting them as you play.

#### Customization/Setup

If the app window is too big or two small, you can adjust it by setting the size, either in the pythia.py file or at the command line.

`python pythia.py --size 1280x725`

You can also open up the 'pythia.py' file in your favorite text editor, then uncomment these lines:

`kivy.config.Config.set ( 'graphics', 'width', 1280 )`<br>
`kivy.config.Config.set ( 'graphics', 'height', 725 )`

Change the numbers (1280, 725) as you'd prefer.

If it is just the font that is too small, open up config.py and change the number after 'basefontsize' to the size you'd prefer; this may make some of your buttons or labels crowded if you go too big but you can always change it back! Note, this changes it for every new game; if you already have a game created you'll need to change the basefontsize in saves/\<game name\>/variables.txt as well.

To shut down, click the x in the upper left of the main window or just close the terminal. You'll find your save games in the same folder under 'saves'. Content is saved pretty frequently but be sure to hit the 'save' button before closing down to be sure.

I recommend playing around in the quicksave a bit until you figure out what kind of output (and input) the various buttons expect! To reset the quicksave, just delete the entire quicksave folder in the saves folder, then remake it at the title screen.

Note: the system expects a quicksave folder to be present and weird things might happen if you decide not to keep one.

Quite a lot of the program's data is saved in plain text format (in json); make a backup and then open up some save game files and see what's in there. You can edit past entries, change configuration values, even set a custom pre and post title for your game (look for those entries and the '---').

#### Wait, I want more tables!

I don't blame you. I use a ton more myself but I don't think it'd be cool to use other authors' content without asking. So I've started asking. Feel free to ask your favorite authors about their licensing/permission as well!

Until then, you have a couple of options; you can use the "pick one" buttons to get weighted answers from a copy-pasted table on the fly, or you can add in whatever tables you like in the code. I've included a sample panel in userdata/oracles as a guide.

If you have created content you'd like included (or you have permission from the original author), drop me a line and I'll add them as panels as I can. Or I'd be happy to link to/add any panels you make, as long as I can follow the code. I've made a separate repository for non-core panels here:

[panel repo](https://github.com/exposit/pythia-oracle-panels)

Any questions please let me know as an issue on the panels repo or here.

Happy Solo Gaming!
