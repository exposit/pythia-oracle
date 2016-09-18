# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
# PC Emulator Panel
#
##---------------------------------------------------------------------------------------------------
import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    l = ToggleButtonBehavior.get_widgets('default_seed')
    for checkbox in l:
        if config.general['seed_func'] == checkbox.func and config.general['seed_type'] == checkbox.type:
            checkbox.active = True
    del l
    pass

def initPanel(self):

    self.seedsAItem = AccordionItem(title='Seeds & Complex Answers', background_selected= os.sep + 'resources' + os.sep + "ui_images" + os.sep + 'invisible.png', min_space=config.aiheight)

    self.seedsMainBox = BoxLayout(orientation='vertical')

    self.seedsMainBox.add_widget(Label(text="Mythic Style", size_hint=(1,.1)))

    self.seedsTwoPartGrid = GridLayout(cols=2)

    for seedpack in seedArray:

        # checkbox for making default
        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useTwoPartSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsTwoPartGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.90,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useTwoPartSeed)
        self.seedsTwoPartGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsTwoPartGrid)

    self.seedsMainBox.add_widget(Label(text="Location Crafter Style", size_hint=(1,.1)))

    self.seedsTitleGrid = GridLayout(cols=2, size_hint=(1,.10))
    self.seedsTitleGrid.add_widget(Label(text="Description"))
    self.seedsTitleGrid.add_widget(Label(text="Action"))
    self.seedsMainBox.add_widget(self.seedsTitleGrid)

    self.seedsThreePartGrid = GridLayout(cols=3)

    for seedpack in seedArray:

        # checkbox for defaults
        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useThreePartSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsThreePartGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.45,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.subtype = "adjective"
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useThreePartSeed)
        self.seedsThreePartGrid.add_widget(button)

        button = Button(text=seedpack, size_hint=(.45,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans', font_size=config.basefont90)
        button.self = self
        button.subtype = "verb"
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useThreePartSeed)
        self.seedsThreePartGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsThreePartGrid)

    self.seedsMainBox.add_widget(Label(text="One Big List", size_hint=(1,.1)))

    self.seedsAllGrid = GridLayout(cols=2)

    for seedpack in seedArray:

        checkbox = CheckBox(size_hint_y=None, size_hint=(.10,.20), height=config.baseheight, group='default_seed')
        checkbox.self = self
        checkbox.func = 'useAllSeed'
        checkbox.type = seedpack
        checkbox.bind(active=setDefaultSeed)
        self.seedsAllGrid.add_widget(checkbox)

        button = Button(text=seedpack, size_hint=(.90,.20), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=useAllSeed)
        self.seedsAllGrid.add_widget(button)

    self.seedsMainBox.add_widget(self.seedsAllGrid)

    self.seedsAItem.add_widget(self.seedsMainBox)

    return self.seedsAItem

def getTwo(typeA, typeB):

    item = config.general['seed_type']
    actionList = seedArray[item][typeA]
    nounList  = seedArray[item][typeB]

    result = random.choice(actionList) + " " + random.choice(nounList)
    return result

def setDefaultSeed(checkbox, value):

    self = checkbox.self

    # first, get all the needed information
    check_func = checkbox.func
    check_type = checkbox.type

    # update config variables
    config.general['seed_func'] = check_func
    config.general['seed_type'] = check_type

    config.general['seed_alt_func'] = check_func
    config.general['seed_alt_type'] = check_type

    if check_func != 'useThreePartSeed':
        config.general['seed_subtype_pretty'] = "Seed"
        config.general['seed_alt_func'] = ''
    else:
        config.general['seed_subtype_pretty'] = "Desc"

    # now remove or add complex buttons as needed
    try:
        if config.general['seed_alt_func'] == '':
            self.seedButtonsBox.remove_widget(self.seedAlternateButton)
            self.seedButtonsBox.size_hint_y=1
    except:
        pass

    try:
        if config.general['seed_alt_func'] != '':
            self.seedButtonsBox.add_widget(self.seedAlternateButton)
            self.seedButtonsBox.size_hint_y=2
    except:
        pass

    self.seedButton.text = config.general['seed_subtype_pretty'].capitalize()

# standard Mythic style "action (adjective or verb) noun"
def useTwoPartSeed(*args):
    try:
        self = args[0].self
        args[0].background_color = neutral

        item = args[0].text
    except:
        self = args[0]
        item = args[1]

    # verb noun
    actionList = seedArray[item]['verb']
    nounList  = seedArray[item]['noun']

    result = random.choice(actionList) + " " + random.choice(nounList)

    updateCenterDisplay(self, "[" + string.capwords(item) + " Seed] " + result, 'oracle')

# location crafter style
def useThreePartSeed(*args):
    try:
        args[0].background_color = neutral
        self = args[0].self
        item = args[0].text
        subtype = args[0].subtype
    except:
        self = args[0]
        item = args[1]
        subtype = args[2]

    adjList = seedArray[item]['adjective']
    verbList = seedArray[item]['verb']
    nounList  = seedArray[item]['noun']
    advList = seedArray[item]['adverb']

    print(subtype)

    if subtype == "adjective":
        # adverb adjective
        adverb = random.choice(advList)
        adjective = random.choice(adjList)
        result = "[" + string.capwords(item) + " Desc] " + adverb + " " + adjective
    else:
        # verb noun
        verb = random.choice(verbList)
        noun = random.choice(nounList)
        result = "[" + string.capwords(item) + " Action] " + verb + " " + noun

    updateCenterDisplay(self, result, 'oracle')

def useAllSeed(*args):
    try:
        args[0].background_color = neutral
        self = args[0].self
        item = args[0].text
    except:
        self = args[0]
        item = args[1]

    result = random.choice(seedArray[item]['adverb']) + ", " + random.choice(seedArray[item]['adjective']) + ", " + random.choice(seedArray[item]['noun']) + " " + random.choice(seedArray[item]['verb'])

    updateCenterDisplay(self, "[" + string.capwords(item) + " Seed] " + result, 'oracle')

seedArray = {
    # general lists off the top of my head; pretty vanilla and bland
    'generic' : {
        'adjective' : ['peaceful', 'beautiful', 'kind', 'calm', 'stoic', 'meaningful', 'trivial', 'bland', 'spicy', 'fiesty', 'cruel', 'ugly', 'quarrelsome', 'paired', 'alone', 'edgy', 'endless', 'loved', 'loving', 'hated', 'hating', 'despised', 'secretive', 'open', 'stoic', 'veiled', 'plainspoken', 'honorable', 'dishonorable', 'trustworthy', 'untrustworthy', 'insane', 'clear', 'scary', 'calming'],
        'adverb' : ['likely', 'ruinously', 'hardly', 'ghostly', 'markedly', 'extremely', 'very', 'unlikely', 'open', 'closed', 'worse', 'better', 'freely', 'guardedly'],
        'verb' : ['accelerate', 'accumulate', 'acquire', 'adjust', 'adopt', 'advance', 'align', 'alter', 'anger', 'anticipate', 'assist', 'assume', 'bestow', 'carry', 'change', 'clarify', 'command', 'commit', 'conclude', 'consider', 'construct', 'control', 'convince', 'couple', 'determine', 'discover', 'disregard', 'divert', 'divide', 'draw', 'dream', 'edgy', 'educate', 'emphasize', 'enable', 'enchain', 'encourage', 'endless', 'enjoy', 'enrage', 'enter', 'entrance', 'eviscerate', 'examine', 'exchange', 'execute', 'exhaust', 'experience', 'facilitate', 'fascinate', 'feint', 'guess', 'impassion', 'improvise', 'inflame', 'inflate', 'interest', 'involve', 'justify', 'keep', 'ken', 'locate', 'loosen', 'lose', 'love', 'mend', 'mesmerize', 'motivate', 'murder', 'negotiate', 'nurture', 'obscure', 'overcome', 'penalize', 'quarter', 'question', 'refuse', 'reject', 'renegotiate', 'revenge', 'run', 'share', 'simplify', 'spy', 'squelch', 'stoic', 'strengthen', 'substitute', 'synthesize', 'teach', 'tighten', 'track', 'transition', 'trap', 'triumph', 'tumble', 'unify', 'unveil', 'weaken', 'withdraw'],
        'noun' : ['addiction', 'air', 'ally', 'armor', 'art', 'beyond', 'blood', 'bravery', 'change', 'class', 'cold', 'common', 'compassion', 'consumption', 'couple', 'cowardice', 'death', 'disaster', 'dispassion', 'displeasure', 'earth', 'earth', 'elements', 'emotions', 'enemy', 'fatigue', 'focus', 'foreign', 'forgiveness', 'freedom', 'friend', 'friendship', 'fury', 'future', 'grief', 'hatred', 'health', 'home', 'honor', 'hope', 'hot', 'ideas', 'illness', 'insanity', 'instinct', 'integrity', 'jewel', 'journey', 'joy', 'key', 'kin', 'location', 'love', 'luxuries', 'master', 'moderation', 'monster', 'moon', 'music', 'near', 'necessities', 'neighbor', 'obsession', 'passion', 'past', 'path', 'physical', 'possessions', 'power', 'priceless', 'quarry', 'quest', 'rain', 'reason', 'regret', 'reserves', 'rubbish', 'sex', 'shine', 'skill', 'sorrow', 'stalemate', 'star', 'status quo', 'stoicism', 'sun', 'survival', 'task', 'tool', 'trap', 'uncontrollable', 'unknowable', 'value', 'vengeance', 'violence', 'water', 'wealth', 'weapons', 'whimsy', 'work'],
        },
    # dracula, of course
    'gothic horror' : {
        'adverb' : ["absolutely", "actually", "afar", "afore", "almost", "alone", "altogether", "anchor", "aside", "away", "back", "beaten", "bore", "brightly", "certainly", "closely", "deadly", "decide", "discover", "downward", "earthly", "east", "eaten", "else", "entirely", "even", "evidently", "exactly", "fast", "finally", "find", "first", "fixedly", "fortunately", "forward", "frankly", "freely", "gather", "gently", "gradually", "gravely", "greatly", "hardly", "hat", "hoarsely", "horribly", "however", "immediately", "implore", "indeed", "instantly", "instinctively", "intently", "just", "keenly", "kindly", "lonely", "long", "loudly", "manifestly", "naturally", "night's", "noise", "nose", "now", "oddly", "often", "otherwise", "pause", "perfectly", "perhaps", "piccadilly", "positively", "presently", "probably", "properly", "quickly", "quietly", "rather", "really", "resolutely", "reverently", "right", "seemingly", "shortly", "simply", "slightly", "solemnly", "sometimes", "sternly", "still", "strangely", "strongly", "suddenly", "surely", "sweetly", "terribly", "therefore", "thoroughly", "thus", "truly", "usually", "well", "whither", "muchly", "yet"],
        'adjective' : ["absolute", "assent", "attendant", "attract", "bear", "black", "broad", "vampire", "child-brain", "come", "concealment", "dear", "deceive", "degree", "desperate", "diabolical", "eager", "ear", "earnest", "earth-box", "empty", "enough", "equal", "excellent", "fair", "fellow", "fierce", "fifty", "foreign", "forgive", "former", "fourth", "full", "funeral", "funny", "greater", "green", "grown", "hard", "heavy", "hidden", "high", "holy", "homicidal", "horrid", "human", "hungarian", "hysterical", "impossible", "injured", "instinct", "interested", "lantern", "latter", "leaden", "little", "live", "local", "main", "massive", "mixed", "nature's", "needless", "needn't", "next", "nice", "old", "opposite", "outside", "patient", "peculiar", "perfect", "personal", "physical", "poor", "present", "proper", "proud", "rough", "russian", "sight", "simple", "smile", "sorrowful", "sorry", "south", "special", "spiritual", "stern", "stole", "stricken", "successful", "sufficient", "supper", "sure", "suspicious", "swear", "third", "to-day", "to-night", "troubled", "unable", "unclean", "unhappy", "vague", "warm", "willing", "window-sill", "worse", "wrought"],
        'noun' : ["advance", "afford", "afternoon", "anyhow", "anything", "await", "band", "bare", "bird", "birds", "bless", "bloofer", "bosom", "boxes", "burst", "clever", "condition", "consent", "couple", "crucifix", "days", "difficulties", "disposal", "edge", "evidence", "excitement", "face", "fate", "fear", "fight", "fingers", "floor", "fog", "folk", "fool", "foul", "game", "grip", "ground", "hears", "helpless", "hint", "horse", "imagine", "information", "intention", "iron", "isself", "jaws", "joy", "knock", "lack", "launch", "law", "letters", "loves", "mad", "map", "masses", "memory", "men's", "minute", "minutes", "music", "nails", "night", "obedience", "observation", "occasion", "operate", "opportunities", "parts", "peace", "pity", "press", "pride", "purity", "race", "range", "rooms", "sea", "sheer", "sheet", "shelter", "shutters", "sign", "sky", "sleeps", "sleepy", "sob", "sorrow", "souls", "strength", "struggle", "telegraph", "thing", "throw", "torture", "towards", "visit", "weapons", "weather", "wheel", "whence", "window", "wood", "word", "work", "wound", "yield"],
        'verb' : ["continued", "agonise", "appear", "ask", "assure", "become", "bed", "begin", "belt", "bend", "blow", "chill", "clutch", "cold", "concern", "cunning", "dare", "desert", "determine", "direct", "end", "examine", "exhaust", "expect", "explain", "eyebrows", "fall", "fear", "feel", "fill", "find", "float", "fly", "force", "give", "grave", "grow", "help", "hundred", "hurry", "interest", "jump", "keep", "kill", "kitten", "kneel", "lap", "lay", "lie", "long", "make", "manage", "mark", "mean", "miss", "move", "occur", "open", "produce", "prolong", "pull", "put", "puzzle", "raise", "reach", "read", "relatives", "remember", "repeat", "restore", "resume", "rise", "roll", "rush", "scatter", "searchlight", "seem", "send", "sense", "shock", "shout", "show", "shut", "sink", "sleep", "something", "step", "stroke", "stroll", "teach", "touch", "turn", "walk", "want", "watch", "wave", "wear", "whisper", "win", "windows", "wolves"],
        },
    'sf horror' : {
        'adverb' : ["aboard", "accurately", "angrily", "away", "back", "blankly", "bleakly", "deadly", "divide", "else", "enormously", "even", "faintly", "first", "grimly", "here", "just", "long", "longer", "monotonously", "monstrously", "much", "nearly", "never", "now", "nucleotide", "patiently", "strangely", "silver", "strangely", "suddenly", "tenderly", "utterly", "vaguely", "weakly"],
        'adjective' : ["alien", "animal", "answer's", "arsenic", "astro-pilot", "atom", "binary", "black", "blood-colored", "blue-veined", "broken", "complex", "crazy", "dark", "dead", "dear", "desperate", "different", "double-stranded", "electronic", "eternal", "etext", "evil", "express", "extensive", "filthy", "fine-boned", "forty-hour", "frantic", "gear", "genetic", "gray-cased", "grid", "grime", "grown", "hard", "hear", "helical", "hidden", "hideous", "huge", "human", "native", "insect", "intercept", "lean", "many", "monstrous", "mutant", "needless", "new", "newest", "old", "open", "particular", "pock-marks", "precious", "pseudo-lilith", "quiet", "rag", "read", "real", "red", "riddle", "sallow", "secret", "seventh", "shallow", "shrank", "silent", "similar", "simplest-seeming", "smallest", "solitary", "spare", "spite", "sterile", "strange", "strangest", "sullen", "suppose", "teeth", "thick", "third", "triumphant", "uncover", "unknown", "uttered", "vegetable", "visible", "wrong", "yellow", "yellow-scummed"],
        'noun' : ["agony", "aid", "approach", "area", "astro-pilot", "astrogation", "astronauts", "atoms", "band", "bloom", "blooms", "blue-prints", "bones", "bring", "button", "cell", "chains", "chance", "circle", "code", "copter", "crater", "creepers", "cry", "dash", "dawn", "day", "days", "dna", "dot", "dusk", "earthmen", "encode", "fierce", "find", "force", "function", "generations", "get", "grope", "guard", "hairy", "home", "hum", "jet", "jets", "juices", "jungle", "key", "landing-jets", "leaves", "leer", "lock", "manipulate", "mask", "message", "micro-probe", "microscopic", "mission", "movement", "muck", "nucleotides", "observe", "places", "planet", "plant", "plot", "pods", "poison", "printer", "probe", "process", "publication", "root", "scowl", "screech", "sentinel", "shapeless", "ship", "show", "silence", "skeleton", "slender", "someone", "something", "stalk", "stone", "stream", "student", "stumps", "survey", "tension", "tentacles", "thing", "thunderbird", "times", "tons", "trace", "turquoise", "units", "use", "voice", "way", "weed", "wilderness", "woman", "word", "words", "worlds", "wreckage"],
        'verb' : ["become", "begin", "blacken", "blight", "bring", "bubble", "buy", "call", "carry", "char", "clang", "coil", "cold", "come", "complicate", "conceal", "constrict", "creep", "crowd", "cut", "decode", "design", "drop", "expect", "fall", "fell", "find", "flying", "form", "gasp", "gather", "get", "hat", "hide", "hold", "hundred", "jut", "keep", "kill", "know", "land", "lay", "lead", "learn", "leer", "link", "look", "lose", "map", "maroon", "murder", "mutter", "need", "nothing", "obey", "ooze", "probe", "produce", "punch", "puzzle", "rank", "renew", "replicate", "return", "rot", "run", "saw", "scar", "scowl", "scream", "search", "see", "show", "sit", "slip", "smoke", "snap", "splash", "stain", "stand", "sterilize", "stifle", "streak", "stun", "suffocate", "take", "tattered", "teem", "ten", "tire", "torment", "try", "turn", "twist", "unnerve", "volunteer", "waste", "watch", "wave", "wear", "whimper", "whir", "whisper", "wing", "wrecked"],
    },
    'history' : {
        'adverb' : ["abandon", "abroad", "accordingly", "actually", "ago", "alone", "already", "also", "altogether", "always", "aside", "assembly", "back", "beside", "bravely", "certainly", "commonly", "completely", "decide", "directly", "driven", "eleven", "else", "entirely", "equally", "even", "ever", "everywhere", "exactly", "excuse", "expressly", "faithfully", "far", "fast", "father", "feast", "first", "forward", "freely", "gallantly", "generally", "gradually", "greatly", "happily", "hardly", "heavily", "however", "immediately", "indeed", "instantly", "instead", "just", "lately", "later", "likely", "lonely", "longer", "lovely", "lover", "meantime", "naturally", "never", "nevertheless", "niece", "nobly", "notice", "now", "often", "otherwise", "particularly", "partly", "possibly", "presently", "pretty", "probably", "quickly", "quietly", "readily", "really", "restore", "scarcely", "secretly", "seldom", "severely", "slowly", "sometimes", "soon", "sooner", "speedily", "stately", "still", "suddenly", "therefore", "thoroughly", "thus", "tide", "together", "unfortunately", "usually", "violently", "whatever", "wonderfully", "yet", "youth"],
        'adjective' : ["agony", "ambitious", "angry", "attachment", "bad", "barbarous", "become", "black", "bloody", "bread", "busy", "candle", "careful", "castle", "clergy", "close", "cold", "come", "comfortable", "content", "crusade", "danish", "destroyed", "distant", "divide", "dreadful", "drunken", "early", "eldest", "false", "fine", "follow", "forest", "forgive", "fortnight", "gentle", "glad", "great", "grown", "hot", "imagine", "important", "infamous", "insulted", "invented", "keep", "latter", "long", "low", "many", "mean", "merciful", "military", "mortal", "nephew", "new", "next", "north", "obeyed", "occupied", "odious", "open", "opposite", "perfect", "possible", "precious", "prepared", "presented", "private", "protestant", "punish", "purpose", "queen", "ransom", "ready", "receive", "rid", "ridiculous", "romish", "rough", "second", "several", "shot", "single", "sixteen", "soften", "soldier", "son", "steady", "stern", "sudden", "superior", "swear", "third", "token", "treacherous", "tremendous", "triumphant", "true", "unjust", "unquiet", "unreformed", "useful", "vigorous", "violent", "whole", "willing", "worse"],
        'noun' : ["alliance", "altar", "armies", "assistance", "book", "bore", "break", "bridge", "camp", "cart", "ceremony", "chains", "chance", "churches", "clever", "confessions", "consent", "cruel", "cruelties", "custom", "customs", "dark", "daughter", "deaths", "declaration", "desert", "discontent", "dominions", "executions", "face", "forth", "forts", "gain", "governor", "grace", "harm", "health", "heard", "hill", "hills", "home", "hundreds", "hung", "joy", "judges", "ladies", "law", "loss", "man's", "massacre", "men", "messengers", "miseries", "misfortune", "monarch", "morning", "neck", "nobles", "none", "note", "occupy", "offering", "offices", "order", "pain", "paper", "pass", "plan", "point", "prayers", "presence", "princess", "punishment", "reason", "remember", "revenge", "room", "ruin", "safety", "sell", "sentence", "sermons", "side", "siege", "sign", "something", "sorry", "speeches", "stake", "stout", "success", "succession", "support", "sword", "take", "tents", "thousands", "title", "travellers", "treasurer", "treat", "treatment", "trust", "uncle", "wall", "waste", "wickedness", "widow", "wonder", "writers"],
        'verb' : ["abandon", "act", "admire", "afraid", "answer", "apply", "arrows", "assemble", "believe", "break", "bury", "cause", "celebrate", "charge", "commit", "conduct", "confess", "continue", "cross", "crowd", "debauch", "decline", "denounce", "deprive", "despatch", "die", "discover", "disperse", "dispose", "dissolve", "distinguish", "enter", "ethelred", "face", "fall", "find", "flee", "gallop", "give", "go", "happen", "hatred", "height", "hire", "hold", "hurry", "inspire", "introduce", "kneel", "knock", "know", "lay", "leave", "like", "maintain", "march", "mark", "mean", "oates", "object", "oblige", "obtain", "occasion", "order", "pardon", "place", "plot", "proceed", "proclaim", "provide", "pull", "reform", "refuse", "regard", "report", "retire", "ring", "roll", "roses", "run", "say", "scaffold", "seem", "sentence", "serve", "shin", "show", "stand", "start", "starve", "stirling", "submit", "suspect", "think", "tremble", "trust", "turn", "urge", "use", "vote", "want", "warn", "wicked", "win"],
        },
    # the simple art of murder
    'hardboiled' : {
        'adverb' : ["actually", "adhere", "ahead", "almost", "alone", "also", "always", "anyway", "apparently", "archer", "artificially", "artistically", "atmosphere", "automatically", "away", "back", "beard", "carefully", "certainly", "close", "completely", "constantly", "counter", "customarily", "daily", "deadly", "dishonestly", "drastically", "duly", "easily", "else", "emily", "entirely", "even", "ever", "exactly", "exclusively", "exquisite", "far", "fast", "forever", "fundamentally", "handsomely", "highly", "however", "humanly", "incomparably", "instead", "intellectually", "intimately", "jolly", "just", "largely", "lightly", "lively", "lonely", "long", "lovingly", "maybe", "mechanically", "merely", "mostly", "motherly", "never", "now", "obviously", "often", "otherwise", "perfectly", "perhaps", "personally", "practically", "pretty", "probably", "provide", "quickly", "quite", "quiver", "rather", "really", "recently", "relatively", "right", "seldom", "simply", "slightly", "slowly", "softly", "sometimes", "somewhere", "soon", "terribly", "them–her", "thereafter", "thereby", "therefore", "thoroughly", "together", "traditionally", "usually", "vance–probably", "vulgarly", "well", "yet"],
        'adjective' : ["amateur", "american", "appear", "arbutus", "arid", "artistic", "authentic", "average—detective", "average—or", "aware", "badly-scared", "bel-air", "belong", "better", "born", "casual", "cellar", "certain", "chic", "conventional", "conversational", "critic", "critical", "daylight", "dead", "detective", "distinguish", "dogcart", "don’t", "dose", "dreary", "early", "easy", "echo", "element", "epicurean", "evasive", "excellent", "expert", "fewer", "fine", "fingerman", "first-grade", "forgotten", "formal", "french", "frown", "funny", "good", "gray", "greek", "hard", "hidden", "higher", "idealistic", "imagined", "impossible", "incapable", "incomprehensible", "indirect", "infinite", "inquest", "insouciant", "international", "keenest", "known", "lad", "lingo", "literal", "little", "logician", "meretricious", "persian", "poor", "pose", "pre-war", "promiscuous", "punch", "rare", "read", "realistic", "satyr", "scientific", "seamy", "second", "second-rate", "semi-antique", "several", "significant", "simple", "slow", "social", "special", "startle", "superlative", "suppose", "suspected", "table", "trained", "triple", "tropical", "typical", "unusual", "upside", "utterly", "week-end", "well-bred", "well-heeled", "worst"],
        'noun' : ["ability", "amount", "anybody", "author", "ball", "blossoms", "body", "books", "brothels", "business", "buy", "cells", "champions", "city", "civilization", "climate", "coffee", "college", "combination", "conflict", "connoisseurs", "considerations", "content", "stool-pigeon", "cops", "corpse", "court", "crawl", "crust", "cute", "defend", "deny", "describe", "desks", "detachment", "detail", "dilemma", "distillation", "elements", "eliminate", "eyes", "fact", "feel", "flavor", "floor", "fraud", "gangsters", "garters", "goods", "grotesque", "hand", "house", "idiots", "imitator", "intrigue", "investigation", "jumps", "jury", "knows", "language", "makeup", "manner", "manners", "melodrama", "men", "morons", "murder", "mâché", "night", "office", "ones", "pair", "patterns", "physics", "platinum", "plausibility", "play", "pleasant", "problem", "racket", "realist", "refrain", "safety", "savage", "sayers", "scenes", "sense", "sex", "sham", "shelf", "shudder", "speech", "stoicism", "testimony", "texture", "thing", "tie", "time", "times", "trade", "tragedy", "triteness", "truth", "try", "village", "violation", "walk", "week", "witnesses", "wouldn’t"],
        'verb' : ["accord", "allow", "annoy", "answer", "argue", "become", "begin", "believe", "bowling", "break", "bring", "call", "cease", "cheat", "condone", "connect", "continue", "debunk", "decide", "depress", "describe", "dominate", "drop", "escort", "establish", "exhaust", "exist", "expose", "feature", "fielding", "find", "flatted", "flower", "fluster", "follow", "found", "get", "go", "guarantee", "happen", "hardboiled", "increase", "inhibit", "invalidate", "keep", "know", "lay", "learn", "leave", "lie", "look", "loosen", "lose", "mark", "mind", "miss", "move", "name", "need", "offer", "order", "penetrate", "perfect", "pick", "polish", "pot", "produce", "publish", "read", "remember", "remind", "require", "ring", "roughen", "saw", "say", "scent", "see", "seem", "sell", "shave", "sip", "speak", "spend", "stab", "stand", "streamline", "suggest", "swallow", "take", "talk", "tarnish", "tell", "think", "try", "turn", "uninhibited", "want", "weather", "wing", "write"],
        },
    'medieval romance' : {
        'adverb' : ["abode", "acold", "again", "all", "alone", "also", "always", "ashore", "away", "back", "best", "childlike", "down", "else", "ere", "err", "even", "ever", "evil", "faith", "far", "fast", "first", "harden", "hardly", "heaven", "heavily", "here", "herein", "indeed", "kingly", "knightly", "less", "lightly", "long", "mightily", "more", "much", "nigh", "none", "not", "now", "oft", "once", "only", "right", "soon", "still", "subtly", "surely", "that", "then", "there", "thereafter", "ruinously", "thus", "together", "too", "twice", "very", "violently", "visibly", "well", "wifely", "yet"],
        'adjective' : ["amorous", "answer", "banished", "best", "bitter", "black", "blame", "bliss", "blown", "break", "brief", "brown", "chiselled", "cold", "dark", "dead", "dear", "deciduous", "deep", "dim", "dire", "dread", "drifted", "eyeless", "fair", "false", "fancy", "fear", "fiery", "fitful", "forest", "forgotten", "free", "gaunt-cheeked", "glad", "glorious", "golden", "good", "great", "green", "grey", "happy", "hard", "heartened", "heavenly", "high", "higher", "highest", "hot", "imperial", "incestuous", "insubmissive", "intermittent", "joyous", "kindlier", "larger", "last", "late", "least", "less", "less", "light", "light-souled", "little", "long", "low", "lute-like", "maiden", "main", "manifest", "many", "memorial", "mine", "more", "most", "mystic", "naked", "old", "ominous", "other", "outlaw-like", "own", "pale", "past", "perpetual", "piteous", "poor", "precious", "proper", "quiet", "radiant", "rapturous", "red", "reverent", "right", "same", "sea-mew", "secret", "several", "sharp", "shouldst", "sightless", "silent", "slow", "soft", "song", "spare", "sprang", "springtide", "star-forsaken", "starless", "statelier", "strange", "strong", "sublime", "subtle", "subtler-eyed", "such", "sweet", "tired", "token", "trembling", "tremulous", "unblest", "undone", "vain", "virgin", "wan", "wearier", "welcome", "wet", "white", "white-handed", "wise", "wondrous", "wrath", "wrong", "young"],
        'noun' : ["afield", "aloud", "angels", "answer", "ardour", "bade", "barren", "blast", "bleak", "blithe", "blood", "bloodless", "bloom", "boughs", "bows", "branches", "breast", "bride", "bridegroom", "brother", "change", "chosen", "clang", "cup", "darkness", "dawn", "day", "dayspring", "death", "deed", "delight", "intoxicant", "doom", "dreams", "earth", "farewell", "feet", "fills", "fire", "flash", "flower", "flowers", "forecasts", "fret", "disguise", "fruitfulness", "girl-star", "gloom", "goodliness", "grace", "half", "halls", "hands", "hap", "haste", "hate", "harbour", "heard", "heart", "heartbeats", "hearts", "heaven", "heights", "hope", "isles", "labour", "lady", "laud", "leaps", "prison", "life", "light", "lord", "lot", "love", "lust", "maiden", "man", "marriage", "measure", "memory", "men", "mist", "moon", "morning", "mouth", "name", "nameless", "night", "nights", "part", "pity", "place", "pledge", "power", "quest", "raging", "rang", "round", "ruining", "sailing", "sake", "sands", "scar", "scarce", "scope", "sea", "sea-roses", "seed", "sense", "set", "shame", "sheer", "sleep", "sleepless", "snowbright", "sorrow", "soul", "souls", "sound", "spirit", "spring", "springs", "star", "repose", "streams", "strength", "strings", "strife", "sun", "sunset", "superflux", "sweet", "sword", "tender", "terrors", "castle", "thing", "passage", "veil", "virtue", "tracery", "triumph", "truth", "tune", "undone", "vow", "wail", "walks", "ways", "freedom", "wits", "word", "yore"],
        'verb' : ["ail", "anhungered", "answer", "be", "bear", "beat", "bid", "bind", "bless", "blind", "blow", "bow", "bring", "burn", "cast", "change", "child", "clothe", "come", "crown", "decline", "deepen", "debate", "dense", "desire", "die", "demean", "dishonour", "dividing", "do", "drown", "dwell", "endure", "errand", "evil", "fade", "feel", "flower", "flush", "foil", "forswear", "fro", "gather", "gaze", "glance", "glitter", "glow", "hallow", "handle", "hang", "hath", "fly", "heal", "heritage", "hold", "hunger", "hurry", "imprison", "keep", "king", "know", "lack", "laughing", "lay", "leave", "lie", "lips", "live", "look", "lose", "love", "made", "make", "meet", "mercy", "move", "naked", "overmuch", "kindled", "pass", "pierce", "plunge", "pray", "purge", "put", "quench", "quiver", "range", "rejoice", "ride", "rise", "roar", "roll", "round", "sacred", "saith", "save", "say", "see", "seek", "seem", "send", "serve", "settle", "shadow", "shaping", "shed", "shift", "shine", "shipwreck", "shorten", "show", "shut", "sight", "sin", "sing", "sit", "spake", "speak", "stand", "stir", "strew", "sunlit", "swell", "take", "thereof", "thin", "think", "touch", "turn", "vanquish", "wake", "waste", "wax", "wane", "whiten", "wist", "wring", "yearn", "yield", "stricken"],
        },
    # from 'the gun'
    'modern' : {
        'adverb' : ["abruptly", "ahead", "almost", "alone", "already", "apart", "aside", "atmosphere", "austere", "away", "back", "badly", "beside", "bitterly", "calmly", "close", "completely", "curiously", "easily", "else", "especially", "even", "everywhere", "exactly", "excitedly", "fast", "feebly", "finally", "foolishly", "gently", "gingerly", "gloomily", "grumpily", "helplessly", "hopefully", "impatiently", "inside", "instantly", "instead", "irritably", "just", "later", "maybe", "meanwhile", "nearsightedly", "nervously", "painfully", "perfectly", "perhaps", "pleasantly", "possibly", "presently", "pretty", "probably", "quickly", "quite", "rather", "really", "slightly", "slowly", "softly", "solemnly", "soon", "stairway", "start", "still", "suddenly", "thoughtfully", "together", "underbelly", "violently", "well", "whichever"],
        'adjective' : ["able", "accidental", "adapt", "alert", "alive", "become", "black", "brittle", "broken", "calm", "certain", "cheek", "circular", "cold", "complex", "concrete", "day-period", "dead", "debris", "deep", "detected", "disgust", "drum", "early", "edible", "eternal", "evolutionary", "eyepiece", "foolish", "free", "front", "frozen", "full", "garment", "give", "glad", "good", "gray", "guardian", "half-circle", "handsome", "hard", "heavy", "imagine", "important", "inscribed", "intelligent", "interested", "lamp", "last", "leaks", "least", "many", "mean", "metal-armored", "middle", "mile", "natural", "next", "nightfall", "open", "original", "outline", "pale", "partial", "past", "poor", "ready", "real", "regular", "right", "safe", "second", "shot", "single", "slid", "slim", "slow", "small", "soft", "spaceworthy", "strange", "suppose", "survive", "suspect", "tall", "terrible", "thick", "torn", "toxic", "true", "twisted", "unbroken", "underfoot", "underground", "underneath", "understand", "unfastened", "unfortunate", "universe", "unmoved", "unmoving", "unwinding", "valuable", "vast", "visible", "warfare", "whole", "young"],
        'noun' : ["afterwards", "answer", "archeologist", "base", "bits", "blond", "blow", "books", "bottom", "breath", "cables", "carbohydrates", "catch", "center", "chance", "chill", "city", "closer", "combat", "commission", "condition", "corridor", "crowns", "danger", "dark", "day-periods", "discover", "ember", "excuse", "expressionless", "fats", "feet", "films", "fire", "firm", "food", "formations", "foundations", "gears", "girders", "hand", "hands", "happens", "head", "horizon", "hundreds", "hung", "instruments", "journey", "keep", "kill", "knows", "land", "letters", "lips", "lists", "literature", "machine", "matter", "mind", "mission", "moment", "morning", "network", "outer", "paper", "paradox", "part", "particles", "parts", "patrols", "piece", "pins", "plaque", "point", "pole", "projectiles", "pull", "ramp", "read", "records", "remains", "repair", "ribbon", "rise", "sample", "screws", "serpent", "shoes", "shreds", "signs", "sixty", "size", "skin", "slag", "solution", "someplace", "something", "sort", "state", "stones", "struts", "tell", "theory", "thing", "tower", "walls", "warheads", "windmill", "work"],
        'verb' : ["add", "adjust", "aim", "appear", "believe", "blacken", "bolt", "bump", "call", "catch", "change", "char", "circle", "click", "dare", "dent", "destroy", "dip", "disappear", "dissipate", "disturb", "eat", "enemy", "find", "finish", "fire", "fly", "follow", "gap", "glance", "glint", "glow", "go", "grin", "grunt", "head", "helmet", "hesitate", "hurry", "interesting", "jewel", "jut", "kill", "know", "leave", "let", "load", "look", "make", "mat", "mount", "murmur", "mutter", "overlook", "peer", "pit", "poison", "preserve", "push", "realize", "remove", "replace", "resume", "roar", "rub", "rush", "scar", "sculpture", "seal", "see", "shatter", "show", "shudder", "sigh", "squat", "stagger", "stand", "start", "step", "stick", "stir", "stop", "store", "strain", "stretch", "stride", "strike", "study", "suck", "suppose", "take", "talk", "think", "throw", "uninviting", "use", "walk", "wander", "want", "watch", "whine", "whisper", "wing"],
    },
    # the three musketeers
    'swashbuckling' : {
        'adverb' : ["almost", "alone", "always", "aside", "asleep", "attentively", "away", "back", "before", "belly", "best", "carefully", "dearly", "down", "else", "even", "ever", "forward", "further", "hastily", "here", "however", "humbly", "immediately", "imprudently", "indeed", "invincibly", "just", "lightly", "long", "more", "most", "much", "nearly", "once", "only", "otherwise", "overheard", "perfectly", "plainly", "positively", "probably", "quite", "rather", "scarcely", "secretly", "still", "straight", "sure", "then", "there", "thus", "timidly", "together", "truly", "very", "well", "when-ever"],
        'adjective' : ["angry", "anxious", "avaricious", "better", "black", "cardinal", "considerable", "contrary", "convulsive", "correct", "dear", "difficult", "dogmatic", "doubtless", "dull", "excellent", "excited", "exterior", "fifty", "fine", "first", "following", "forth", "frightful", "full", "future", "good", "great", "happy", "hundred", "inclined", "ineffaceable", "infinite", "last", "latter", "least", "little", "long", "mildness", "more", "most", "much", "old-fashioned", "open", "ordinary", "other", "pale", "past", "pleasant", "possible", "pretty", "profoundest", "prompt", "prosperous", "queen's", "ready", "right", "royal", "sacred", "secret", "separate", "serious", "serious", "short", "silent", "simple", "sinister", "slight", "softened", "strange", "such", "treated", "uncertain", "understood", "unfortunate", "unknown", "unlikely", "weak", "whole", "worthy", "young"],
        'noun' : ["abduction", "accomplice", "action", "affair", "appointments", "attendant", "background", "bargain", "believers", "board", "bottles", "cause", "chair", "charming", "cloister", "comparison", "comrade", "convalescent", "convent", "copyright", "curl", "daybreak", "debt", "door", "dreams", "efforts", "enemy", "estimate", "evening", "everything", "excellency", "eyes", "father", "fear", "feet", "friends", "genius", "gentleman", "gesture", "girl", "hand", "hands", "heart", "height", "heresy", "horse", "host", "house", "idea", "infraction", "interests", "keys", "king", "kitchen", "letter", "life", "lovers", "magnificent", "monsieur", "musket", "need", "nothing", "object", "occasion", "part", "person", "pistol", "politeness", "prisoner", "prosperity", "protestations", "queen", "question", "rage", "rebels", "religion", "reproach", "rises", "roberges", "rounds", "search", "second", "servants", "silence", "someday", "someone", "speak", "sufferings", "supply", "swearing", "swords", "table", "taste", "teeth", "teller", "time", "times", "tomorrow", "town", "twelve", "whites", "wind", "window", "year", "years"],
        'verb' : ["allow", "announce", "answer", "appear", "approach", "ask", "assure", "attribute", "be", "beat", "believe", "bring", "bruise", "come", "continue", "cover", "cry", "dash", "dare", "deliver", "depart", "depend", "desire", "double", "dress", "drink", "encourage", "enter", "escape", "exclude", "exhaust", "fly", "follow", "gain", "give", "go", "grow", "guard", "have", "hold", "know", "look", "lower", "make", "murmur", "nail", "name", "place", "play", "ponder", "present", "promise", "prove", "raise", "recognize", "remain", "repeat", "resolve", "retire", "salute", "satisfy", "say", "see", "separate", "shade", "sleep", "speak", "start", "starve", "steel", "surprise", "take", "talk", "tell", "think", "turn", "utter", "vulgar", "wait", "want", "wish", "worse"],
    },

}
