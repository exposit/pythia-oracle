# -*- coding: utf-8 -*-
##-------------------------------------------------------------------------------------------------------------------------------------------
# Actor Generator Panel
#
# A set of tools to generate inspiring, interpretive (but not too interpretive) NPCs.
#
##-------------------------------------------------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    pass

def initPanel(self):

    self.actorsAItem = AccordionItem(title='Actors & Motives', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)
    actorsMainBox = BoxLayout(orientation='vertical')

    actorsMainBox.add_widget(Label(text="Appearance", size_hint=(1,1)))

    actorsAgeBox = BoxLayout(orientation="horizontal")

    button = Button(text="Age - Adult", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorAgeAdult"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsAgeBox.add_widget(button)

    button = Button(text="Age - Any", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorAgeAny"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsAgeBox.add_widget(button)

    actorsMainBox.add_widget(actorsAgeBox)

    button = Button(text="Gender", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorGender"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Appearance Modifier", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorAppearanceModifier"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Visible Quirk", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorVisibleQuirk"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Non-Visible Quirk", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "actorNonvisibleQuirk"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    actorsMainBox.add_widget(Label(text="Motivations", size_hint=(1,1)))

    button = Button(text="Wheel (General Outlook)", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.function = "wheelMotives"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=miscChartRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Immediate Goals", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getDualMotives)
    actorsMainBox.add_widget(button)

    button = Button(text="Relationship - Close", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = 0
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=relationshipRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Relationship - Group", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = 1
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=relationshipRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Relationship - General", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = 2
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=relationshipRoll)
    actorsMainBox.add_widget(button)

    button = Button(text="Actor's Next Move", size_hint=(1,1), background_normal='',
     background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getActorMove)
    actorsMainBox.add_widget(button)

    button = Button(text="One Line Motive", size_hint=(1,1), background_normal='',
     background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getWhyMotive)
    actorsMainBox.add_widget(button)

    button = Button(text="Get Character Trait", size_hint=(1,1), background_normal='',
     background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getCharacterTrait)
    actorsMainBox.add_widget(button)

    button = Button(text="Trait-Based Character Event", size_hint=(1,1), background_normal='',
     background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getTraitBasedCharacter)
    actorsMainBox.add_widget(button)

    button = Button(text="Defining Characteristic", size_hint=(1,1), background_normal='',
     background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getDefiningCharacteristic)
    actorsMainBox.add_widget(button)

    actorsMainBox.add_widget(Label(text="Emotional Reaction"))

    actorsReactionBox = BoxLayout(orientation='horizontal')

    button = Button(text="Positive", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = "positive"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=reactionRoll)
    actorsReactionBox.add_widget(button)

    button = Button(text="Negative", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral)
    button.value = "negative"
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=reactionRoll)
    actorsReactionBox.add_widget(button)

    actorsMainBox.add_widget(actorsReactionBox)

    self.actorsAItem.add_widget(actorsMainBox)

    return self.actorsAItem

#-------------------------------------------------------------------------------------------------------------------------------------------
# actors & actor button functions
#-------------------------------------------------------------------------------------------------------------------------------------------

def miscChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = eval(args[0].function)()
    updateCenterDisplay(self, result)

def reactionRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = emotionalReaction(args[0].value)
    updateCenterDisplay(self, result)

def relationshipRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    if len(self.textInput.text) > 0:
        try:
            item1, item2 = self.textInput.text.split(', ')
            if args[0].value == 0:
                result = actorRelationshipClose(item1, item2)
            if args[0].value == 1:
                result = actorRelationshipGroup(item1, item2)
            if args[0].value == 2:
                result = actorRelationshipGeneral(item1, item2)
            updateCenterDisplay(self, result)
        except:
            updateCenterDisplay(self, "Enter two values separated by a comma.")
    else:
        if args[0].value == 0:
            result = actorRelationshipClose()
        if args[0].value == 1:
            result = actorRelationshipGroup()
        if args[0].value == 2:
            result = actorRelationshipGeneral()
        updateCenterDisplay(self, result)

def getWhyMotive(*args):
    args[0].background_color = neutral
    self = args[0].self
    array = dualMotives()
    result = "[Motive] " + array[1] + " " + array[2]
    updateCenterDisplay(self, result)

def getDualMotives(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = dualMotives()[0]
    updateCenterDisplay(self, result)

# logic
def actorGender():

    genderAppearance = random.choice(["male", "female"])
    return "[Gender Appearance] " + genderAppearance

def actorAppearanceModifier():

    modifier = random.choice(["Something is mysterious.", "Something is amiss.", "Is younger than appears.", "Is older than appears.", "Is in disguise.", "Wealthier than appears.", "Poorer than appears.", "Is not what they seem.", "Is exactly what they seem.", "Is impersonating or mimicking someone else in some way.", "Is impersonating or mimicking someone else wholecloth.", "Is more in some way than they appear.", "Is less in some way than they appear."])

    return "[Reality] " + modifier

def actorAgeAdult():

    chart = {
        2 : "Mid to late teens.",
        3 : "Nineteen or twenty.",
        4 : "Early twenties.",
        5 : "Mid-twenties.",
        6 : "Late twenties.",
        7 : "Thirties.",
        8 : "Forties.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Age - Mature] " + chart[roll]

    return result

def actorAgeAny():

    chart = {
        2 : "Child.",
        3 : "Teen.",
        4 : "Young Adult.",
        5 : "Mature.",
        6 : "Middle-Aged.",
        7 : "Old.",
        8 : "Venerable.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Age - Any] " + chart[roll]
    return result

def actorVisibleQuirk():

    chart = [
    "gap in front teeth", "unusual eye color", "unusual hair color", "very tall", "very short", "plump", "thin", "extremely average; they must work at it", "limping", "distinctive facial feature", "many hair braids", "very pale","smells of alcohol or drugs", "smells clean", "smells strongly", "black eye", "light freckles", "heavy freckles", "clumsy", "looks tired", "mole", "clothes don't fit well", "clothes very tailored", "graceful", "intense eyes", "distant stare", "prominent birthmark", "prominent scar", "disfiguring scar", "faint scar", "tanned", "broken limb", "bite or claw mark scar", "paint or dye on hands", "flower or leaves in hair", "rubbing back of neck", "military bearing", "displays a totem", "has a pet", "sunburned", "paragon of their race", "exemplar of their race", "minor tattoo or mark", "many tattoos or marks", "untreated wound", "inappropriate attire", "beautiful", "plain", "ugly", "mark of special heritage", "unnaturally beautiful", "unnaturally ugly", "incredibly charismatic", "appealing", "disturbing demeanor", "repellent", "immobilizing or slowing injury", "minor birthmark", "mark of unnatural heritage", "mark of distasteful heritage", "stocky and/or wide", "tall and/or slender", "petite and/or curvy", "waifish", "lithe and/or muscular", "distinctive jewelry", "distinctive weapon", "distinctive clothes", "wearing an item of military gear", "looks tired", "carrying a wounded pet", "carrying a child", "carrying a wounded person", "carrying too little gear to be prepared for surroundings", "chewing on something", "barely remaining standing", "falls unconscious", "typical hair color for a group", "typical eye color for a group", "tall for gender", "short for gender", "robust for gender", "undersized for gender", "well-endowed in some fashion", "very long hair", "very short hair", "definite case of bed-head", "sweating heavily", "cool and collected", "shrewd or piercing gaze", "constantly assessing", "completely covered in tattoos or marks", "carrying a dangerous animal", "has sharpened teeth", "mutation or power", "royal bearing", "haughty or arrogant bearing", "delicate hands", "looking down", "scanning the area", "mark of exotic heritage", "heritage is hard to determine", "lingering injury or infirmity"
    ]

    return "[Visible Quirk] " + random.choice(chart)

def actorNonvisibleQuirk():

    chart = [
    "fond of rhetorical questions", "incorrigible gossip", "keeps secrets", "cusses like a sailor", "really bad cook", "really good cook", "taciturn", "gestures while talking", "physically very friendly", "stutters", "falls in love easily", "accent", "very perceptive", "very unperceptive", "chip on shoulder", "placid temperament", "volatile temperament", "paranoid", "explosive temper", "hard to rouse to anger", "holds grudges", "lets bygones be bygones", "superstitious", "conceited", "nods frequently", "has a pet", "carries a totem", "pouty", "vicious when crossed", "mixes up two languages in speech", "has a soft spot for children", "has a soft spot for orphans", "can't stand small children", "hates a common pet type", "loves a common pet type", "stuck up", "down to earth", "wistful for the past", "apprehensive about the future", "afraid of change", "loves variety", "pessimist", "optimist", "pauses frequently when speaking", "dry sense of humor", "slapstick sense of humor", "openly prejudiced", "rigorously prepared in area of expertise", "a very good friend", "values loyalty above all else", "values honor above all else", "values family above all else", "values self above all else", "emotionally damaged", "emotionally centered", "feels at peace", "feels guilty", "bad at small talk", "bad at flirtation", "bad at negotiation", "nervous when around object of attraction", "easily embarrassed", "has no shame", "easily distracted", "single-minded", "cannot read or write", "unfailingly polite", "extremely rude", "has a phobia", "very sophisticated", "jaded and cynical", "bad temper", "tends to negativity", "mutation or odd power", "prefers to wing it", "wasn't taught better", "was taught better but doesn't care", "rejects social mores", "ignores social mores", "upholds social mores", "dwells on past event", "is steered by past event", "never looks back", "fastidious", "a taker from or user of people", "very self-sacrificing", "very selfish", "bossy", "high maintenance", "low maintenance", "skittish and conflict averse", "not easily frightened", "skittish and prone to flee conflict", "arrogant", "supremely self-confident", "lacks self-confidence", "feels a particular skill or task is beyond them", "lecherous despite risks", "lecherous but discreet", "lecherous and proud of it", "discreetly chaste", "overtly prudish", "overtly chaste", "private with personal affairs", "boastful", "embodies a virtue", "embodies a vice", "embodies many virtues", "embodies many vices", "embodies a virtue and a vice", "has a particular type of person they feel it's dishonorable to strike at", "will fight anybody, any time", "boisterous",
    ]

    return "[Non-Visible Quirk] " + random.choice(chart)

def actorRelationshipClose(npc1="The first actor", npc2="the second actor"):

    closeChart = [
       "opposes every goal of", "is married/devoted to", "is close blood kin of", "is distand blood kin of",
       "hates but can't escape from", "is in love with", "is trying to ruin", "was childhood friends with",
       "grew up with", "was childhood rivals with", "came to blows with", "respects the opinion of", "disregards the value of", "finds everything objectionable about", "finds everything admirable about", "seeks out the advice of",
    ]

    overtly = random.choice(["overtly", "covertly"])
    actively = random.choice(["actively", "passively"])

    result = npc1 + " " + random.choice(closeChart) + " " + npc2 + " and expresses it " + overtly + " and " + actively + "."
    return result

def actorRelationshipGroup(npc1="The first actor", group1="the target group"):

    groupChart = [
       "is a member in good standing of", "is an escapee from", "is a lapsed member of", "is an ardent supporter of", "is a fanatic of", "seeks to undermine", "seeks to join", "seeks to disband",
       "wants to avoid contact with", "wants to be left alone by", "wants the counsel of", "is hunted by",
       "pays lip service to", "tithes regularly to", "is oppressed by", "was liberated by"
    ]

    overtly = random.choice(["overtly", "covertly"])
    actively = random.choice(["actively", "passively"])

    result = npc1 + " " + random.choice(groupChart) + " " + group1 + " and expresses it " + overtly + " and " + actively + "."
    return result

def actorRelationshipGeneral(npc1="The actor", object="the target"):

    generalChart =[
    "hates and fears", "is enraged by", "is happy with", "is thrilled by", "wants to avoid", "prefers to deal with", "wants to destroy", "wants to preserve", "wants to fight", "wants to make peace with", "wants to use", "wants to prevent others from using"
    ]

    result = npc1 + " " + random.choice(generalChart) + " " + object + "."
    return result

# various motive charts based on emotions
targetChart = [
    "chaos", "order", "right", "wrong", "skill", "secrets", "status", "power", "food", "freedom", "sex", "love", "nearby person", "far away person", "death", "alcohol", "danger", "honor", "pain", "ghosts", "the divine", "wealth", "physical struggle", "emotional struggle", "adventure", "the physical", "tax", "the intellectual", "the emotional", "change", "status quo", "duty", "family", "survival", "job", "hate", "illness", "lies", "mildy unsuitable target", "inappropriate target", "wildly inappropriate target", "death", "violence", "wealth",
]

degreesChart = [
    ["traces", "overwhelming"],
    ["slight", "great"],
    ["just a little", "quite a bit"],
    ["weak", "strong"],
    ["mild", "driving"],
    ["strong", "strong"],
    ["twinge", "driving"],
    ["mere whim", "powerful"],
    ["flirting with", "demanding"],
    ["ignorable", "nearly consuming"],
]

oddsChart = [
    ["1/8", "7/8"],
    ["1/4", "3/4"],
    ["1/3", "2/3"],
    ["1/2", "1/2"],
    ["2/3", "1/3"],
    ["3/4", "1/4"],
    ["7/8", "1/8"],
]

def getDegrees():
    degrees = degreesChart[random.randint(0,len(degreesChart)-1)]
    flip = random.choice(['same', 'flipped'])
    if flip == 'same':
        return degrees[0], degrees[1]
    else:
        return degrees[1], degrees[0]

def wheelMotives():

    emotionChart = ["interest", "curiosity", "attraction", "desire", "admiration", "surprise", "amusement", "alarm", "panic", "aversion", "disgust", "revulsion", "indifference", "familiarity", "comfort", "hope", "fear", "gratitude", "thankfulness", "joy", "elation", "triumph", "jubilation", "patience", "anger", "rage", "sorrow", "grief", "frustration", "disappointment", "humility", "pride", "charity", "sympathy", "avarice", "greed", "miserliness", "envy", "jealousy", "love", "hate", "optimistic", "serene", "joyful", "ecstatic", "loving", "accepting", "trusting", "admiring", "submissive", "apprehensive", "fearful", "terrified", "awe-filled", "distracted", "surprised", "amazed", "disapproving", "pensive", "sad", "grieving", "remorseful", "bored", "disgusted", "loathing", "contemptuous", "annoyed", "angry", "furious", "aggressive", "interested", "anticipating", "vigilant", "addicted", "apathetic", "lethargic", "lustful", "vengeful", "obsessed", "spiteful", "hateful", "jealous", "scheming", "forthright", "fatalistic", "generous", "creative", "proud", "craving", "desiring", "bitter", "driven", "ambition", "concerned", "greedy", "enthusiastic", "consumed by", "protective", "numb"]

    degree, oppdegree = getDegrees()
    degree1, oppdegree1 = getDegrees()

    emotionList = random.sample(emotionChart, 4)
    item1 = emotionList[0]
    item2 = emotionList[1]
    item3 = emotionList[2]
    item4 = emotionList[3]

    emotionPatterns = {
    1 : "[" + degree.capitalize() + "] " + item1 + ", [" + oppdegree + "] " + item2,
    2 : "[" + degree.capitalize() + "] " + item1 + ", [" + degree1 + "] " + item2,
    3 : "[" + degree.capitalize() + "] " + item1 + ", [" + degree1 + "] " + item2 + ", [" + oppdegree + "] " + item3,
    4 : "[" + degree.capitalize() + "] " + item1,
    }

    roll = random.randint(1,2)
    targetList = random.sample(targetChart, roll)

    priorityList = random.sample(["primary", "secondary"], 2)

    if roll == 2:
        target = targetList[0] + " [" + priorityList[0] + "], " +  targetList[1] + " [" + priorityList[1] + "]"
    else:
        target = targetList[0]

    result = emotionPatterns[random.randint(1,4)] + "\n[Focus] " + target

    result = "[Wheel]\n" + result
    return result

# inspired by http://goblinpunch.blogspot.com/2014/11/what-mermaids-want.html
def dualMotives():

    goalChart = [
        "to consume out of necessity", "to trade gossip", "to protect home", "to make a new friend",
        "to serve a master", "to preserve beauty", "to pass on a curse out of spite",
        "to maintain silence", "to consume endlessly", "to seduce to ruin", "to procreate",
        "to lure into a trap", "to make a living", "to find meaning in life",
        "to placate an object of worship", "to sacrifice suitable targets", "to stop the invaders",
        "to preserve life", "to hoard shiny things", "to pass on a curse and thus be rid of it",
        "to protect offspring", "to deceive for personal gain", "to deceive for the greater good",
        "to stop a greater evil", "to gain an edge over", "to avoid passing on a curse",
        "to watch over a ward", "to learn about the world", "to explore new places", "to fall in love",
        "to conquer", "to ensnare", "to see the world burn", "to find excitement", "to stir up mischief",
        "to gain resources for the tribe", "to get revenge for a petty slight",
        "to get revenge for a serious matter", "to test someone's mettle", "to test the limits of skill",
        "to create something of lasting value", "to perfect a physical being",
        "to secure their safety", "to experience the thrill of the forbidden", "to seduce for pleasure", "to seduce for nefarious purposes", "to be entertained", "to be flattered and praised",
        "to seduce to a cause or mission or betrayal", "to seduce away from a cause or mission",
        "to seduce out of duty", "to increase food stores against hardship", "to increase weapons",
        "to find a companion", "to find a cause", "to be the best at something",
        "to gain ridiculous levels of wealth", "to obtain someone else's loved one",
        "to love 'em and leave 'em", "to cuckold or embarrass a rival", "to be a hero",
        "to scout out opportunities", "to find the truth", "to find true love",
        "to destroy out of necessity", "to bully the weak", "to live like a tyrant",
        "to live like a king", "to taste a delicacy", "to perform a great deed",
        "to perform a masterwork", "to escape a prison", "to imprison someone",
        "to enjoy solitude", "to avoid others", "to learn how to socialize", "to learn a secret",
        "to perform an appointed duty", "to subvert an appointed duty", "to shirk a duty",
        "to feel alive", "to ruin someone more powerful", "to murder",
        "to steal from by stealth or trickery", "to take from by force or guile", "to discredit",
        "to break free from", "to destroy out of malice", "to overthrow a ruler",
        "to repair a great wrong", "to make things right", "to create something creative",
        "to rebuild that which is destroyed", "to mend that which is broken", "to have a polite chat",
        "to learn news of the outside world", "to acquire something simply to have it",
        "to have an intelligent conversation", "to earn freedom", "to enslave as labor or cannon fodder",
        "to get to the other side", "to acquire magic for magic's sake", "to solve a puzzle or anomaly",
        "to experience other ways of life", "to entice to a dangerous task",
        "to embark on a perilous journey", "to get someone else to assume the risk",
        "to encourage bravery", "to encourage cowardice", "to encourage love", "to encourage lust",
        "to scare off interlopers", "to acquire knowledge for knowledge's sake",
        "to trap interlopers to meet basic needs", "to trade for treasure", "to trade for exotic wares",
        "to sell fruits of someone else's labors", "to help someone else"
        "to sell someone else", "to buy someone else", "to prove worthy of an honor", "to find a way in",
        "to find a way out", "to achieve success", "to atone for a sin of omission",
        "to achieve power peacefully and rightfully", "to achieve power through force and guile",
        "to atone for a transgression", "to locate the missing", "to buy just a little more time",
        "to indulge an addiction or craving", "to transmit a disease, contagion, or state of being",
        "to achieve status", "to retrieve a mark of status", "to express the pinnacle of an art",
        "to improve beauty", "to capture beauty", "to find literal immortality",
        "to find figurative immortality", "to be youthful", "to be wise",
        "to create more", "to destroy someone's creations", "to undo a terrible mistake",
        "to find a great treasure", "to prove the ends justify the means",
        "to have a civilized conversation", "to be tutored in the ways of another culture",
        "to bestow a boon", "to bestow a curse", "to be followed somewhere", "to spite someone",
        "to be free of a curse",

    ]

    goals = random.sample(goalChart, 2)

    focusChart = {
        2 : "everyone",
        3 : "race",
        4 : "kin",
        5 : "enemy",
        6 : "myself",
        7 : "hero",
        8 : "ally",
        9 : "enemy",
        10 : "kin",
        11 : "heritage",
        12 : "anyone",
    }

    modifierChart = [
        "hero's",
        "my",
        "nearby",
        "potential",
    ]

    roll1 = random.randint(1,6) + random.randint(1,6)
    roll2 = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])

    roll3 = random.randint(1,6) + random.randint(1,6)
    roll4 = random.choice([0, 0, 0, 0, 1, 1, 1, 2, 2, 3])

    focus = []
    focus1 = focusChart[roll1]
    focus2 = focusChart[roll3]

    if (roll1 > 2 and roll1 < 6) or (roll1 > 6 and roll1 < 12):
        focus1 = modifierChart[roll2] + " " + focus1
    if (roll3 > 2 and roll3 < 6) or (roll3 > 6 and roll3 < 12):
        focus2 = modifierChart[roll4] + " " + focus2

    degree, oppdegree = getDegrees()

    goal1 = "\n[" + degree.capitalize() + "] " + goals[0] + " [" + focus1 + "] "
    goal2 = "\n[" + oppdegree.capitalize() + "] " + goals[1] + " [" + focus2 + "] "

    return "[Goals]" + goal1 + goal2, goals[0], goals[1]

def emotionalReaction(reaction="positive"):

    negativeChart = [
    ["negative active", "anger", "annoyance", "contempt", "disgust", "irritation"],
    ["negative out of control", "anxiety", "embarrassment", "fear", "helplessness", "powerlessness", "worry"],
    ["negative", "pride", "doubt", "envy", "frustration", "guilt", "shame"],
    ["negative passive", "boredom", "despair", "disappointment", "hurt", "sadness"],
    ["agitation", "stress", "shock", "tension"],
    ]

    positiveChart = [
    ["positive active", "amusement", "delight", "elation", "excitement", "happiness", "joy", "pleasure"],
    ["positive caring", "affection", "empathy", "friendliness", "love"],
    ["positive", "courage", "hope", "humility", "satisfaction", "trust"],
    ["positive passive", "calmness", "contentment", "relaxation", "relief", "serenity"],
    ["reactive", "interest", "politeness", "surprise"],
    ]

    if reaction == "positive":
        chart = positiveChart
        oppchart = negativeChart
    else:
        chart = negativeChart
        oppchart = positiveChart

    degree, oppdegree = getDegrees()
    degree1, oppdegree1 = getDegrees()

    emotion1Chart = random.choice(chart)
    roll1 = random.randint(1, len(emotion1Chart)-1)
    emotion1 = emotion1Chart[roll1]

    emotion2Chart = random.choice(chart)
    roll2 = random.randint(1, len(emotion2Chart)-1)
    emotion2 = emotion2Chart[roll2]

    emotion3Chart = random.choice(oppchart)
    roll3 = random.randint(1, len(emotion3Chart)-1)
    emotion3 = emotion3Chart[roll3]

    emotion4Chart = random.choice(oppchart)
    roll4 = random.randint(1, len(emotion4Chart)-1)
    emotion4 = emotion4Chart[roll4]

    patterns = {
        1 : emotion1.capitalize() + " [" + degree + "]",
        2 : emotion1.capitalize() + " [" + degree + "] hidden by " + emotion3 + " [" + oppdegree + "]",
        3 : emotion1.capitalize() + " [" + degree + "], " + emotion2 + " [" + oppdegree + "]",
        4 : emotion1.capitalize() + " [" + degree + "], " + emotion2 + " [" + oppdegree + "] hidden behind " + emotion3 + " [" + degree1 + "], " + emotion4 + " [" + oppdegree1 + "]",
        5 : emotion1.capitalize() + " [" + degree + "], " + emotion2 + " [" + oppdegree + "] tinged with " + emotion3,
    }

    roll = random.randint(1,5)
    result = patterns[roll]
    return "[Reaction] " + result

# inspired by Apocalypse World & Simple World
def getActorMove(*args):
    self = args[0].self
    args[0].background_color = neutral

    chart = {
       2 : "Acts out of character in a negative way; a terrible secret revealed.",
       3 : "Draw a new Seed and interpret it negatively in context of the actor's potential actions.",
       4 : "Something from his backstory negatively influences his action.",
       5 : "Actor indulges or expresses a vice or ignoble facet of their character.",
       6 : "Actor takes the easiest possible option for them.",
       7 : "Actor acts in accordance with their current desire.",
       8 : "Actor uses an aspect they're comfortable with (maybe a skill, profession, tactic, or similar).",
       9 : "Actor indulges or expresses a noble facet of their character.",
      10 : "Something from his backstory positively influences his action.",
      11 : "Draw a new Seed and interpret it positively in context of the actor's potential actions.",
      12 : "Actor acts out of character in a positive way; a secret revealed.",
     }

    modchart = {
        2 : "True Face",
        3 : "Inept",
        4 : "Flashback",
        5 : "Ignoble",
        6 : "Weak",
        7 : "Focused",
        8 : "Skilled",
        9 : "Noble",
       10 : "Flashback",
       11 : "On Point",
       12 : "True Face",
     }

    roll = random.randint(1,6) + random.randint(1,6)

    result = chart[roll]

    result = "[" + modchart[roll] + "] " + result

    updateCenterDisplay(self, result, 'oracle')

# alternate method for generating NPCs
def getCharacterTrait(button, *args):

    button.background_color = neutral
    self = button.self

    full_trait = random.choice(adjectiveList) + " " + random.choice(traitList).lower()

    result = "[Trait] \"" + full_trait + "\""
    updateCenterDisplay(self, result)

def getTraitBasedCharacter(button, *args):

    button.background_color = neutral
    self = button.self

    full_traits = []

    how_recentlyList = ["was ongoing for years", "happened recently", "went on for months", "went on for weeks", "happened for a few days, a few years ago", "happened for a brief, intense period a few years ago", "was ongoing for years, but recently stopped", "occurred for a brief, intense period a a few years ago and recently resumed", "was a long term thing", "started in childhood", "happened once or twice a month but never more frequently"]

    how_affectedList = ["and it completely changed the actor's personality", "and it completely changed the actor physically", "and it completely changed the actor's outlook on life", "and it changed the actor's outlook on life in an important way", "and it changed the actor's outlook on life in a  minor way", "and it encouraged total abstention", "and it encouraged more of the same", "and it encouraged redoubled efforts", "apparently not at all", "mildly", "severely", ", and still is", "but shrugged it off"]

    consequencesList = ["were negligible", "were concrete, resulting in a worsening of situation", "were concrete, resulting in a bettering of situation", "were concrete", "left the actor trapped", "were concrete, giving more freedom", "seemed neglible but had a lasting effect", "seemed negigible but had a secret effect", "affected the world negatively", "affected the world positively", "affected the actor's social standing negatively", "affected the actor's social standing positively", "made the actor a pariah", "kept the actor from achieving something of importance", "hurt someone else very badly", "resulted in a death", "resulted in someone else's ruin", "resulted in the actor losing everything", "resulted in someone else losing everything", "resulted in the actor losing someone of value", "resulted in the actor losing some thing of value", "were expensive", "were relatively cheap", "were cheap to the actor and expensive for someone else", "were undiscovered"]

    immediate_situationList = ["are hidden and the actor intends to keep it that way", "are secretly working against him", "are overtly working against him", "are threatening to ruin the actor's current situation"]

    response_reactionA = [ "is still indulging, ignoring the consequences", "is refusing to indulge out of fear of the consequences", "wants to indulge but can't ", "wants to indulge but can't", "has changed for the better", "has gotten much worse", "is indulging at every opportunity", "is indulging only when he has to"]
    response_reactionB = ["pretends that part of him is set aside", "pretends that part of him never existed", "tries to hide it", "flaunts it", "avoids situations where it might reoccur or come up", "seeks out situations where it might reoccur or come up", "because of concrete reasons", "because of abstract reasons"]

    events = ["an opportunity", "a life Lesson", "a personal failure", "a personal victory"]

    event = "The event was " + random.choice(events) + "."

    how_recently = " It " + random.choice(how_recentlyList) + "."

    how_affected = " The actor was affected " + random.choice(how_affectedList) + "."

    consequences = " The immediate consequences " + random.choice(consequencesList) + "."

    immediate_situation = " Currently, the consequences " + random.choice(immediate_situationList) + "."

    responsePattern = random.randint(1,3)

    response_reaction = " The actor "

    if responsePattern == 1:
        response_reaction = response_reaction + random.choice(response_reactionA) + " and " + random.choice(response_reactionB)
    elif responsePattern == 2:
        response_reaction = response_reaction + random.choice(response_reactionA)
    else:
        response_reaction = response_reaction + random.choice(response_reactionB)

    result = event + how_recently + how_affected + consequences + immediate_situation + response_reaction + "."
    updateCenterDisplay(self, result)

def getDefiningCharacteristic(button, *args):
    button.background_color = neutral
    self = button.self

    important_characteristic = "[Defining Characteristic] The actor is " + random.choice(degreeList) +  " \"" + random.choice(adjectiveList + traitList).lower() + "\"" + "."
    updateCenterDisplay(self, important_characteristic)

degreeList = ["minor", "major", "extremely", "a little", "very", "somewhat", "slightly", "impaired", "enhanced", "incredibly", "ridiculously bad at", "downright terrible at", "amazing at"]

adjectiveList = ["abandoned", "able", "absolute", "adorable", "adventurous", "academic", "acceptable", "acclaimed", "accomplished", "accurate", "aching", "acidic", "acrobatic", "active", "actual", "adept", "admirable", "admired", "adolescent", "adorable", "adored", "advanced", "afraid", "affectionate", "aged", "aggravating", "aggressive", "agile", "agitated", "agonizing", "agreeable", "ajar", "alarmed", "alarming", "alert", "alienated", "alive", "all", "altruistic", "amazing", "ambitious", "ample", "amused", "amusing", "anchored", "ancient", "angelic", "angry", "anguished", "animated", "annual", "another", "antique", "anxious", "any", "apprehensive", "appropriate", "apt", "arctic", "arid", "aromatic", "artistic", "ashamed", "assured", "astonishing", "athletic", "attached", "attentive", "attractive", "austere", "authentic", "authorized", "automatic", "avaricious", "average", "aware", "awesome", "awful", "awkward", "babyish", "bad", "back", "baggy", "bare", "barren", "basic", "beautiful", "belated", "beloved", "beneficial", "better", "best", "bewitched", "big", "big-hearted", "biodegradable", "bite-sized", "bitter", "black", "black-and-white", "bland", "blank", "blaring", "bleak", "blind", "blissful", "blond", "blue", "blushing", "bogus", "boiling", "bold", "bony", "boring", "bossy", "both", "bouncy", "bountiful", "bowed", "brave", "breakable", "brief", "bright", "brilliant", "brisk", "broken", "bronze", "brown", "bruised", "bubbly", "bulky", "bumpy", "buoyant", "burdensome", "burly", "bustling", "busy", "buttery", "buzzing", "calculating", "calm", "candid", "canine", "capital", "carefree", "careful", "careless", "caring", "cautious", "cavernous", "celebrated", "charming", "cheap", "cheerful", "cheery", "chief", "chilly", "chubby", "circular", "classic", "clean", "clear", "clear-cut", "clever", "close", "closed", "cloudy", "clueless", "clumsy", "cluttered", "coarse", "cold", "colorful", "colorless", "colossal", "comfortable", "common", "compassionate", "competent", "complete", "complex", "complicated", "composed", "concerned", "concrete", "confused", "conscious", "considerate", "constant", "content", "conventional", "cooked", "cool", "cooperative", "coordinated", "corny", "corrupt", "costly", "courageous", "courteous", "crafty", "crazy", "creamy", "creative", "creepy", "criminal", "crisp", "critical", "crooked", "crowded", "cruel", "crushing", "cuddly", "cultivated", "cultured", "cumbersome", "curly", "curvy", "cute", "damaged", "damp", "dangerous", "dapper", "daring", "darling", "dark", "dazzling", "dead", "deadly", "deafening", "dear", "dearest", "decent", "decimal", "decisive", "deep", "defenseless", "defensive", "defiant", "deficient", "definite", "definitive", "delayed", "delectable", "delicious", "delightful", "delirious", "demanding", "dense", "dental", "dependable", "dependent", "descriptive", "deserted", "detailed", "determined", "devoted", "different", "difficult", "digital", "diligent", "dim", "dimpled", "dimwitted", "direct", "disastrous", "discrete", "disfigured", "disgusting", "disloyal", "dismal", "distant", "downright", "dreary", "dirty", "disguised", "dishonest", "dismal", "distant", "distinct", "distorted", "dizzy", "dopey", "doting", "double", "downright", "drab", "drafty", "dramatic", "dreary", "droopy", "dry", "dual", "dull", "dutiful", "eager", "earnest", "early", "easy", "easy-going", "ecstatic", "edible", "educated", "elaborate", "elastic", "elated", "elderly", "electric", "elegant", "elementary", "elliptical", "embarrassed", "embellished", "eminent", "emotional", "empty", "enchanted", "enchanting", "energetic", "enlightened", "enormous", "enraged", "entire", "envious", "equal", "equatorial", "essential", "esteemed", "ethical", "euphoric", "even", "evergreen", "everlasting", "every", "evil", "exalted", "excellent", "exemplary", "exhausted", "excitable", "excited", "exciting", "exotic", "expensive", "experienced", "expert", "extraneous", "extroverted", "extra-large", "extra-small", "fabulous", "failing", "faint", "fair", "faithful", "fake", "false", "familiar", "famous", "fancy", "fantastic", "far", "faraway", "far-flung", "far-off", "fast", "fat", "fatal", "fatherly", "favorable", "favorite", "fearful", "fearless", "feisty", "feline", "female", "feminine", "few", "fickle", "filthy", "fine", "finished", "firm", "first", "firsthand", "fitting", "fixed", "flaky", "flamboyant", "flashy", "flat", "flawed", "flawless", "flickering", "flimsy", "flippant", "flowery", "fluffy", "fluid", "flustered", "focused", "fond", "foolhardy", "foolish", "forceful", "forked", "formal", "forsaken", "forthright", "fortunate", "fragrant", "frail", "frank", "frayed", "free", "French", "fresh", "frequent", "friendly", "frightened", "frightening", "frigid", "frilly", "frizzy", "frivolous", "front", "frosty", "frozen", "frugal", "fruitful", "full", "fumbling", "functional", "funny", "fussy", "fuzzy", "gargantuan", "gaseous", "general", "generous", "gentle", "genuine", "giant", "giddy", "gigantic", "gifted", "giving", "glamorous", "glaring", "glass", "gleaming", "gleeful", "glistening", "glittering", "gloomy", "glorious", "glossy", "glum", "golden", "good", "good-natured", "gorgeous", "graceful", "gracious", "grand", "grandiose", "granular", "grateful", "grave", "gray", "great", "greedy", "green", "gregarious", "grim", "grimy", "gripping", "grizzled", "gross", "grotesque", "grouchy", "grounded", "growing", "growling", "grown", "grubby", "gruesome", "grumpy", "guilty", "gullible", "gummy", "hairy", "half", "handmade", "handsome", "handy", "happy", "happy-go-lucky", "hard", "hard-to-find", "harmful", "harmless", "harmonious", "harsh", "hasty", "hateful", "haunting", "healthy", "heartfelt", "hearty", "heavenly", "heavy", "hefty", "helpful", "helpless", "hidden", "hideous", "high", "high-level", "hilarious", "hoarse", "hollow", "homely", "honest", "honorable", "honored", "hopeful", "horrible", "hospitable", "hot", "huge", "humble", "humiliating", "humming", "humongous", "hungry", "hurtful", "husky", "icky", "icy", "ideal", "idealistic", "identical", "idle", "idiotic", "idolized", "ignorant", "ill", "illegal", "ill-fated", "ill-informed", "illiterate", "illustrious", "imaginary", "imaginative", "immaculate", "immaterial", "immediate", "immense", "impassioned", "impeccable", "impartial", "imperfect", "imperturbable", "impish", "impolite", "important", "impossible", "impractical", "impressionable", "impressive", "improbable", "impure", "inborn", "incomparable", "incompatible", "incomplete", "inconsequential", "incredible", "indelible", "inexperienced", "indolent", "infamous", "infantile", "infatuated", "inferior", "infinite", "informal", "innocent", "insecure", "insidious", "insignificant", "insistent", "instructive", "insubstantial", "intelligent", "intent", "intentional", "interesting", "internal", "international", "intrepid", "ironclad", "irresponsible", "irritating", "itchy", "jaded", "jagged", "jam-packed", "jaunty", "jealous", "jittery", "joint", "jolly", "jovial", "joyful", "joyous", "jubilant", "judicious", "juicy", "jumbo", "junior", "jumpy", "juvenile", "keen", "key", "kind", "kindhearted", "kindly", "klutzy", "knobby", "knotty", "knowledgeable", "knowing", "known", "kooky", "kosher", "lame", "lanky", "large", "last", "lasting", "late", "lavish", "lawful", "lazy", "leading", "lean", "leafy", "left", "legal", "legitimate", "light", "lighthearted", "likable", "likely", "limited", "limp", "limping", "linear", "lined", "liquid", "little", "live", "lively", "livid", "loathsome", "lone", "lonely", "long", "long-term", "loose", "lopsided", "lost", "loud", "lovable", "lovely", "loving", "low", "loyal", "lucky", "lumbering", "luminous", "lumpy", "lustrous", "luxurious", "mad", "made-up", "magnificent", "majestic", "major", "male", "mammoth", "married", "marvelous", "masculine", "massive", "mature", "meager", "mealy", "mean", "measly", "meaty", "medical", "mediocre", "medium", "meek", "mellow", "melodic", "memorable", "menacing", "merry", "messy", "metallic", "mild", "milky", "mindless", "miniature", "minor", "minty", "miserable", "miserly", "misguided", "misty", "mixed", "modern", "modest", "moist", "monstrous", "monthly", "monumental", "moral", "mortified", "motherly", "motionless", "mountainous", "muddy", "muffled", "multicolored", "mundane", "murky", "mushy", "musty", "muted", "mysterious", "naive", "narrow", "nasty", "natural", "naughty", "nautical", "near", "neat", "necessary", "needy", "negative", "neglected", "negligible", "neighboring", "nervous", "new", "next", "nice", "nifty", "nimble", "nippy", "nocturnal", "noisy", "nonstop", "normal", "notable", "noted", "noteworthy", "novel", "noxious", "numb", "nutritious", "nutty", "obedient", "obese", "oblong", "oily", "oblong", "obvious", "occasional", "odd", "oddball", "offbeat", "offensive", "official", "old", "old-fashioned", "only", "open", "optimal", "optimistic", "opulent", "orange", "orderly", "organic", "ornate", "ornery", "ordinary", "original", "other", "outlying", "outgoing", "outlandish", "outrageous", "outstanding", "oval", "overcooked", "overdue", "overjoyed", "overlooked", "palatable", "pale", "paltry", "parallel", "parched", "partial", "passionate", "past", "pastel", "peaceful", "peppery", "perfect", "perfumed", "periodic", "perky", "personal", "pertinent", "pesky", "pessimistic", "petty", "phony", "physical", "piercing", "pink", "pitiful", "plain", "plaintive", "plastic", "playful", "pleasant", "pleased", "pleasing", "plump", "plush", "polished", "polite", "political", "pointed", "pointless", "poised", "poor", "popular", "portly", "posh", "positive", "possible", "potable", "powerful", "powerless", "practical", "precious", "present", "prestigious", "pretty", "precious", "previous", "pricey", "prickly", "primary", "prime", "pristine", "private", "prize", "probable", "productive", "profitable", "profuse", "proper", "proud", "prudent", "punctual", "pungent", "puny", "pure", "purple", "pushy", "putrid", "puzzled", "puzzling", "quaint", "qualified", "quarrelsome", "quarterly", "queasy", "querulous", "questionable", "quick", "quick-witted", "quiet", "quintessential", "quirky", "quixotic", "quizzical", "radiant", "ragged", "rapid", "rare", "rash", "raw", "recent", "reckless", "rectangular", "ready", "real", "realistic", "reasonable", "red", "reflecting", "regal", "regular", "reliable", "relieved", "remarkable", "remorseful", "remote", "repentant", "required", "respectful", "responsible", "repulsive", "revolving", "rewarding", "rich", "rigid", "right", "ringed", "ripe", "roasted", "robust", "rosy", "rotating", "rotten", "rough", "round", "rowdy", "royal", "rubbery", "rundown", "ruddy", "rude", "runny", "rural", "rusty", "sad", "safe", "salty", "same", "sandy", "sane", "sarcastic", "sardonic", "satisfied", "scaly", "scarce", "scared", "scary", "scented", "scholarly", "scientific", "scornful", "scratchy", "scrawny", "second", "secondary", "second-hand", "secret", "self-assured", "self-reliant", "selfish", "sentimental", "separate", "serene", "serious", "serpentine", "several", "severe", "shabby", "shadowy", "shady", "shallow", "shameful", "shameless", "sharp", "shimmering", "shiny", "shocked", "shocking", "shoddy", "short", "short-term", "showy", "shrill", "shy", "sick", "silent", "silky", "silly", "silver", "similar", "simple", "simplistic", "sinful", "single", "sizzling", "skeletal", "skinny", "sleepy", "slight", "slim", "slimy", "slippery", "slow", "slushy", "small", "smart", "smoggy", "smooth", "smug", "snappy", "snarling", "sneaky", "sniveling", "snoopy", "sociable", "soft", "soggy", "solid", "somber", "some", "spherical", "sophisticated", "sore", "sorrowful", "soulful", "soupy", "sour", "sparkling", "sparse", "specific", "spectacular", "speedy", "spicy", "spiffy", "spirited", "spiteful", "splendid", "spotless", "spotted", "spry", "square", "squeaky", "squiggly", "stable", "staid", "stained", "stale", "standard", "starchy", "stark", "starry", "steep", "sticky", "stiff", "stimulating", "stingy", "stormy", "straight", "strange", "steel", "strict", "strident", "striking", "striped", "strong", "studious", "stunning", "stupendous", "stupid", "sturdy", "stylish", "subdued", "submissive", "substantial", "subtle", "suburban", "sudden", "sugary", "sunny", "super", "superb", "superficial", "superior", "supportive", "sure-footed", "surprised", "suspicious", "svelte", "sweaty", "sweet", "sweltering", "swift", "sympathetic", "tall", "talkative", "tame", "tan", "tangible", "tart", "tasty", "tattered", "taut", "tedious", "teeming", "tempting", "tender", "tense", "tepid", "terrible", "terrific", "testy", "thankful", "thick", "thin", "third", "thirsty", "thorough", "thorny", "those", "thoughtful", "threadbare", "thrifty", "thunderous", "tidy", "tight", "timely", "tinted", "tiny", "tired", "torn", "total", "tough", "traumatic", "treasured", "tremendous", "tragic", "trained", "tremendous", "triangular", "tricky", "trifling", "trim", "trivial", "troubled", "true", "trusting", "trustworthy", "trusty", "truthful", "tubby", "turbulent", "twin", "ugly", "ultimate", "unacceptable", "unaware", "uncomfortable", "uncommon", "unconscious", "understated", "unequaled", "uneven", "unfinished", "unfit", "unfolded", "unfortunate", "unhappy", "unhealthy", "uniform", "unimportant", "unique", "united", "unkempt", "unknown", "unlawful", "unlined", "unlucky", "unnatural", "unpleasant", "unrealistic", "unripe", "unruly", "unselfish", "unsightly", "unsteady", "unsung", "untidy", "untimely", "untried", "untrue", "unused", "unusual", "unwelcome", "unwieldy", "unwilling", "unwitting", "unwritten", "upbeat", "upright", "upset", "urban", "usable", "used", "useful", "useless", "utilized", "utter", "vacant", "vague", "vain", "valid", "valuable", "vapid", "variable", "vast", "velvety", "venerated", "vengeful", "verifiable", "vibrant", "vicious", "victorious", "vigilant", "vigorous", "villainous", "violet", "violent", "virtual", "virtuous", "visible", "vital", "vivacious", "vivid", "voluminous", "wan", "warlike", "warm", "warmhearted", "warped", "wary", "wasteful", "watchful", "waterlogged", "watery", "wavy", "wealthy", "weak", "weary", "webbed", "wee", "weekly", "weepy", "weighty", "weird", "welcome", "well-documented", "well-groomed", "well-informed", "well-lit", "well-made", "well-off", "well-to-do", "well-worn", "wet", "which", "whimsical", "whirlwind", "whispered", "white", "whole", "whopping", "wicked", "wide", "wide-eyed", "wiggly", "wild", "willing", "wilted", "winding", "windy", "winged", "wiry", "wise", "witty", "wobbly", "woeful", "wonderful", "wooden", "woozy", "wordy", "worldly", "worn", "worried", "worrisome", "worse", "worst", "worthless", "worthwhile", "worthy", "wrathful", "wretched", "writhing", "wrong", "wry", "yawning", "yearly", "yellow", "yellowish", "young", "youthful", "yummy", "zany", "zealous", "zesty", "zigzag"
]

traitList = ["Accessible", "Active", "Adaptable", "Admirable", "Adventurous", "Agreeable", "Alert", "Allocentric", "Amiable", "Anticipative", "Appreciative", "Articulate", "Aspiring", "Athletic", "Attractive", "Balanced", "Benevolent", "Brilliant", "Calm", "Capable", "Captivating", "Caring", "Challenging", "Charismatic", "Charming", "Cheerful", "Clean", "Clear-headed", "Clever", "Colorful", "Companionable", "Compassionate", "Conciliatory", "Confident", "Conscientious", "Considerate", "Constant", "Contemplative", "Cooperative", "Courageous", "Courteous", "Creative", "Cultured", "Curious", "Daring", "Debonair", "Decent", "Decisive", "Dedicated", "Deep", "Dignified", "Directed", "Disciplined", "Discreet", "Dramatic", "Dutiful", "Dynamic", "Earnest", "Ebullient", "Educated", "Efficient", "Elegant", "Eloquent", "Empathetic", "Energetic", "Enthusiastic", "Esthetic", "Exciting", "Extraordinary", "Fair", "Faithful", "Farsighted", "Felicific", "Firm", "Flexible", "Focused", "Forceful", "Forgiving", "Forthright", "Freethinking", "Friendly", "Fun-loving", "Gallant", "Generous", "Gentle", "Genuine", "Good-natured", "Gracious", "Hardworking", "Healthy", "Hearty", "Helpful", "Heroic", "High-minded", "Honest", "Honorable", "Humble", "Humorous", "Idealistic", "Imaginative", "Impressive", "Incisive", "Incorruptible", "Independent", "Individualistic", "Innovative", "Inoffensive", "Insightful", "Insouciant", "Intelligent", "Intuitive", "Invulnerable", "Kind", "Knowledge", "Leader", "Leisurely", "Liberal", "Logical", "Lovable", "Loyal", "Lyrical", "Magnanimous", "Many-sided", "Masculine", "Mature", "Methodical", "Meticulous", "Moderate", "Modest", "Multi-leveled", "Neat", "Non-authoritarian", "Objective", "Observant", "Open", "Optimistic", "Orderly", "Organized", "Original", "Painstaking", "Passionate", "Patient", "Patriotic", "Peaceful", "Perceptive", "Perfectionist", "Personable", "Persuasive", "Prepared", "Playful", "Polished", "Popular", "Practical", "Precise", "Principled", "Profound", "Protean", "Protective", "Providential", "Prudent", "Punctual", "Purposeful", "Rational", "Realistic", "Reflective", "Relaxed", "Reliable", "Resourceful", "Respectful", "Responsible", "Responsive", "Reverential", "Romantic", "Rustic", "Sage", "Sane", "Scholarly", "Scrupulous", "Secure", "Selfless", "Self-critical", "Self-defacing", "Self-denying", "Self-reliant", "Self-sufficient", "Sensitive", "Sentimental", "Seraphic", "Serious", "Sexy", "Sharing", "Shrewd", "Simple", "Skillful", "Sober", "Sociable", "Solid", "Sophisticated", "Spontaneous", "Sporting", "Stable", "Steadfast", "Steady", "Stoic", "Strong", "Studious", "Suave", "Subtle", "Sweet", "Sympathetic", "Systematic", "Tasteful", "Teacherly", "Thorough", "Tidy", "Tolerant", "Tractable", "Trusting", "Uncomplaining", "Understanding", "Undogmatic", "Unfoolable", "Upright", "Urbane", "Venturesome", "Vivacious", "Warm", "Well-bred", "Well-read", "Well-rounded", "Winning", "Wise", "Witty", "Youthful", "", "Absentminded", "Aggressive", "Ambitious", "Amusing", "Artful", "Ascetic", "Authoritarian", "Big-thinking", "Boyish", "Breezy", "Businesslike", "Busy", "Casual", "Cerebral", "Chummy", "Circumspect", "Competitive", "Complex", "Confidential", "Conservative", "Contradictory", "Crisp", "Cute", "Deceptive", "Determined", "Dominating", "Dreamy", "Driving", "Droll", "Dry", "Earthy", "Effeminate", "Emotional", "Enigmatic", "Experimental", "Familial", "Folksy", "Formal", "Freewheeling", "Frugal", "Glamorous", "Guileless", "High-spirited", "Hurried", "Hypnotic", "Iconoclastic", "Idiosyncratic", "Impassive", "Impersonal", "Impressionable", "Intense", "Invisible", "Irreligious", "Irreverent", "Maternal", "Mellow", "Modern", "Moralistic", "Mystical", "Neutral", "Noncommittal", "Noncompetitive", "Obedient", "Old-fashioned", "Ordinary", "Outspoken", "Paternalistic", "Physical", "Placid", "Political", "Predictable", "Preoccupied", "Private", "Progressive", "Proud", "Pure", "Questioning", "Quiet", "Religious", "Reserved", "Restrained", "Retiring", "Sarcastic", "Self-conscious", "Sensual", "Skeptical", "Smooth", "Soft", "Solemn", "Solitary", "Stern", "Stolid", "Strict", "Stubborn", "Stylish", "Subjective", "Surprising", "Soft", "Tough", "Unaggressive", "Unambitious", "Unceremonious", "Unchanging", "Undemanding", "Unfathomable", "Unhurried", "Uninhibited", "Unpatriotic", "Unpredictable", "Unreligious", "Unsentimental", "Whimsical", "", "Abrasive", "Abrupt", "Agonizing", "Aimless", "Airy", "Aloof", "Amoral", "Angry", "Anxious", "Apathetic", "Arbitrary", "Argumentative", "Arrogant", "Artificial", "Asocial", "Assertive", "Astigmatic", "Barbaric", "Bewildered", "Bizarre", "Bland", "Blunt", "Boisterous", "Brittle", "Brutal", "Calculating", "Callous", "Cantankerous", "Careless", "Cautious", "Charmless", "Childish", "Clumsy", "Coarse", "Cold", "Colorless", "Complacent", "Complaintive", "Compulsive", "Conceited", "Condemnatory", "Conformist", "Confused", "Contemptible", "Conventional", "Cowardly", "Crafty", "Crass", "Crazy", "Criminal", "Critical", "Crude", "Cruel", "Cynical", "Decadent", "Deceitful", "Delicate", "Demanding", "Dependent", "Desperate", "Destructive", "Devious", "Difficult", "Dirty", "Disconcerting", "Discontented", "Discouraging", "Discourteous", "Dishonest", "Disloyal", "Disobedient", "Disorderly", "Disorganized", "Disputatious", "Disrespectful", "Disruptive", "Dissolute", "Dissonant", "Distractible", "Disturbing", "Dogmatic", "Domineering", "Dull", "Easily Discouraged", "Egocentric", "Enervated", "Envious", "Erratic", "Escapist", "Excitable", "Expedient", "Extravagant", "Extreme", "Faithless", "False", "Fanatical", "Fanciful", "Fatalistic", "Fawning", "Fearful", "Fickle", "Fiery", "Fixed", "Flamboyant", "Foolish", "Forgetful", "Fraudulent", "Frightening", "Frivolous", "Gloomy", "Graceless", "Grand", "Greedy", "Grim", "Gullible", "Hateful", "Haughty", "Hedonistic", "Hesitant", "Hidebound", "High-handed", "Hostile", "Ignorant", "Imitative", "Impatient", "Impractical", "Imprudent", "Impulsive", "Inconsiderate", "Incurious", "Indecisive", "Indulgent", "Inert", "Inhibited", "Insecure", "Insensitive", "Insincere", "Insulting", "Intolerant", "Irascible", "Irrational", "Irresponsible", "Irritable", "Lazy", "Libidinous", "Loquacious", "Malicious", "Mannered", "Mannerless", "Mawkish", "Mealymouthed", "Mechanical", "Meddlesome", "Melancholic", "Meretricious", "Messy", "Miserable", "Miserly", "Misguided", "Mistaken", "Money-minded", "Monstrous", "Moody", "Morbid", "Muddle-headed", "Naive", "Narcissistic", "Narrow", "Narrow-minded", "Natty", "Negativistic", "Neglectful", "Neurotic", "Nihilistic", "Obnoxious", "Obsessive", "Obvious", "Odd", "Offhand", "One-dimensional", "One-sided", "Opinionated", "Opportunistic", "Oppressed", "Outrageous", "Over-imaginative", "Paranoid", "Passive", "Pedantic", "Perverse", "Petty", "Pharisaical", "Phlegmatic", "Plodding", "Pompous", "Possessive", "Power-hungry", "Predatory", "Prejudiced", "Presumptuous", "Pretentious", "Prim", "Procrastinating", "Profligate", "Provocative", "Pugnacious", "Puritanical", "Quirky", "Reactionary", "Reactive", "Regimental", "Regretful", "Repentant", "Repressed", "Resentful", "Ridiculous", "Rigid", "Ritualistic", "Rowdy", "Ruined", "Sadistic", "Sanctimonious", "Scheming", "Scornful", "Secretive", "Sedentary", "Selfish", "Self-indulgent", "Shallow", "Shortsighted", "Shy", "Silly", "Single-minded", "Sloppy", "Slow", "Sly", "Small-thinking", "Softheaded", "Sordid", "Steely", "Stiff", "Strong-willed", "Stupid", "Submissive", "Superficial", "Superstitious", "Suspicious", "Tactless", "Tasteless", "Tense", "Thievish", "Thoughtless", "Timid", "Transparent", "Treacherous", "Trendy", "Troublesome", "Unappreciative", "Uncaring", "Uncharitable", "Unconvincing", "Uncooperative", "Uncreative", "Uncritical", "Unctuous", "Undisciplined", "Unfriendly", "Ungrateful", "Unhealthy", "Unimaginative", "Unimpressive", "Unlovable", "Unpolished", "Unprincipled", "Unrealistic", "Unreflective", "Unreliable", "Unrestrained", "Unself-critical", "Unstable", "Vacuous", "Vague", "Venal", "Venomous", "Vindictive", "Vulnerable", "Weak", "Weak-willed", "Well-meaning", "Willful", "Wishful", "Zany", "Egocentric"]
