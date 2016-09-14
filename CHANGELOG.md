####Changelog

Please note that this is very rough and just to give you an idea of what's been changed or improved. API breaking and save game breaking stuff may happen fairly frequently until we get up to 1.0!

MAKE BACKUPS BEFORE EDITING FILES MANUALLY.

Next Version

Version 0.6.0

BIG STUFF!!!
* added in a story/scenario mode that supports user-created 'modules'
* to skip this, just use the blank template when creating a new game
* lots of fun scenario support, including hyperlinks, descriptive passages, inline toggles
* wrote really basic sample scenario based on part of [Oracle's Decree](http://blog.trilemma.com)
* diagram dungeon mapping panel for simple mapping while exploring

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
