#Documentation -- Pythia 1.3.0

Table of Contents
=================

  * [Configuration](#configuration)
    * [Basics](#basics)
    * [Output Log Files &amp; Templates](#output-log-files--templates)
    * [Configuring Panels](#configuring-panels)
  * [Title Screen](#title-screen)
  * [Main Screen](#main-screen)
    * [Center Panel](#center-panel)
      * [Top Status Bar](#top-status-bar)
      * [Threads](#threads)
      * [Main Text Display](#main-text-display)
        * [Main Control Panel](#main-control-panel)
        * [Primary Text Input](#primary-text-input)
        * [Side Controls](#side-controls)
      * [Footer Controls](#footer-controls)
    * [Right Stack](#right-stack)
      * [Notes panel](#notes-panel)
      * [Actors Panel](#actors-panel)
      * [Character Sheets](#character-sheets)
    * [Left Stack](#left-stack)
      * [Oracle Stack](#oracle-stack)
        * [FU &amp; How's It Going](#fu--hows-it-going)
        * [Mythic Oracle](#mythic-oracle)
        * [Seeds &amp; Complex Answers](#seeds--complex-answers)
        * [Secrets &amp; Triggers](#secrets--triggers)
        * [Pythy Oracle](#pythy--oracle)
      * [Generators Stack](#generators-stack)
        * [Actors &amp; Motives](#actors--motives)
        * [Plot &amp; Monsters](#plot--monsters)
        * [World &amp; Dungeon](#world--dungeon)
      * [Map Stack](#map-stack)
        * [Grid Map](#grid-map)
        * [Diagram Map](#diagram-map)
        * [Images](#images)

###### Created with [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go).

## Configuration

### Basics

Always save backup copies of your text files in a separate directory outside the main Pythia directory before trying a new version or making any changes! And check your saved work occasionally by hitting save and then opening up one of the log files to make sure things are saving as you expected them to.

You can also open up the 'pythia.py' file in your favorite text editor, then comment out (or change the values of) these two lines:

`kivy.config.Config.set ( 'graphics', 'width', 1280 )`<br>
`kivy.config.Config.set ( 'graphics', 'height', 725 )`

Most of the program's user data is saved in plain text files (in json format).

MAKE BACKUPS BEFORE EDITING FILES. It takes two seconds to right click on your save folder and 'compress' or 'save as zip' then drag and drop the zip somewhere else. See also "Config Flags"; there's a manual_edit_mode that will help protect your data when editing those files directly.

__I strongly suggest that you use a [json editor](https://github.com/josdejong/jsoneditor) when editing save game files. Just unzip the release, then open the "04_load_and_save" file in the examples directory in a modern browser.__

There are two types of config files, the main config.py (not json) and a config.txt per game. The main config in the pythia root directory; you can edit this as much as you'd like and all changes will propagate to any new games (but not existing ones).

You'll find your save games in the pythia folder under 'saves'. Backups are in the "backups" folder. Pythia automatically makes a zipped backup of your current saves director and places it in backups when you start up Pythia.

To reset the quicksave, just delete the entire quicksave folder in the saves folder, then remake it at the title screen.

__*Config Flags*__

If 'manual_edit_mode' is set to True, the game will no longer overwrite the main.txt with "the adventure begins" on a failed save game load. It is much better to just use a json editor instead of messing with 'manual_edit_mode'.

__It will also no longer save any changes made in Pythia itself until the manual_edit_mode flag is set back to False.__

If 'debug' is set to True, you'll get a lot more messaging than default. Some of it might even be useful if you're having an issue. Most of it is simple notifications and should be ignored, especially when making a new game.

If there are entries in the "backup_behavior" list, specifically "app_start" and/or "app_exit", Pythia will zip up your save folder when one of those events occurs. If this list is empty, no backups will be made at all.

If the backup_limit is set to 0, Pythia will keep all backups. If it's set to a negative number, no backups at all will be made (regardless of backup_behavior). If it's set to a positive number, only up to that number of backups will be made, and older ones will be deleted when a new one is made.

Everything in config.py should be pretty well documented in config.py's comments.

### Output Log Files & Templates

Output log file templates are stored in "resources/logforms".

Current templates include html with javascript, html fiction only, html complete, markdown fiction only, markdown complete, markdown prepared for conversion via pandoc to pdf, and markdown versions with YAML headers pulled from config.py.

By default, only a few log files are enabled. To disable a log template, change "False" under "exclude()" to "True". To enable, set it back to False.

To make a new template, duplicate an existing one and change the "makeLogFile" routine.

### Configuring Panels

By default, all Pythia core panels (in "resources/panels") are enabled except gridmap.py. To disable a panel, change "False" under "exclude()" to "True". Setting exclude() to return False will enable it. You may experience odd results if you disable a panel other widgets rely on, so proceed with caution.

For Seeds, simply delete or rename any files in the "resources/panels/seeds" folder you don't wish to have show up in your Seeds panel. Be sure to delete (or add) all four subtypes when changing seed source files.

You can choose to exclude each map panel from being shown on a game-by-game basis by setting the "exclude_\<mapname.py\>" variables in config.general to True.

__*Setting Up Oracle Defaults*__


The key variables in config.py that control which oracle is called by the "???" and Seed buttons are "oracle", which should be the name of the file containing the oracle, and "oracle_func", which should contain the name of the oracle function in that file.

Note that the seed function in the general section only takes the four options listed -- it handles Mythic as a special exception case.

To revert to FU oracle as the default for new games, set the following in the config.py:

`oracle = 'fu'`

`oracle_func = 'fu'`

And in the general section:

`general['seed_func']= 'useTwoPartSeed'`

To use Mythic as default:

`oracle = 'mythic'`

`oracle_func = 'mythic'`

And in the general section (if you wish to use the Mythic seed tables):

`general['seed_func'] = 'useMythicComplex'`

## Title Screen

By default, the last game run is re-opened when Pythia is restarted. "Load" will show a list of all potential save game folders.

When creating a new game, you'll be given the option of a scenario or "blank" game. You'll generally want to choose "Blank" or "No Template" since Scenario support is rudimentary at the moment.

If you change the theme, you'll need to restart the program for it to take effect.

## Main Screen

### Center Panel

#### Top Status Bar

From left to right, there's an up/down tracker, bookmark buttons, a button to temporarily display only prose tagged blocks, and a spinner to control the behavior of the enter key when the text input is focused.

The up/down tracker is pretty self-explanatory; it was originally designed to track Chaos Factor but you can use it for whatever you please. I generally just use the "Tracker" panel for most things like that, but it's nice to have a dedicated spot for Chaos Factor since it has to be changed so frequently.

The bookmark panel consists of five bookmark slots and a "Clear" button. If you're not editing a specific block, you can click on one of the slot buttons (marked with a "-"), then on that text block, and store its index for later reference. Clicking on the bookmark again will jump back to that referenced block. To clear a bookmark, click the "Clear" button and then on the bookmark slot you want cleared.

"PROSE" will temporarily remove all non-fiction-tagged blocks from view. The view will reset if you edit a block or create a new one.

The enter behavior spinner allows you to choose what text is automatically tagged with when you hit "enter" while typing in the main text input. "Plain" and "Aside" modes correspond to the "Direct" and "Aside" buttons in the bottom control panel.

"None" reverts the text field's behavior to default for Kivy -- hitting enter will not send text through. In this mode, if you want to submit the text field's contents, you need to click the Direct or Aside buttons.

__Some generators will pass the text field's text into the main log but others won't, so use caution when writing long blocks of text in "None" (or any other) mode.__

#### Threads

The threads section has two buttons, "copy to main window" and "random thread". These are context-sensitive and pull from the specified panel.

"Copy to main window" copies the contents of your thread panel into your main text log. This is useful if you're posting sessions serially and want to be able to recap or set the scene for a new session.

The "random thread" button will pick a random thread from existing threads by keyword. The default is "All" but you can specify a tag or keyword to use by typing it into the text input.

####Main Text Display

The main text display consists of a nav bar and the main text blocks. The nav bar has a "top/bottom" jump button a "find" button, and a "next button".

The top/bottom jump button just goes from top to bottom.

The "find" button takes whatever string is entered into the text input and jumps to the first block containing an instance of it if that block is currently displayed. Use the "next" button to jump to the next displayed block that contains the text, and so on.

The main text blocks are displayed as labels by default. Click on a text block to make it editable; click on the "done" button to return it to a label.

#### Main Control Panel

At the bottom of the center panel is the main control panel. It has the primary text input, the footer buttons, and the side control panel.

#### Primary Text Input

The primary text input is how you get text into the program. It also supports passing information to various other buttons across the program, like the different "random [item]" buttons, the dice roller, and the "find" button.

To roll dice without using the "Roll Dice" button, you need to be in a text entering mode other than "None". If you begin your string with a number or include the keyword "roll" anywhere in the string, Pythia will check if the string contains any dice notation segments (2d8, 2d6x3, and so on) and, if so, roll them.

If you include the keyword "??", it will return your text as a query then call an oracle automatically after you hit enter.

Finally, you can tag your blocks automatically with "-p" (plain) or "-a" for aside. This must be the first or last element in the text input and any other keywords will override it. Hit "enter" to pass the keyword to Pythia.

#### Side Controls

The side control panel has a quick oracle button ("???") that generates an answer to a yes or no question. Which oracle is used by default can be changed in the config file; it defaults to "Fu" at even odds.

"Direct" and "Aside" send text from the text input to the main text display with "Plain" (prose) or "Aside" (mechanics) formatting.

"Roll Dice" takes an input from the main text input in the format "[count]d[sides]", ie, 1d10 would roll one 10-sided die, or 3d20 would roll three 20-sided dice, showing individual rolls and the sum. Adding "x[reps]" to the end repeats the action [i]reps[/i] number of times. So 3d20x5 would roll three 20-sided dice, displaying each roll and the sum, three full times.

"Seed" will be either one or two buttons, depending on which Seed schema you've chosen. By default, "Seed" (or "Complex") returns a two part string chosen from an "verb" "noun" set of lists. If you choose a two part seed scheme, it will be "Desc" ("adjective" "noun") and "Action" ("adverb" "adjective").

#### Footer Controls

__*Flags*__

The first button cycles the main control panel between mythic oracle and fu oracle.

"DQ" is "dice qualities". When this is toggled on, all dice rolled will have a quality attached. See the section "Resolution Clarifiers" under "Oracle Panel" for more information or read the original [article](http://thealexandrian.net/?p=2781) here.

"Save" immediately runs the save routine, saving the game and the configuration file.

__*Add*__

The Add section is how you add threads and actors to those sections; pressing either will take the text in the text input and turn it into a suitable entry.

__*Pick*__

The Pick section has four buttons, each of which takes a comma-separated list ("one, two, three, four") in the text input and attempts to return a random choice from it.

* "Pick List" will choose one option at random.
* "Pick 2d6" will roll 2d6, giving a range from 2 to 12, weighted towards 7.
* "Pick 2d4" will roll 2d4, giving a range from 2 to 8, weighted towards 5.
* "Pick 3:2:1" rolls a d6 and on a 1, 2, or 3 returns option 1, on 4 or 5, returns option 2, and on a 6 returns option 3.

__*Dice Presets*__

The Dice Presets section lets you click a button to roll that quantity and sides of dice, quickly. It can be configured in the config file. The right most two buttons are spinners that let you roll up to 10x quickly.

__*Dice Parsing Presets*__

This is a section for dice rolling mechanics that require more complicated parsing than just rolling plain dice. Parsing that can be off-loaded to the program.

The "ORE" button is for "ORE" style result parsing -- you roll a pool of dice and sort out the matching sets and waste dice.

There's room for one more scheme if anybody can suggest a good one!

### Right Stack

#### Notes panel

This is used for miscellaneous notes, status conditions, and things like health tracks. Each line has a checkbox so you can note if a line is active. "Random track" defaults to returning a random choice from all active tracks.

#### Actors Panel

Enter actors by typing a brief text about them into the main text input and pressing the "add actor" button. Text before the first comma is treated as the name or tag of the actor for the index.

Each actor has a tag/name, a text, and a status button.

"Random actor" picks from all actors, by default.

The Actor Index panel can be opened/closed by clicking on the title.

#### Character Sheets

Displays between 1 and 10 character sheets (depending on config setting).

If the sheet has a Nick", "NN", or "Name" tagged field, that field will be used for the title of the sheet.

"Random Major" defaults to looking at all "Name" tagged fields across all character sheets and returning one.

### Left Stack

The left stack contains oracles, random generators, and maps. User-created panels and scenario panels are also generally added here.

#### Oracle Stack

#### FU & How's It Going

*The FU oracle is based on FU: The Freeform/Universal RPG (found at http://nathanrussell.net/fu), by Nathan Russell, and licensed for our use under the Creative Commons Attribution 3.0 Unported license (http://creativecommons.org/licenses/by/3.0/).*

The FU oracle uses d6s and counts the number of odd versus even results to determine the answer. When asking a question of the oracle, press the text (or percentage) that matches how likely the answer is a "yes". The default "???" button maps to FU0, or "even odds".

Answers can be "Yes" or "No", either unqualified or with an "And" (an intensifier) or "But" (a complication or drawback). Extra modifiers occur if doubles are rolled.

There is a small (~5%) chance of a random event occurring.

You can also use this to quickly determine how an actor performs on a check. Just add up the number of penalties and the number of bonuses an actor has, on a scale of 1 to 5, and press that number. It can also be used for opposed checks as well.

A useful scale is 1, a bit, 2, fairly, 3, very, 4, extremely, 5, overwhelmingly. You can use the 'How Difficult Is It' generator on the World panel in the Generator stack to get a random modifier, too.

*Reil is fairly strong (+2) but the stone is very heavy (-3), for a net of -1. If I want to know if he can move the stone,  I click on the -1, or "Doubtful".*

*Reil is an expert wrestler (+3) and fairly strong (+2) but the town rowdy he's facing must have ogre heritage (-5). It's "even odds" if he can avoid being tossed out the window.*

The "How Much" button returns a weighted response; the first part is empirical, the second in context of expected results. Choose the answer that makes the most sense for your question.

>__*"How much does it cost?"*__<br>
>*[How Much?] A little or much less than expected.*

"How's It Going?" offers two columns, one for questions best answered with a "good" or "bad" response, the other for "yes" and "no" answers. Press the button that best describes the current state of events.

"Chaotic" will pick at random. "Same Old" weights towards the middle, and the other options tend towards more positive results or more negative results, depending on which you choose.

The "Chaos Oracle" returns a response weighted heavily towards random events and qualifiers. Use it when you want lots of information quickly -- or want there to be lots of excitement, mixed victories, and sudden reversals in your characters' lives.

>__*is my hero tied up?*__<br>
> *[Chaos 11] Yes, and, but*<br>
>__*Yes, and*__ *blind-folded,* __*but*__ *not gagged.*

__*Resolution Clarifier*__

Press the number corresponding to the dice you're about to throw, then roll as normal. Each qualifier result corresponds to one of the thrown dice, in order, left to right. If the roll succeeds, the higher of the two dice indicates why; if the roll fails, the lower of the two dice indicates why.

This is useful for describing why a roll succeeds or fails.

*Reil's player rolls 2d8 to evade the falling pillar, a DC of 13. The dice qualities are "Luck" and "Skill", in that order. Pythia returns (again in order) a 4 and a 6; not enough, so he fails! Matching qualities to the rolls means Luck was the lower and thus it was bad luck that he failed -- his foot slips or the pillar just happens to be falling in such a way he can't evade. If he'd succeeded, it would have been because of his skill -- his years of experience aided him or his intense physical training, perhaps.*

Uses ideas and terminology from this [article](http://thealexandrian.net/?p=2781); you should read it if you want to understand how it works, get proper definitions for each term, and for much, much better examples and adaptations.

You can set your own qualifiers in the config file. You can also toggle this to happen on every dice roll automatically using the "DQ" flag in the footer.

__*Hit Locations*__

Hit Locations works similarly to the Resolution Clarifier above, but returns one or more hit locations ("Head", "Left Arm", and so on). You can assign the results to each die you are about to throw or just grab one as needed. Useful for describing the outcome of a combat roll, or picking a body part if the question comes up.

You can set your own hit locations list in the config file.

__*But/And Clarifier*__

From [Abulafia](http://www.random-generator.com/index.php?title=But_Cards) under [CC-BY 2.5](https://creativecommons.org/licenses/by/2.5/). Having trouble thinking of a suitable 'and' or 'but'? Click on the appropriate button for inspiration.

>[likely: 6 2 5 ] Yes, and...<br>
>And you learn something about your enemies in the process.

__*Random Events*__

The Random Events section is used when events indicate a random event should occur. It has two parts. First, a spinner that can be used to select the subtype of events if desired or appropriate (you can use "Pick List" to pick which to use if you wish). "Random" will draw from all potential events.

To get a random event, once you've set the spinner (or left it at Random), choose how the scene is going so far or press "random", following the same principles as the "How's It Going" roll.

Results state the context, the effect, and if it's good or bad (and how good or bad it is). Draw a Seed if needed to help flesh out the answer.

> *[Random Event] Context: Plot! New thread. This is good.*

##### Mythic Oracle

*Content from the [Mythic Game Master Emulator](http://www.mythic.wordpr.com/page14/page9/page9.html) is used with the permission of the author under the condition that it not be used commercially. This content is not MIT licensed. Please see the mythic.py file for more information. If you want to use the oracle properly -- and for an excellent RPG -- buy the book!*

The first two elements are dropdown menus.

"Context" is reflected in the scene results but doesn't do much else. You should keep the context in mind whenever you have to interpret a result.

"Genre" is used by the scene generator and the random event generator. It also has an effect on how the chaos factor tracker works; for full range of movement with the tracker, change genre to "Standard".

"Get Scene" will get a Mythic-style scene.

> [CONTEXT] PCs (Start)<br>
> [FOCUS] Ambiguous event<br>
> [MEANING] Judge Messages

"Get Complex Answer" will get a Mythic-style two part answer, similar to a Seed.

> [Mythic Complex] Carelessness / Misfortune

__*Oracle*__

Choose an appropriate likelihood of the answer being 'Yes'. If you have set your oracle to mythic, you can then click the question button, or you can use the "Ask Oracle" button.

> [unlikely, 37>=35] NO

__*Opposed Checks*__

Choose the acting rank of your actor and the target difficulty (or opposing actor's rank). Use "Make Opposed Check" to see the outcome.

> [exceptional vs average, 92>=85] NO

__*Backstory*__

You can generate either a complete backstory (between 0 and 7 items, weighted towards the middle), or generate a single backstory event at a time.

> [FOCUS] PC Negative "Judge Military"

*Obviously our hero was court martialed at some point.*

You can set many of the parameters for Mythic in the config.py file, as well as disabling it. To revert to FU as default, set the following in the config.py (you can use the cycle button in each individual game):

`oracle = 'fu'`

`oracle_func = 'fu'`

`general['seed_func'] = 'useTwoPartSeed'`

#### Pythy Oracle

Largely based on Markov chains and Eliza. By default, it uses the current log as the source, but if you create a file named "sources" in a save directory and put text files in it, you can grab Markov chain sentences from those sources or set one of those sources as default for the auto-predict.

> Sailing for London, I reembarked at once for the sensation which his offering created.

"Use Auto-Predict" is a toggle between "True" and False" and controls if predict is on. If it is, when you start typing for the first time in a session you will notice a few seconds of lag.

The "Predict Suggestions" section will show one or two word nouns phrases that Pythy determines are related to what you're typing. Use them as Complex Answers and Seeds or simply as inspiration.

The "Next Word" section shows what the system thinks is the most likely next word; you can use it as the predict suggestions box or to cobble together a GM-esque statement.

You can remove either section by setting the number for that group shown to 0 in config.py. You can turn off both by turning auto predict off entirely in config.py.

#### Seeds & Complex Answers

This panel holds links to all the different seed types and patterns available in the "seeds" directory.

If you need to answer a question like "what does it look like" or "what is it" or "what's this random event about" or just need inspiration, choose a pattern ("verb noun", "description", "action", and so on) and press the button for the appropriate genre. The default is "medieval romance". You can select the default for the current game by clicking in the column to the left of the option you'd like to set as default.

Note: if you are using Mythic as your seed generator and set a new default through the Seed panel, the only way to go back to Mythic is to change "seed_func" in your game's config.txt back to "useMythicComplex".

> __*I search the room. What do I find? (What Is It, Detective)*__<br>
> *[Seed] oblique clues*<br>
> I find a letter, but it only alludes to motive.<br>

> __*I pick up the sword, what does it look like? (Description, Fairytale)*__<br>
> *[Seed] asleep unfortunate*<br>
> Its power lies dormant, and it is cursed.

> __*Why is the Captain so anti-Empire? (Verb Noun, Planet Romance)*__<br>
> *[Seed] creep soldier*<br>
> He hates their soldiers because they raided his home during the war.

#### Secrets & Triggers

This panel is all about surprises.

__*Preset Triggers*__

The first section adds random triggers that will fire after a certain number of fiction blocks have been created. Click on the interval that seems appropriate, based on the current chaos/excitement level in your game, then continue playing as normal. When you see the event fire, hit the generator button it directs you to or make the check as instructed.

If you are asked to roll a check, do so, then use a custom trigger to see whether or not something really was there -- or if the dm is just messing with you!

The difficulties correspond to Scarlet Heroes' difficulties but shouldn't be too hard to translate to whatever system. "Expected" is a subjective target, meant to be used with Scarlet Heroes' threat adjustment system. It's essentially "as appropriate to this particular adventure" and can be interpreted as "average" or "simple" difficulty if you aren't using Threat.

Remember that the difficulty indicates the challenge, just as if a GM were calling for the check. So if you get a trigger for a Perception check, at "hard" difficulty, you should interpret that as (assuming it's not a false alarm) the bad guy is pretty good at sneaking around (or well-hidden). For an intelligence check, a "hard" difficulty might mean the fact is obscure, while an "easy" difficulty might mean it's almost common knowledge.

Keep a few at "random" duration active any time something interesting might happen!

__*Custom Triggers*__

If you think something might be present -- an ambush, a hidden treasure, a clue -- make an appropriate check as if a GM has called for it. You can use the 'How Difficult Is It' generator on the Dungeon panel in the Generator stack to get a DC if needed.

Then create a custom trigger based on the results of your check.

"Name" is a short, descriptive phrase describing the trigger. For example, "perc check at cave". This is displayed when the trigger fires, so you can determine the effects (or if it should be ignored).

"Interval" is a rough estimate of, if something is there, when it should come into play. If you've just entered a new area and think an ambush is likely, pick 'now', for example. If you're moving between rooms fairly quickly, you should generally use 'now' or 'soon'; otherwise, use whatever seems appropriate or 'random'.

"Succeed/Fail" is if you succeeded or failed at your check. Success returns an immediate response, while a failure is delayed between 1 and 20 blocks, depending on the interval.

"Odds" are the odds something might be there to be missed. In an area frequented by bandits? Maybe it's "likely". Just wandering around town? "Even odds" or "Doubtful" or "Unlikely".

When (or if) the trigger fires, it will tell you you missed something but now it has come to light. Ask oracle questions or draw a seed to determine what 'it' is, as usual, and apply penalties and drawbacks to the situation as expected from a surprise of that type, based on the original difficulty. For example, if you've missed a 'hard' Perception check, the enemy who leaps out to ambush you a few rounds later might be higher level than one who was hiding with an 'easy' Perception check.

If it doesn't make sense for the hidden thing to come to light at this point -- maybe you determine it's treasure you missed two rooms ago or an important fact is remembered that is no longer relevant -- just treat it as player knowledge and move on.

#### Generators Stack

#### Actors & Motives

This panel holds random generators related to creating "actors" for your stories and games. They can be used to make NPCs for your hero to interact with or to help flesh out your hero himself.

__Appearance__

These buttons are generally used when you first meet an NPC, to guide how they are described and their initial behavior.

"Age - Any" chooses from child to elder, weighted towards the middle of the range. "Age - Adult" should be used when a character is known to be an adult or to narrow it down if you get "Mature" on the "Age - Any" roll.

"Gender Appearance" is a simple flip of a coin between "male" and "female". You can interpret it however you want.

"Appearance Modifier" is things like "is younger than they appear" or "is in disguise". It's up to you to interpret this -- "older than they look" might mean they look very young for their age, or perhaps they're more experienced or world-weary, or perhaps they're a supernatural creature.

"Visible Quirk" is a detail you'd notice when you first encounter someone. Their height, their attractiveness, their gear or bearing or tattoos or gestures or expression. It's up to you if your hero notices these things.

The "Non-Visible Quirk" is used for behavior that isn't immediately apparent, like a stutter or tendency towards rhetorical questions or a phobia or a dislike for cats, that can help define the character in play. I tend to roll one of these fairly soon after the hero's initial impressions are noted, but before I start roleplaying the actor heavily.

> [Age - Any] Mature.<br>
> [Age - Mature] Late twenties.<br>
> [Gender Appearance] female<br>
> [Reality] Is impersonating or mimicking someone else in some way.<br>
> [Visible Quirk] very short<br>
> [Visible Quirk] very pale<br>
> [Non-Visible Quirk] lacks self-confidence<br>

__Motivations__

These are different ways of getting character motivations, goals, and outlook. You generally won't roll all or even most of these per character. I almost always do "Wheel" and "Immediate Goals".

__*Wheel (General Outlook)*__

The wheel button returns a line indicating the actor's primary emotions, followed by their primary (and possibly secondary) focus. You can interpret the parts separately or together, as seems appropriate to you.

>[Wheel]<br>
>[Strong] amusement, [strong] interest<br>
>[Focus] inappropriate target [secondary], secrets [primary]

*Obviously a super-spy with a weakness for the enemy's chief lieutenant, who he finds equal parts interesting and entertaining, even as he seeks out secrets to use against his enemy.*

__*Immediate Goals*__

Immediate goals returns two goals that the actor wants to achieve, along with how strongly he wants to achieve them and a context. The context can be interpreted as part of the goal or as the driving force for it, as appropriate.

>[Goals]<br>
>[Twinge] to transmit a disease, contagion, or state of being [hero's enemy]<br>
>[Driving] to learn how to socialize [hero's heritage]

*This actor is a biologically engineered vampire soldier who worked for the chief villain making more vampires for his undead armies. She's defected and has to learn how to fit in again with her people if she wants to survive.*

__*Conundrum*__

From [Abulafia](http://www.random-generator.com/index.php?title=Conundrum). Provides a suitably agonizing dilemma to motivate your hero or for you to explore as the theme of an adventure.

>[Conundrum] You survived moral depravity; can you survive a buried secret?

__*Relationships*__

These three buttons -- Close, Group, and General -- describe out a "first actor" feels about a "subject" (specific to each query type). The first actor is the primary source of the emotion or perspective. Each button takes two parameters in the text input, separated by a comma, generally prefaced with "the" if appropriate. If no parameters are in the text input, it will just use the listed defaults.

"Relationship - Close" ["The first actor, the second actor"] covers friendships, personal enmities, blood kin, essentially any time two people have a shared history based on proximity. It takes the parameters First Actor and Second Actor, with the first actor's actions and attitude being described towards the second actor. So if you ask "How does the hero feel about the king?", the hero is the first actor and the king is the second actor. If you reverse the question -- "How does the king feel about the hero?" -- the king is the first actor and the hero, the second actor.

> How does the merchant Jelur feel about his old school-mate Reil?<br>
> The first actor was childhood rivals with the second actor and expresses this covertly and passively.

*Jelur was childhood rivals with Reil and to this day he holds a grudge, acting against his old rival whenever it won't be obvious and he doesn't have to go out of his way to do it.*

"Relationship - Group" ["The first actor, the target group"] is used whenever an actor's affiliation is in question; it takes the parameters First Actor and Target Group.

> How does the merchant Jelur feel about the Circle of the Seven Suns?<br>
> The first actor wants the counsel of the target group and expresses this overtly and actively.

*Jelur thinks that the Circle might be able to help him prosper. He seeks out every opportunity to laud their good works and makes sure any visitors from the Circle hear him doing so.*

"Relationship - General" ["The actor, the target"] is used whenever a close connection is unlikely but you want to know how a target feels about a specific thing. It takes First Actor and Target, where Target is a person, place, thing, or whatever.

> Reil, the nearby swamps<br>
> The actor hates and fears the target.

*Reil hates and fears the nearby swamps, because his parents vanished there while picking berries several years ago.*

__*Actor's Next Move*__

The Actor's Next Move returns a move that indicates what the actor in question will do next. You can use this as frequently or infrequently as you wish. The "move" is generally a concrete instruction, while the "tag" in brackets points to motive or to general effectiveness.

*Reil has the assassin responsible for his parents' death at his mercy. The assassin claims he was coerced with magic. Reil's player isn't sure what Reil would do.*

> How does Reil proceed?<br>
> [Noble] Actor indulges or expresses a noble facet of their character.

*Reil finds he doesn't have it in him to murder someone in cold blood, let alone someone who was forced into evil deeds. Nobly, he turns the man over to the city guard -- and goes hunting for the sorcerer behind things.*

__*One Line Motive*__

If you find yourself asking why someone is doing a specific action or what an actor's end goal is, this is the button to push. You can also use this to determine your hero's starting goal, or to determine what the primary antagonist wants.

> [Motive] to overthrow a ruler to acquire something simply to have it

__*Get Character Trait*__

Returns a two word phrase describing a character trait, similar to a Seed but personality specific. Pull up to three of these to give a good picture of an actor. You can also use this trait in conjunction with the "Trait-Based Character Event".

> [Trait] "vigorous confident"

__*Trait-Based Character Event*__

Using a character trait (possibly one generated by "Get Character Trait"), generate an event stemming from that trait that happened in the character's past or present and affected him in some way.

> The event was a personal victory. It started in childhood. The actor was affected and it completely changed the actor's outlook on life. The immediate consequences were concrete. Currently, the consequences are secretly working against him. The actor pretends that part of him is set aside.

*Reil has always been good at athletic pursuits, with a naturally gifted physique. This confidence has defined him and led to his choice of career, but also led him to behaving less than kindly to those he perceived as weaker than he was. Secretly, an old childhood rival envious of his natural prowess and angry about past mistreatment is scheming against him. Reil is embarrassed about his past as a bully and does his best to avoid behaving like that now.*

__*Defining Attribute*__

This returns a character attribute and a modifier that indicates something the character is good, bad, or indifferent at. Use to ballpark an actor's stats, or similarly to "Defining Characteristic".

__*Defining Characteristic*__

This returns a character trait and a modifier that sum up the character in some way. You can use it to describe an immediate impression of the actor or to determine long term general tendency.

> [Defining Characteristic] The actor is very "lovely".<br>
> [Defining Characteristic] The actor is impaired "imaginative".

*When Reil meets Maela, a prisoner he frees from the Circle's secret prisons, he immediately falls in love with her lovely spirit and great personal beauty. However, he quickly realizes she's a bit, to put it nicely, overly literal, in a way that sets his teeth on edge.*

*[The GM assigns Maela a Charisma of 18 and a Wisdom of 8.]*

__Emotional Reaction__

This tool is used to generate an emotion and degree of emotion from a negative or positive list. It can be used as a reaction roll, in response to a successful or failed check, or it can be used simply to determine how a character responds to a particular crisis or event.

> A successful Persuasion check to convince the scout to help against the Circle.<br>
> [Reaction] Relief [driving]

*The scout is relieved someone's here to assist him, and that relief drives him to be as helpful as he can be.*

##### Plot & Monsters

This panel is all about plots and monsters. Surprisingly?

__General Plotting__

"Plot Premise" is a dropdown list of different formats for a randomly generated premise. They of course need interpretation.

> A taciturn bard wants to make the world a better place but can't have it because of dark secrets, so will sacrifice a rival in order to hire a scholar.<br>
> The decision to betray a demon hunter by a reckless grave robber sparks an unhappy harlot to set a trap. This hurts a depressed baron who is fighting the disposal of a blackmailer.

"Plot Web" will generate three actors, each of whom connects to another in a circle (the status quo). It then generates a fourth actor with two points of connection to the first three (the wildcard).

> An angry king is sleeping with a pathetic shopkeeper. A pathetic shopkeeper is pursuing a haughty monk. A haughty monk is drinking buddies with an angry king.  A disillusioned vampire is chasing after an angry king.  A disillusioned vampire owes money to a pathetic shopkeeper.

*The status quo involves the romantic entanglements of a king, a shopkeeper, and a monk. Into this heady mix comes a vampire who is chasing the king -- perhaps so that the shopkeeper he owes money to, once out of favor, can be disposed of?*

"Plot Move" chooses a potential GM-style move. Use to emulate a GM's actions or plot movement.

>*[Plot Move] Add or remove an NPC from the current scene or area.*

__Script Framework__

This is a simple tracker for a scriptwriting style plot. On the left is a dropdown menu for the current function of the scene (essentially an Act structure) and on the right is a tracker for whatever you'd like to track.

"Get a Scene" takes the current stage from the spinner and returns a scene description and a scene type.

>[Plot Point: Inciting Incident] Reversal of Expectations & Recognition, Dream sequence (1)

*In this case, the scene will feature a reversal of expectations and the sudden recognition of something. It also has a good chance of being a dream sequence!*

__Scene List__

These two buttons work together to provide interpretive scene descriptions. "Make List" will create a list of scenes ('elements') around three randomly chosen topics. "Get Element" will pop the first element off the list and display it.

> [Scene] common folk (overcome) secret
> [Scene] magic triumphs

You can use the word in parenthesis as a bridge between the two words, if it makes sense to do so, or simply look at each word as a separate element of the scene. The final scene for each topic will not have the bridge.

__Monsters__

Press the "new" button next to each field to generate a new monster in that field. Monsters are fairly abstract so they can be used with any system -- things like AC and attacks are left up to the GM's discretion. Press "new" again to replace the monster with a new one. You can edit your monsters directly in the fields, and they are persistent across sessions, but if you want to save a monster long term you should transfer it to a tracker slot or to an actor slot.

The number in parenthesis is how many are around, either in this encounter or total in the area. If the HD seems high, you can choose to divide it among the members of the group. Alternately, you can ignore the HD and count and use a different method to generate those.

> automaton or elemental (10) Int: none HD: 11 Traits: greedy, perverse SA: None

*Since there are ten of them, the DM decides to divide the 11 HD among them, giving 9 with 1 HD each and one with 2 HD. They are mindless automatons, operating solely on their programming, which is to collect items to repair broken machinery. Perversely, they continue to do this even though their makers -- and the machinery -- are long gone.*

> insect-humanoid (2) Int: high intelligent HD: 11 Traits: rapacious, chimeric SA: spell-like ability resembling 2nd level spell

*A bizarre centaur-like hybrid of mindflayer and ant, these creatures display a rapacious intelligence but seem only interested in one-upping each other in petty schemes. Fortunately, there are only two of them, but each is a fearsome foe. Notably, if one touches a victim in melee, the victim takes a d6 penalty to Intelligence, Wisdom, and Charisma (down to a minimum of 1) that lasts until their next full rest.*

"Copy Monsters To Main" copies your monsters into your main log.

"Clear Monsters" erases all of the fields.

##### World & Wilderness

These generators help flesh the world out when a simple "Yes/No" question doesn't seem sufficient.

__Kingdom Generator__

__*Make Kingdom*__

Choose an era, "Modern" -- with results ranging from as vast as Russia to as small as Hong Kong -- or "Medieval" with results skewing to the much smaller end. Returns a kingdom size and a modern country about that size that you can use purely for size comparison or take cultural inspiration from as well.

__*Power Structure*__

Returns a power structure for your new kingdom, complete with general ruling style, primary leader, and important factions.

> [Power] It is formally anarchic. The highest authority is an elected body of ex-soldiers that has the support of a weak trader partner and the enmity of the dutiful.

*Looks like a neighboring kingdom-funded coup to me; the ex-soldiers elected themselves, the 'dutiful', ie, the loyalists, are still fuming about it, and the power base hasn't been consolidated enough for anyone to get anything of note achieved.*

__*Known Quirk*__

Roll this to get a fact or rumor that "everyone knows" about the people of your new kingdom or village. Whether or not it's true is up to you (and your oracle). You should likely roll up several of these, ranking them from "strongest" to "weakest".

> [Known Quirk] The majority are proud of a local ability like sailing, fishing, or navigating swamps.<br>
> [Known Quirk] The common folk are very traditional.<br>
> [Known Quirk] Criminals are very poor

*The locals, known as "fen-folk" are justifiably proud of their long tradition of navigating the local fens. They carry this traditionalism into every aspect of their lives, including their criminal punishment system, which is elaborately built on a system of weregild and fines that generally mean a bad or unlucky thief is a poor one.*

__*Secret Quirk*__

Roll this to get a fact or rumor that is only whispered about -- or perhaps nobody dares to do even that -- about the people of your new kingdom or village. Whether or not it's true is up to you (and your oracle).

> [Secret Quirk] The church leaders are cursed with ill-luck.<br>
> [Secret Quirk] The poor are blessed with good luck.<br>
> [Secret Quirk] The ruler's advisors are fomenting rebellion.

*The traditional fen-folk stubbornly cling to their old traditions and rituals of propitiation, bringing them continued good luck, while the determined friars of the new religion seem cursed at every turn. The devout whisper of divine wrath. One of the high-ranking enlisted men is secretly a loyalist looking for allies.*

__Region Diagram Dungeon__

This allows you to determine hex or block terrain on a somewhat procedural basis.

__*Make a Region*__

This is used when you first enter a region. If you know the starting population density, change the spinner to it, otherwise leave it at random, then press one of the "Make a Region" buttons (roll 1d9 to pick one at random) to get the starting terrain.

If you're leaving one region and entering another, press the button numbered for the terrain you've just left.

__*Upcoming Terrain*__

Once you know your starting terrain, you can generate more terrain as you leave each block and enter a new block.

__*Distance to Next Region*__

This gives you a distance in [units] of ideal travel time (easiest is for each "unit" to correspond to one "day" of travel or block on the map).

*Reil enters the notoriously dangerous realm of the sorcerer-king he's heard is in thrall to the Circle.*

> [Settled Level] Dense [Seed] 4<br>
> [Terrain Type] plains (1) | heavy forest | light forest (3) | hills (4)<br>
> [Settlements] ['Town', 'City', 'Town', 'City', 'Town']<br>
> [Beneath] Ruins<br>
> [Known Ruins] ['habitation', 'sewer']<br>

*It's a densely settled area, predominantly plains, with some light and heavy forest and a few hills. There are two major cities and three towns; beneath the area is a sprawling set of ancient ruins. One of the major cities has been decimated by plague and lies abandoned. Adventure also can be found in the sewers beneath the remaining city, the sorcerer-king's capital.*

> [Time Units] 1 [Road?] No

*Reil decides to travel from his location to the nearby active city. It will take him one day to get there.*

*This means marking down one block's worth of exploration; as he enters the block, roll for upcoming terrain.*

> [Terrain] plains (1)

*Unsurprisingly, the terrain is flat, level plains. Any encounters will be drawn from that pool, as well as any hazards, features, or the like.*

__Miscellaneous Questions__

"What's the Weather Like?" is in context of yesterday's weather.

##### Dungeon & Underground

The dungeon panel is, unsurprisingly, for generating dungeon content. The general order of things is to use "What is the Room Like" and "First Impression" to get an idea of what the room looks like and what it contains at first glance, then use "What Do I See?" (if necessary) to determine if there's an overtly hostile or dangerous situation.

__General Questions__

"More or Less Than Expected" requires a general idea of the quantity, size, or duration. If you enter text into the text input, it will replace "expected".

> "Is the ogre larger than expected?"<br>
> [More or Less] A bit less than expected.

> "How long will it take?"<br>
> "a few hours"<br>
> [More or Less] Less than a few hours.

"How Difficult is It?" returns a statement on how hard the task or feat is, along with a suggested modifier to the DC.

__"What Do I See?"__

"Monster, Treasure, Trap" tells you basic room contents (monster, treasure, special, etc.) using a d6 distribution from early D&D (or you can set it to a more Gygax-ian distribution in the config file). If it's a trap, it will return "Empty" and set the result of the "Trap" button to the truth.

Explore the room, make any rolls you need to, and then hit the "Trap" button to see if there was one there!

__"What's So Special?"__

I tried to stay away from "gonzo" but results will still need to be interpreted for your surroundings. If something doesn't fit, discard it. Or maybe it's a toy version! The items in this list range from simple dungeon dressing through encounters.

"First Impression" rolls up a random number of special features that represent the things you can immediately see on first glance.

"Single Item" returns a single item, maybe suitable for discovering behind, under, or beneath other items, or noticing after a fight finishes, or if you want some bit of dressing to make a fight more interesting.

"Make a Saving Throw" is for after you've investigated that special feature, if it's something unusual (or if your "Trap" roll says it's a trick or trap).

__"Point Crawl Dungeon"__

This is a very simple freeform, node-based dungeon generator, intended to be used with the other tools on this panel. It basically creates a list, named either "Dungeon 0", "Dungeon 1", and so on, or whatever is in the main text input when you hit "New Dungeon".

"Next Area" will generate a theme for the dungeon and a number of rooms to explore before rolling up a new theme. As you explore, you will occasionally locate connections to previously explored areas. Themes can be set in config.py on a game-by-game basis.

"New Theme" will generate just a theme ("Ice", "Fire", "Treasure", and so on). This is not saved as part of the current dungeon.

"New Type" will generate a new type ("City", "Lair"). This is not saved as part of the current dungeon.

"New Activity Level" will generate a random activity level for the area. This is not saved as part of the current dungeon.

"New Dungeon" will take the currently entered text in the main input or the next index in the saved dungeons list and make a new empty slot for it.

__"What Did It Do?"__

This is a long list of terrible, baffling, interesting, and occasionally awesome things that can be inflicted on a hero who messes with things Man Was Not Meant To Know. Useful when exploring dungeons if you run into old altars, malfunctioning machines, or suspiciously serendipitous fountains. Also useful if you're hit with a magical spell or curse or a faerie decides you need magicking. Or drink a potion. Or need a wild surge effect.

It's fairly OSR, but I tried to stay away from things that would shut a game down or just be embarrassing or that were boring. I'm sure I didn't succeed; use this chart only if you're okay with your hero ending up one inch tall and blue, or with zero sex appeal and blind, or with a Dexterity of 3 and a phobia of fish. You can enter your own list of effects in config.py (and opt to replace all of mine if you wish).

You'll note I did not put a duration on the effects. You can either use "How Much" with a base duration of twenty-four hours, do a "Pick One" for the various options ("permanent", "one month", "one week", "one day", "a few hours", "a few minutes", "one round"), or just ask your oracle. Remember, though, you should never ask the oracle a question you don't want to hear a "Yes" answer to...

__Diagram Mapping__

"What Direction?" is used when mapping, to determine what direction an exit is located in.

"What is the Room Like?" can be used while mapping or any time a room description is needed. It should be interpreted in context of the adventure.

> [Room] gleaming, wood [Purpose] bodily functions [Size] expansive [Shape] square

*If my hero is storming a castle, it's a lavish spa room, all gleaming wood and white tile. If he's exploring a ruin, it's a latrine for ogres, open above to the gleaming stars and night sky.*

"What is the Passage Like?" is rolled when you leave a room headed elsewhere.

> [Passage] slopes up or passes stairs [Special] a exit or arch or gap in the wall

*Heading deeper into the ruin, Reil quickly realizes the passage is sloping upwards. A gap in one crumbling wall leads into darkness.*

"How Far Is It" is used when you need to know how close something is. Need to know the range to the high priest's altar? Use "same room". Know the item is located somewhere in the ruin complex but not exactly where? "Same area". Know it's in the same kingdom or forest? "Same region." Have no idea where it is? "Anywhere."

__Grid Mapping__

The grid map options are used in conjunction with the grid map panel or with a piece of graph paper or a similar program. Each button returns a set of coordinates you can click or fill in to make a room or passage. Obviously, sanity checks are needed; if something doesn't make sense, connect it differently or skip it.

"Get Grid Room Pattern" returns a room-shaped graphic that should be pretty easy to translate to grid paper (or the grid map panel if you're using it).

> [Grid Room] <br>
> \* * * * * * *  <br>
> \* X X X X X *  <br>
> \* X X X X X *  <br>
> \* X X X X X *  <br>
> \* X X X X X *  <br>
> \* * * * * * * <br>

> [Grid Room] <br>
> \* * * * * * * * * *  <br>
> \* X X X X X X X X *  <br>
> \* X X * * X X * * *  <br>
> \* X X * * X X * * *  <br>
> \* * * * * * * * * *  <br>

"Get Grid Corridor Pattern" returns a corridor. Use "Get Grid Exits" to determine how many exits and which direction they are first.

> [Corridor] 1 by 3, 1 by 8 intersection at 2

*This is a t-shaped intersection, one square wide by three squares long, and right in the center it's bisected by a perpendicular hallway eight squares long and one square wide.*

#### Map Stack

Both map panels share the same buttons.

"New Map" makes a new map.

"Full Map" shows the current map and saves a screenshot of it.

"Show Minimap" shows a small minimap version of the current map.

The spinner shows all available maps to load; choosing one loads that map.

The compass rose moves the viewport around the map, or you can scroll if your mouse supports it.

The first thing you should do when making a new map is to enter a title in the top input and hit "Save".

Finally, there are a number of tools on the World Panel in the Generators Stack for generating content for the different maps.

#### Grid Map

*Grid mapping is excluded (turned off) by default.*

This works like a sheet of graph paper. Click once to change the background color, click again to return it to base. You can enter a single digit or letter into any square.

#### Diagram Map

The black squares are "rooms" or "blocks" and can be labeled, and the areas between can be clicked to set links between two blocks or rooms. Click repeatedly to cycle through the various types of connections.

#### Images

To use this panel, you need a subdirectory in your save folder named 'images'. Any images in the images folder will be displayed in the images panel, along with a couple of fields each to label or store notes about each picture. It's pretty basic and doesn't correlate labels with images, just saves them in order.

Note that the images directory is not created by default with a new game!
