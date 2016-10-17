####Changelog

Please note that this is very rough and just to give you an idea of what's been changed or improved. API breaking and save game breaking stuff may happen!

MAKE BACKUPS BEFORE EDITING FILES MANUALLY.

Version 1.1.0 (WIP)

* added a new user variable, 'trigger_tests', so you can set your own trigger checks
* added more backup options, including cap on total saves and more options for when to save
* added a new status ("BigQ") to the threads panel for Perilous Intersections compatibility
* added some error catching to the top/bottom jump button
* tweaked a few other generators to give more sensible and usable results
* added a couple of new generators, one for clarifying 'and' and 'but' results, one for character development, both from [Abulafia](http://www.random-generator.com/index.php?title=Main_Page) under CC-BY
* added 'secrets & triggers' panel for adding some surprises to your games
* moved the save for images to the config.user variable, just to eliminate the extra file
* updated help pretty thoroughly
* added a manual edit flag to config to help protect against manual editing overwrites

Version 1.0.0

* added an image panel to the map stack that reads all files out of an 'images' subfolder in a save game and displays them
* combined status and main save files; should load old format fine still too
* seed curation. so much seed curation, so much more needed
* fixed a bug with the actor panel titles; should update correctly now
* new per game setting to determine how many half size (attribute) rows show on a character sheet
* character sheet stack titles will update as soon as the name or nn (nickname) field is exited now
* fixed yet another issue with the collapsing html output; should work now
* tweaked some of the random content on the actor panel to be less gender specific and more broad
* fixed issue where map panels weren't loading pre-existing maps on start
* adjusted the "Generate Grid Room Pattern" some more, added graphical representations
* removed most of the ways to set plain text formatting to streamline interface; use kivy [markup](https://kivy.org/docs/api-kivy.core.text.markup.html) inline if needed

Version 0.9.0

* added in a merge toggle for merging behavior and moved "about" to the title screen
* rewrote the kindom generation on the world panel with new, more useful generators
* wrote up a rough part by part documentation
* more seed curation; there are a LOT of seeds to go through. Recommend using "hardboiled" or "medieval romance" for the most curated results
* hitting "enter" with no input focused will now take a screenshot if debug mode is on
* button for showing the full map and saving a screenshot to your save directory
* fixed up map panels a bit, streamlined saving (no more auto-save)
* new options in the world generator panel for generating grid patterns (rough)
* added a simple grid map panel for grid-based dungeon crawls
* merge mode; choose if your save game consolidates sequential identical tags or not (or vice versa)
* dice presets cleaned up, now customizable in config
* buttons now have a border for better usability
* as always, bug fixes

Version 0.8.0

* formatting now pulls from the config file and can be set on a tag by tag basis
* refactored some things to help avoid identification issues when two lines of block text were identical
* added a toggle for a basic "debug mode" to config; with it False you will see a lot less messaging, with True, a lot more (and hopefully more helpful) messaging. If your game is working correctly, ignore the messaging
* fixed scrolling and jumps and bookmarks so hopefully they work correctly now
* basic "Find" and "Next" functions for quickly jumping around (still experimental).
* deprecated "don't show" in favor of "ephemeral"; ephemeral now triggers the old "don't show" behavior
* renamed 'clean' to 'fiction' and 'cedit' to 'fic-edit' (for now)
* separated out block formatting into clear "fiction" and "mechanics" categories; the appearance is the same but "mechanics" tags won't show in "fiction" editing modes or in fiction-only logs
* added support to logs for some markdown tags if placed in blocks (italic, bold, superscript, subscript, underline, strikethrough). Underline and strikethrough won't display in block but the markdown and html logs will appear correctly
* moved play logs to a sub directory and added some "no mechanics" versions
* updated PC panel to support multiple PCs; renamed to "Character Sheets"
* pulled out unused stuff from pythia.py
* updated post and pretitle to textfields and cleared config issue carrying them over
* "resolved" status for a thread will now send it to the bottom of the list
* seeds are much better curated (but there's still a lot of them so I might have missed something)

Version 0.7.1

* fixed a couple of issues related to refactoring the main display routine, mainly formatting updates on status toggle and editing text carrying over to every mode. Looks great now!
* a few other bug fixes
* removed some old commented out code

Version 0.7.0

* refactored main display routine so switching modes should work much much faster now.
* actor index to make navigating long actor rosters easier
* "don't show" status; items with this tag will no longer show up in main window. Ever.
* added a new but/and/- oracle weighted towards lots of events
* added two new Simple World (Apocalypse World) inspired generation buttons for actor/plot moves
* reversed panel adding order
* curated the seeds (barely, likely still a few misses) and revamped core seed panel to support user-generated seeds
* new default setting so you can choose the seed pattern and source you prefer per game
* new core panel for several seed patterns and sources
* new config variable to control pattern and source for seeds
* bugfixes, notably with configs from loaded gaming bleeding into new game

Version 0.6.0

BIG STUFF!!!
* toggle to disable core tools and core oracle on scenario by scenario basis
* added in a story/scenario mode that supports user-created 'modules'
* to skip this, just use the blank template when creating a new game
* lots of fun scenario support, including hyperlinks, descriptive passages, inline toggles
* wrote really basic sample scenario based on part of [Oracle's Decree](http://blog.trilemma.com)
* diagram dungeon mapping panel for simple mapping while exploring
* diagram dungeon minimap & nav panel for those of us affected by the Kivy-Mac-??? x-axis scroll issue

Version 0.5.0

* added more font size options to base config; still need to work on font sizes
* fixed bug with terrain generation & a few other minor bugs
* added a whole bunch of new generators to the world panel (was wilderness panel)
* added a random event system with trigger (5% of the time) to fu oracle
* added manual random event buttons
* fixed bug with collapsing html log
* removed exception catcher on user panel import to facilitate troubleshooting user panels

Version 0.4.0

* cleaned up bookmarks so they should work better in all modes
* basic backup system that saves the entire save folder on program load with timestamp
* improved saving to log files for sharing, should happen on loading a game and on every save now
* added a "clean edit" mode for editing just narrative text ('no_format' tag) and cleaned up other modes
* tweaked actor generators for broader results that should be more interpretive & to offer more options
* added 'unknown' status tag for actors your hero hasn't met yet
* set actor panel and thread panels to hide 'don't show' status tagged items on Save button press (they're not erased, just not visible until you restart the game or edit the status tag manually)
* added jump button to top of main log window so you can quickly go top to bottom and back
* added buttons to each side tracking panel to copy text from panels into main window quickly

Version 0.3.0

* improved autosave on exit
* clarified fu oracle results
* improved enter key toggle to support more behavior options, including none
* lots of bug fixes
* added more words to complex answer pool
* tweaked some result pools to be more sfw
* removed simplejson dependency in favor of python's built-in json
* added a better html output with collapsing sections

Version 0.2.0

* better support for user panels
* improved "on enter" behavior so user panels can self-update
* new config.user variable dictionary for saving variables from user panels
* updated the oracle/sample.py file to be clearer, have more examples
* renamed save game config file from "variables.txt" to "config.txt"
* improved actor charts, including personality, motive, and appearance generators
* lots of minor bug fixes

Version 0.1.0

* initial release
