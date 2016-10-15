#Documentation -- Pythia 1.0.0

##Configuration

__*Basics*__

Always save backup copies of your text files IN A SEPARATE DIRECTORY OUTSIDE THE PYTHIA DIRECTORY before trying a new version or making any changes! And check your saved work occasionally by hitting save and then opening up one of the log files to make sure things are saving as you expected them to.

If the app window is too big or two small, you can adjust it by setting the size, either in the pythia.py file or at the command line.

`python pythia.py --size 1280x725`

You can also open up the 'pythia.py' file in your favorite text editor, then uncomment these lines:

`kivy.config.Config.set ( 'graphics', 'width', 1280 )`<br>
`kivy.config.Config.set ( 'graphics', 'height', 725 )`

Change the numbers (1280, 725) as you'd prefer.

Most of the program's user data is saved in plain text files (in json format); make a backup and then open up some save game files and see what's in there. You can edit past entries, change configuration values, even set a custom pre and post title for your game (look for those entries in 'saves/\<game name\>/config.txt' and the '---').

There are multiple config files, the main config and one per game. The main config in the pythia root directory; you can edit this as much as you'd like and all changes will propagate to any new games (but not old ones). You can always make a new, fresh game, and copy that config into older save games to 'refresh' them on upgrades.

Formatting is set in the config file and on a per game basis. If you really want to change something, you can scroll to the bottom of the config file for the app-wide derived font settings.

To shut down, click the x in the upper left of the main window or just close the terminal. You'll find your save games in the pythia folder under 'saves'. Content is saved pretty frequently but be sure to hit the 'save' button before closing down to be sure. Backups are in the "backups" folder. Pythia automatically makes a zipped backup of your current saves director and places it in backups when you start up Pythia.

To reset the quicksave, just delete the entire quicksave folder in the saves folder, then remake it at the title screen.

Note: the system expects a quicksave folder to be present and it's a good idea to have one.

MAKE BACKUPS BEFORE EDITING FILES MANUALLY. It takes two seconds to right click on your save folder and 'compress' or 'save as zip' then drag and drop the zip somewhere else.

__*Config Flags*__

If 'manual_edit_mode' is set to True, the game will no longer overwrite a failed save game load with "the adventure begins". It will also no longer save any changes made in Pythia itself until the manual_edit_mode flag is set back to False. This is so, if you're making manual edits, you have a bit of protection against missed commas or other json formatting issues in the main text file.

If 'debug' is set to True, you'll get a lot more messaging than default. Some of it might even be useful if you're having an issue. Most of it is simple notifications and should be ignored.

##Title Screen

When creating a new game, you'll be given the option of a scenario or "blank" game. You'll generally want to choose "Blank" or "No Template".

If you change the theme, you'll need to restart the program for it to take effect.

##Main Screen

###Center Panel

####Top Status Bar

From left to right, there's an up/down tracker, bookmark buttons, a spinner to control the display mode, and a spinner to control the behavior of the enter key when the text input is focused.

The up/down tracker is pretty self-explanatory; it was originally designed to track Chaos Factor but you can use it for whatever you please. I generally just use the "Tracker" panel for most things like that, but it's nice to have a dedicated spot for Chaos Factor since it has to be changed so frequently.

The bookmark panel consists of five bookmark slots and a "Clear" button. If you're in a non-edit mode, you can click on one of the slot buttons (marked with a "-"), then on a text block, and jump back to it whenever you want. To clear a bookmark, click the "Clear" button and then on the bookmark slot you want cleared.

There are five display modes; Play, Read, Edit, Fic-Edit, Fiction, controlled by the display spinner.

*  "Play" displays all prose-tagged and mechanics-tagged text in non-editable blocks with status buttons for toggling formatting status.
*  "Read" displays all prose-tagged and mechanics-tagged blocks in non-editable blocks with no status buttons.
*  "Fiction" displays just prose-tagged blocks in non-editable mode with no status buttons.
*  "Edit" is the most full-featured editing mode; prose-tagged and mechanics-tagged text blocks are editable and status buttons are visible.
*  "Fic-Edit" shows just editable prose-tagged blocks with status buttons.

The enter behavior spinner allows you to choose what text is automatically tagged with when you hit "enter" while typing in the main text input. "Plain" and "Aside" modes correspond to the "Direct" and "Aside" buttons in the bottom control panel. "Multi" makes the text input support multiple paragraphs -- in this mode, if you want to submit next, you need to click the Direct or Aside buttons.

####Threads

The threads section has two buttons, "copy to main window" and "random thread". These are context-sensitive and pull from the specified panel.

"Copy to main window" copies the contents of your thread panel into your main text log. This is useful if you're posting sessions serially and want to be able to recap or set the scene for a new session.

The "random thread" button will pick a random thread from existing threads by keyword. The default is "All" but you can specify a tag or keyword to use by typing it into the text input.

####Main Text Display

The main text display consists of a nav bar and the main text blocks. The nav bar has a "top/bottom" jump button a "find" button, and a "next button".

The top/bottom jump button just goes from top to bottom.

The "find" button takes whatever string is entered into the text input and jumps to the first block containing an instance of it if that block is currently displayed. Use the "next" button to jump to the next displayed block that contains the text, and so on.

The main text blocks are controlled by the "mode" button at the very top of the center panel. They may be editable or display-only, and may have attached status toggle boxes or not, depending on the mode.

The main text blocks might be one per entered chunk of text or merged, depending on if the "merge" flag is set in the footer.

####Main Control Panel

At the bottom of the center panel is the main control panel. It has the primary text input, the footer buttons, and the side control panel.

####Primary Text Input

The primary text input is how you get text into the program. It also supports passing information to various other buttons across the program, like the different "random [item]" buttons, the dice roller, and the "find" button.

####Side Controls

The side control panel has a quick oracle button ("???") that generates an answer to a yes or no question. Which oracle is used by default can be changed in the config file; it defaults to "Fu" at even odds.

"Direct" and "Aside" send text from the text input to the main text display with "Plain" (prose) or "Aside" (mechanics) formatting.

"Roll Dice" takes an input from the main text input in the format "[count]d[sides]", ie, 1d10 would roll one 10-sided die, or 3d20 would roll three 20-sided dice, showing individual rolls and the sum. Adding "x[reps]" to the end repeats the action [i]reps[/i] number of times. So 3d20x5 would roll three 20-sided dice, displaying each roll and the sum, three full times.

"Seed" will be either one or two buttons, depending on which Seed schema you've chosen. By default, "Seed" returns a two part string chosen from an "verb" "noun" set of lists. If you choose a two part seed scheme, it will be "Desc" ("adjective" "noun") and "Action" ("adverb" "adjective").

####Footer Controls

__*System*__

The System section has a "Save" button that saves the current state of the program to disk, a "Merge" flag that determines if blocks are merged or not.

__*Add*__

The Add section is how you add threads and actors to those sections; pressing either will take the text in the text input and turn it into a suitable entry.

__*Pick*__

The Pick section has four buttons, each of which takes a comma-separated list ("one, two, three, four") in the text input and attempts to return a random choice from it.

* "Pick List" will choose one option at random.
* "Pick 2d6" will roll 2d6, giving a range from 2 to 12, weighted towards 7.
* "Pick 2d4" will roll 2d4, giving a range from 2 to 8, weighted towards 5.
* "Pick 3:2:1" rolls a d6 and on a 1, 2, or 3 returns option 1, on 4 or 5, returns option 2, and on a 6 returns option 3.

__*Dice Presets*__

The Dice Presets section lets you click a button to roll that quantity and sides of dice, quickly. It can be configured in the config file. The right most four buttons are spinners that let you roll up to 10x quickly.

###Right Stack

####Notes panel

This is used for miscellaneous notes, status conditions, and things like health tracks. Each line has a checkbox so you can note if a line is active. "Random track" defaults to returning a random choice from all active tracks.

####Actors Panel

Enter actors by typing a brief text about them into the main text input and pressing the "add actor" button. Text before the first comma is treated as the name or tag of the actor for the index.

Each actor has a tag/name, a text, and a status button.

"Random actor" picks from all actors, by default.

The Actor Index panel can be opened/closed by clicking on the title.

####Character Sheets

Displays between 1 and 10 character sheets (depending on config setting).

If the sheet has a "Name" or "NN" tagged field, that field will be used for the title of the sheet, with "NN" having precedence.

"Random Major" defaults to looking at all "Name" tagged fields across all character sheets and returning one.

###Left Stack

The left stack contains oracles, random generators, and maps. User-created panels and scenario panels are also generally added here.

####Oracle Stack

####FU & How's It Going

The FU oracle is based on rolling d6s and counting the number of odd versus even results. When asking a question of the oracle, press the text (or percentage) that matches how likely the answer is a "yes".

Answers can be "Yes" or "No", either unqualified or with an "And" (an intensifier) or "But" (a complication or drawback). Extra modifiers occur if doubles are rolled.

There is a small (~5%) chance of a random event occurring.

"How Much...?" returns a weighted response; the first part is empirical, the second in context of expected results. Choose the answer that makes the most sense for your question.

>__*"How much does it cost?"*__<br>
>*[How Much?] A little or much less than expected.*

"How's It Going?" offers two columns, one for questions best answered with a "good" or "bad" response, the other for "yes" and "no" answers. Press the button that best describes the current state of events.

"Chaotic" will pick at random. "Same Old" weights towards the middle, and the other options tend towards more positive results or more negative results, depending on which you choose.

The "Chaos Oracle" returns a response weighted heavily towards random events and qualifiers. Use it when you want lots of information quickly -- or want there to be lots of excitement, mixed victories, and sudden reversals in your characters' lives.

>__*is my hero tied up?*__<br>
> *[Chaos 11] Yes, and, but*<br>
>__*Yes, and*__ *blind-folded,* __*but*__ *not gagged.*

"Plot Move" chooses a potential GM-style move. Use to emulate a GM's actions or plot movement.

>*[Plot Move] Add or remove an NPC from the current scene or area.*

The Random Events section is used when events indicate a random event should occur. It has two parts. First, a spinner that can be used to select the subtype of events if desired or appropriate (you can use "Pick List" to pick which to use if you wish). "Random" will draw from all potential events.

To get a random event, once you've set the spinner (or left it at Random), choose how the scene is going so far or press "random", following the same principles as the "How's It Going" roll.

Results state the context, the effect, and if it's good or bad (and how good or bad it is). Draw a Seed if needed to help flesh out the answer.

> *Random, random*<br>
> *[Random Event] Context: Plot! New thread. This is good.*

#### Seeds & Complex Answers

This panel holds links to all the different seed types and patterns available in the "seeds" directory.

If you need to answer a question like "what does it look like" or "what is it" or "what's this random event about" or just need inspiration, choose a pattern ("verb noun", "description", "action", and so on) and press the button for the appropriate genre. The default is "medieval romance". You can select the default for the current game by clicking in the column to the left of the option you'd like to set as default.

> __*I search the room. What do I find? (What Is It, Detective)*__<br>
> *[Seed] oblique clues*<br>
> I find a letter, but it only alludes to motive.<br>

> __*I pick up the sword, what does it look like? (Description, Fairytale)*__<br>
> *[Seed] asleep unfortunate*<br>
> Its power lies dormant, and it is cursed.

> __*Why is the Captain so anti-Empire? (Verb Noun, Planet Romance)*__<br>
> *[Seed] creep soldier*<br>
> He hates their soldiers because they raided his home during the war.

####Secrets & Triggers

This panel is all about surprises.

__*Preset Triggers*__

The first section adds random triggers that will fire after a certain number of fiction blocks have been created. Click on the interval that seems appropriate, based on the current chaos/excitement level in your game, then continue playing as normal. When you see the event fire, hit the generator button it directs you to or make the check as instructed. If you are asked to roll a check, do so, then use a custom trigger to see whether or not something really was there -- or if the dm is just messing with you!

Keep a few at "random" duration active any time something interesting might happen.

__*Custom Triggers*__

If you think something might be present -- an ambush, a hidden treasure, a clue -- make an appropriate check as if a GM has called for it. Then create a custom trigger.

"Name" is a short, descriptive phrase describing the trigger. For example, "perc check at cave".

"Interval" is a rough estimate of, if something is there, when it should fire. If you've just entered a new area and think an ambush is likely, pick 'now', for example.

"Succeed/Fail" is if you succeeded or failed at your check. Success returns an immediate response, while a failure is delayed.

"Odds" are the odds something might be there to be missed. In an area frequented by bandits? Maybe it's "likely". Just wandering around town? "Even odds" or "Doubtful" or "Unlikely".

When or if the trigger fires, it will tell you you missed something but now it has come to light. Ask oracle questions or draw a seed to determine what 'it' is, as usual.

####Generators Stack

####Actors & Motives

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

#####World & Dungeon

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

__*Sizes*__

These just return a population count for the various types of town you might encounter.

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

"More or Less Than Expected" requires a general idea of the quantity, size, or duration. If you enter text into the text input, it will replace "expected".

> "Is the ogre larger than expected?"<br>
> [More or Less] A bit less than expected.

> "How long will it take?"<br>
> "a few hours"<br>
> [More or Less] Less than a few hours.

"How Difficult is It?" returns a statement on how hard the task or feat is, along with a suggested modifier to the DC.

__Diagram Mapping__

"What Direction?" is used when mapping, to determine what direction an exit is located in.

"What is the Room Like?" can be used while mapping or any time a room description is needed. It should be interpreted in context of the adventure.

> [Room] gleaming, wood [Purpose] bodily functions [Size] expansive [Shape] square

*If my hero is storming a castle, it's a lavish spa-room, all gleaming wood and white tile. If he's exploring a ruin, it's a latrine for ogres, open above to the gleaming stars and night sky.*

"What is the Passage Like?" is rolled when you leave a room headed elsewhere.

> [Passage] slopes up or passes stairs [Special] a exit or arch or gap in the wall

*Heading deeper into the ruin, Reil quickly realizes the passage is sloping upwards. A gap in one crumbling wall leads into darkness.*

"How Far Is It" is used when you need to know how close something is. Need to know the range to the high priest's altar? Use "same room". Know the item is located somewhere in the ruin complex but not exactly where? "Same area". Know it's in the same kingdom or forest? "Same region." Have no idea where it is? "Anywhere."

__Grid Mapping__

The grid map options are used in conjunction with the grid map panel or with a piece of graph paper or a similar program. Each button returns a set of coordinates you can click or fill in to make a room or passage. Obviously, sanity checks are needed; if something doesn't make sense, connect it differently or skip it.

"Get Grid Room Pattern" returns a room-shaped set of coordinates. Pick a square on the map (likely an exit from another room or corridor or center-bottom if it's a new map) and count it as "1"; the rest of the room coordinates are in relation to this.

> [Grid Room] <br>
> 1: 1 to 5 <br>
> 2: 1 to 5 <br>
> 3: 1 to 5 <br>
> 4: 1 to 5 <br>

> \* * * * * * *  <br>
> \* X X X X X *  <br>
> \* X X X X X *  <br>
> \* X X X X X *  <br>
> \* X X X X X *  <br>
> \* * * * * * * <br>

*You would, starting from your "1", fill in 1 to 5, then move down a row and repeat until you have four filled rows.*

If a result has two or more numbers separated by commas, you should just fill in those squares.

> [Grid Room] <br>
> 1: 1 to 8 <br>
> 2: 1, 2, 5, 6 <br>
> 3: 1, 2, 5, 6 <br>

> \* * * * * * * * * *  <br>
> \* X X X X X X X X *  <br>
> \* X X * * X X * * *  <br>
> \* X X * * X X * * *  <br>
> \* * * * * * * * * *  <br>

"Get Grid Corridor Pattern" returns a corridor. Use "Get Grid Exits" to determine how many exits and which direction they are first.

> [Corridor] 1 by 3, 1 by 8 intersection at 2

*This is a t-shaped intersection, one square wide by three squares long, and right in the center it's bisected by a perpendicular hallway eight squares long and one square wide.*

####Map Stack

Both map panels share the same buttons.

"New Map" makes a new map.

"Full Map" shows the current map and saves a screenshot of it.

"Show Minimap" shows a small minimap version of the current map.

The spinner shows all available maps to load; choosing one loads that map.

The compass rose moves the viewport around the map, or you can scroll if your mouse supports it.

The first thing you should do when making a new map is to enter a title in the top input and hit "Save".

Finally, there are a number of tools on the World Panel in the Generators Stack for generating content for the different maps.

####Grid Map

This is exactly like a sheet of graph paper. Click once to change the background color, click again to return it to base. You can enter a single digit or letter into any square.

####Diagram Map

The black squares are "rooms" or "blocks" and can be labeled, and the areas between can be clicked to set links between two blocks or rooms. Click repeatedly to cycle through the various types of connections.

####Images

To use this panel, you need a subdirectory in your save folder named 'images' and a blank text file named 'imgs.txt' in your save directory. Any images in the images folder will be displayed in the images panel, along with simple fields to label or store notes about each picture.

Note that the images directory and file are not created by default with a new game!
