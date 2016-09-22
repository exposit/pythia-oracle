# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#  world & dungeon panel
#
#
##---------------------------------------------------------------------------------------------------

import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):
    #print("update my own widgets")
    pass

def initPanel(self):

        self.hexAItem = AccordionItem(title='World & Dungeon', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)
        hexMainBox = BoxLayout(orientation='vertical')

        button = Button(text="Make Kingdom", size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "makeKingdom"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="Village Size", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "mathVillagePop"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="Town Size", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "mathTownPop"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="City Size", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "mathCityPop"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="Big City Size", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "mathBigCityPop"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        hexMainBox.add_widget(Label(text="Region Diagram Dungeon", size_hint=(1,.1)))

        regionTypeSpinner = Spinner(
            text='Random',
            values=["Random", "Scattered", "Dense", "Unsettled", "Frontier", "Desolate"],
            size_hint=(1,.25),
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            )

        regionTypeSpinner.self = self
        hexMainBox.add_widget(regionTypeSpinner)

        button = Button(text="Make a Region", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.value = 9
        button.self = self
        button.link = regionTypeSpinner
        button.randomnext = True
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getNewRegion)
        hexMainBox.add_widget(button)

        hexPointABox = GridLayout(cols=9, size_hint=(1,.2))
        for i in range(0,9):
            button = Button(text=str(i), size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.value = i
            button.link = regionTypeSpinner
            button.self = self
            button.randomnext = False
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getNewRegion)
            hexPointABox.add_widget(button)

        hexMainBox.add_widget(hexPointABox)

        hexMainBox.add_widget(Label(text="Upcoming Terrain", size_hint=(1,.1)))
        hexPointCBox = GridLayout(cols=9, size_hint=(1,.2))
        for i in range(0,9):
            button = Button(text=str(i), size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.value = i
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getUpcomingTerrain)
            hexPointCBox.add_widget(button)

        hexMainBox.add_widget(hexPointCBox)

        button = Button(text="Distance to Next Region", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getNextRegionDistance)
        hexMainBox.add_widget(button)

        hexMainBox.add_widget(Label(text='Miscellaneous Questions', size_hint=(1,.25)))

        button = Button(text="What's the Weather Like?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.function = "weatherWeighted"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="More or Less Than Expected?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=moreOrLessRoll)
        hexMainBox.add_widget(button)

        button = Button(text="How Difficult Is it?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.function = 'howDifficultWeighted'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="What Direction?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.function = 'whatDirection'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="What Is The Room Like?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.function = 'roomLike'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        button = Button(text="What Is The Passage like?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
        button.self = self
        button.function = 'passageLike'
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        hexMainBox.add_widget(button)

        hexMainBox.add_widget(Label(text='How Far Is It?', size_hint=(1,.25)))

        hexFarBox = GridLayout(cols=2, size_hint=(1,.25))
        howFarList = ['same room', 'same area', 'same region', 'anywhere']
        for item in howFarList:
            button = Button(text=item, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='Fantasque-Sans')
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=pressHowFar)
            hexFarBox.add_widget(button)

        hexMainBox.add_widget(hexFarBox)

        self.hexAItem.add_widget(hexMainBox)

        return self.hexAItem

#-------------------------------------------------------------------------------------------------------------------------------------------
# hexcrawl & wilderness panel button functions
#-------------------------------------------------------------------------------------------------------------------------------------------
def getNextRegionDistance(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = getDistance()
    updateCenterDisplay(self, result)

def getNewRegion(*args):
    self = args[0].self
    link = args[0].link
    density = link.text
    randomnext = args[0].randomnext
    args[0].background_color = neutral
    result = makeRegion(args[0].value, density, randomnext)
    updateCenterDisplay(self, result)

def getUpcomingTerrain(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = upcomingTerrain(args[0].value)
    updateCenterDisplay(self, result)

def miscChartRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = eval(args[0].function)()
    updateCenterDisplay(self, result)

def pressHowFar(*args):
    args[0].background_color = neutral
    self = args[0].self
    result = howFarIsIt(args[0].text)
    updateCenterDisplay(self, result)

def moreOrLessRoll(*args):
    args[0].background_color = neutral
    self = args[0].self
    text = "expected"
    if len(self.textInput.text) > 0:
        text = self.textInput.text

    result = morelessWeighted(text)
    updateCenterDisplay(self, result)
    self.textInput.text = ""

#-------------------------------------------------------------------------------------------------------------------------------------------
# --> Math based world generation
# inspired by http://www222.pair.com/sjohn/blueroom/demog.htm
# all dumb math errors, wildly inaccurate extrapolations, and lazy fudges are my fault
#-------------------------------------------------------------------------------------------------------------------------------------------
def makeKingdom(userandom=True, total_area=88700, subtype="Standard", popdensity=75, popfactor=5, kingdom_age=300):

    # lower popdensity for crappier world conditions, higher for better, with 120 being the best-ish and 30 being lowest-ish
    if userandom == True:
        # set variables here
        #total_area = random.randint(1, 6592772)
        roll = random.randint(1,100)
        if roll <= 5:
            # giant country, Russia, 5%
            roll = float(random.randint(1,25)) / 100
            total_area = int(6601670 - (6601670 * roll))
        elif roll <= 10:
            # big country, America or China, 5%
            roll = random.randint(-250000,250001)
            total_area = 3250000 + roll
        elif roll <= 11:
            # very small country, ie, Guernsey 1%
            roll = random.randint(1,100) + 20
            total_area = roll
        else:
            if roll <= 20:
                roll = random.randint(-200000,200001)
                total_area = 900000 + roll
            elif roll <= 40:
                roll = random.randint(-2000,2000)
                total_area = 4000 + roll
            else:
                total_area = random.randint(100000, 500000)

        subtype = random.choice(["Standard", "Pre-Crusades", "Renaissance"])
        popfactor = random.randint(1,5)
        popdensity = 0
        for i in range(6):
            popdensity = popdensity + random.randint(1,4)
        popdensity = popdensity * popfactor
        kingdom_age = random.randint(2, 30) * 100

    total_population = total_area * popdensity
    pop_remaining = total_population

    largest_city_pop_p = math.sqrt(total_population)
    largest_city_pop_m = random.randint(1,4) + random.randint(1,4) + 10
    largest_city_pop = int(largest_city_pop_p * largest_city_pop_m)

    second_largest_pop_p = (random.randint(1,4) + random.randint(1,4) * 10) / 100.0
    second_largest_pop = int(largest_city_pop * second_largest_pop_p)

    pop_remaining = pop_remaining - largest_city_pop - second_largest_pop

    cityList = [largest_city_pop, second_largest_pop]
    if subtype == "Renaissance" or subtype == "Pre-Crusades":
        target = 1000
    else:
        target = 8000

    cities = len(cityList)
    towns = 0
    count = 0
    while pop_remaining > target and count < 10:
        factor = (random.randint(1,4) + random.randint(1,4) * 5) / 100.0
        new_pop = cityList[-1] - (cityList[-1] * factor)
        if pop_remaining - new_pop >= 8000:
            cityList.append(new_pop)
            if pop_remaining > 8000:
                cities = cities + 1
            else:
                towns = towns + 1
            pop_remaining = pop_remaining - new_pop
        else:
            pop_remaining = target - 1
        count = count + 1
        pop_remaining = target - 10

    if subtype == "Standard":
        towns = (random.randint(1,8) * random.randint(1,8)) * len(cityList)

        townie_pop = towns * 2500

        pop_remaining = pop_remaining - townie_pop

    # everyone else lives in a village or hamlet, or solo in the wilderness
    while pop_remaining > 0:
        village_size = random.randint(2, 100) * 10
        if pop_remaining - village_size > 0:
            cityList.append(village_size)
            pop_remaining = pop_remaining - village_size
        else:
            pop_remaining = 0

    agrarian_land = (float(total_population / 180.0) / total_area) * 100

    wilderness_land = 100 - agrarian_land

    ruins = total_population / 5000000
    ruins = int(ruins * math.sqrt(kingdom_age))

    active_castles = int(total_population/50000)

    urban_string = ""
    for urban in cityList:
        urban_string = urban_string + " | "
        urban_string = urban_string + str(math.floor(urban))

    result = "Total area: " + str(total_area) + ", subtype: " + subtype + ", population density: " + str(popdensity) + ", population factor: " + str(popfactor) + ", kingdom age: " + str(kingdom_age)
    result = result + "\nTotal population: " + str(total_population)
    result = result + "\nCities: " + str(cities) + ", Towns: " + str(towns) + "\nCity/town populations (8k): " + str(urban_string)
    result = result + "\nAgrarian land percent: " + str(agrarian_land) + ", percent wilderness: " + str(wilderness_land)
    result = result + "\nRuins: " + str(ruins) + ", active castles: " + str(active_castles)

    return result

def mathBigCityPop():
    roll = random.randint(1,100)
    if roll < 75:
        roll = random.randint(12,100)
    else:
        roll = random.randint(50,80)

    return "[Big City Pop.] " + str(roll * 1000)

def mathCityPop():
    roll = random.randint(1,100)
    if roll < 75:
        roll = random.randint(8,12)
    else:
        roll = 10

    return "[City Pop.] " + str(roll * 1000)

def mathTownPop():
    roll = random.randint(1,100)
    if roll < 75:
        roll = random.randint(1,8)
    else:
        roll = 2.5

    return "[Town Pop.] " + str(roll * 1000)

def mathVillagePop():
    roll = random.randint(1,100)
    if roll < 75:
        roll = random.randint(2,100)
    else:
        roll = random.randint(5, 30)

    return "[Village Pop.] " + str(roll * 10)

# pointcrawl terrain generator
# inspired by these posts on the subject
#       http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html
#       http://mmmnm.blogspot.com/2014/11/random-solo-hexless-wilderness.html

terrain = [
    ["0", "coast (1)", "light forest (2)", "heavy forest (3)", "mountains (4)"],
    ["1", "coast (1)", "swamp (2)", "light forest (3)", "heavy forest (4)"],
    ["2", "heavy forest (1)", "light forest (2)", "plains (3)", "plains (4)"],
    ["3", "plains (1)", "plains (2)", "light forest (3)", "swamp (4)"],
    ["4", "plains (1)", "heavy forest", "light forest (3)", "hills (4)"],
    ["5", "hills (1)", "heavy forest (2)", "light forest (3)", "plains (4)"],
    ["6", "light forest (1)", "heavy forest (2)", "hills (3)", "mountains (4)"],
    ["7", "mountains (1)", "hills (2)", "light forest (3)", "deserts (4)"],
    ["8", "deserts (1)", "plains (2)", "hills (3)", "mountains (4)"],
]

def makeRegion(seed, settledlevel="Scattered", randomnext=False):

    if seed == 9:
        seed = random.randint(0,8)

    if settledlevel == "Random":
        settledlevel = random.choice(["Dense", "Scattered", "Frontier", "Unsettled", "Desolate"])

    ruins = []
    if settledlevel == "Dense":
        target = 99
        count = random.randint(3,6)
        targetList = ["Town", "Town", "Village", "City", "City", "City"]
        rcount = random.randint(1,3)
        if random.randint(1,100) < 50:
            ruins.append("sewer")
        if random.randint(1,100) < 50:
            ruins.append("habitation")
    elif settledlevel == "Scattered":
        target = 90
        count = random.randint(1,5)
        targetList = ["Town", "Town", "Village", "Village", "City"]
        rcount = random.randint(1,3)
        if random.randint(1,100) < 50:
            ruins.append("fortress")
        if random.randint(1,100) < 50:
            ruins.append("habitation")
    elif settledlevel == "Frontier":
        target = 75
        count = random.randint(1,4)
        targetList = ["Town", "Town", "Town", "Village", "Village", "Village", "City"]
        rcount = random.randint(1,6)
        if random.randint(1,100) < 75:
            ruins.append("fortress")
    elif settledlevel == "Desolate":
        target = 15
        count = random.randint(1,2)
        rcount = random.randint(4,8)
        targetList = ["Town", "Village", "Village", "Village"]
    else:
        settledlevel = "Unsettled"
        target = 50
        count = random.randint(1,5)
        targetList = ["Town", "Village", "City"]
        rcount = random.randint(1,8)

    settlements=[]
    for i in range(count):
        if random.randint(1,100) < target:
            settlements.append(random.choice(targetList))
            if settlements[-1] == "City":
                if random.randint(1,100) > 75:
                    settlements[-1] = "Capital City"
        else:
            if settledlevel == "Dense":
                settlements.append("Decayed City")
            else:
                settlements.append("Abandoned")

    if randomnext == True:
        next_choice = seed
        if seed <= 8 and seed >= 0:
            next_choice = seed + random.choice([-3,-2,-1,0,1,2,3])

        if next_choice > 8:
            next_choice = 8 - random.randint(0,4)
        elif next_choice < 0:
            next_choice = 0 + random.randint(0,3)
    else:
        next_choice = seed

    curr_terrain = terrain[next_choice]

    for i in range(rcount):
        ruins.append(random.choice(["cavern", "habitation", "fortress", "temple", "academy", "sewer"]))

    beneath = random.choice(["Ruins", "Caves", "Solid", "Solid", "Solid", "River"])

    terrain_string = curr_terrain[1] + " | " + curr_terrain[2] + " | " + curr_terrain[3] + " | " + curr_terrain[4]
    return "[Settled Level] " + settledlevel + " [Seed] " + curr_terrain[0] + "\n[Terrain Type] " + terrain_string + "\n[Settlements] " + str(list(settlements)) + "\n[Beneath] " + beneath + "\n[Known Ruins] " + str(list(ruins))

def getDistance():
    # empirical distance in time units; player will need to modify if necessary by terrain costs by system
    distance = random.randint(1,6)
    road = random.choice(["Yes", "No"])

    return "[Time Units] " + str(distance) + " [Road?] " + road

def upcomingTerrain(seed=0):

    curr_terrain = terrain[seed]
    roll = random.randint(1,100)

    if roll <= 10:    # 10% of the terrain
        result = curr_terrain[4]
    elif roll <= 30:  # 20% of the terrain
        result = curr_terrain[3]
    elif roll <= 60:    # 30% of the terrain
        result = curr_terrain[2]
    else:             # 40% of the terrain
        result = curr_terrain[1]

    return "[Terrain] " + result

def weatherWeighted():
    chart = {
        2 : "The opposite of yesterday.",
        3 : "Much less comfortable than yesterday.",
        4 : "Noticeably less comfortable than yesterday.",
        5 : "The same as yesterday.",
        6 : "Noticeably more comfortable than yesterday.",
        7 : "Much more comfortable than yesterday",
        8 : "The same as yesterday.",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[Weather] " + chart[roll]
    return result

def howDifficultWeighted():

    rolls = [random.randint(1,4), random.randint(1,4)]
    maxroll = max(rolls)
    minroll = min(rolls)

    diff = rolls[0] - rolls[1]
    chart = {
        -3 : "Trivial.",
        -2 : "Fairly easy.",
        -1 : "A bit easy.",
         0 : "On par with hero's abilities.",
         1 : "A bit difficult.",
         2 : "Fairly difficult.",
         3 : "Overwhelming.",
    }

    result = "[How Difficult?] " + chart[diff] + " [" + str(diff) + "]"
    return result

def morelessWeighted(text="expected"):

    chart = {
        2 : "Much less than ",
        3 : "Less than ",
        4 : "A bit less than ",
        5 : "As ",
        6 : "A bit more than ",
        7 : "More than ",
        8 : "Much more than ",
    }

    roll = random.randint(1,4) + random.randint(1,4)

    result = "[More or Less] " + chart[roll] + text + "."
    return result

def whatDirection():

    chart = {
        1 : "North or Up",
        2 : "Northeast",
        3 : "East or Right",
        4 : "Southeast",
        5 : "South or Down",
        6 : "Southwest",
        7 : "West or Left",
    }

    roll = random.randint(1,7)

    result = "[Direction] " + chart[roll] + ". If this direction won't work, use up or down."
    return result

def roomLike():

    oppositesChart = [
        ["rough", "smooth"],
        ["gleaming", "dull"],
        ["slick", "dry"],
        ["crumbling", "intact"],
        ["extreme", "mild"],
        ["cared for", "disused"],
        ["stone", "metal"],
        ["wood", "brick"],
        ["wood", "metal"],
        ["stone", "brick"],
        ["painted", "bare"],
        ["finished", "unfinished"],
        ["ostentatious", "spartan"],
        ["bare", "stuffed"],
        ["worn", "new-looking"],
    ]
    descChart = []
    for pairList in oppositesChart:
        descChart.append(random.choice(pairList))

    roll = random.randint(1, 3)
    descList = random.sample(descChart, roll)
    desc = ', '.join(descList)

    shapeChart = [
        "round", "square", "oval", "elongated", "rectangular", "trapezoidal",
    ]

    roll = random.choice([1,1,1,2])
    shapeList = random.sample(shapeChart, roll)
    shape = ', '.join(shapeList)

    sizeChart = [
        "large", "small", "average", "cubby", "alcove", "cavern", "nook", "chamber", "vault", "great", "negligible", "brief", "vast", "expansive", "extensive",
    ]
    size = random.choice(sizeChart)

    purposeChart = [
        "sleeping", "eating", "bathing", "bodily functions", "imprisoning", "killing", "disposal", "studying", "reading", "working", "crafting", "disassembling", "assembling", "interrogating", "relaxing", "recuperating", "mending", "rending", "cooking", "exercise", "planning", "plotting", "communing", "praying", "keeping", "displaying", "storing",
    ]

    roll = random.choice([1,2])
    purposeList = random.sample(purposeChart, roll)
    purpose = ', '.join(purposeList)

    result = "[Room] " + desc + " [Purpose] " + purpose + " [Size] " + size + " [Shape] " + shape
    return result

def passageLike():

    veerChart = ["continues straight", "ends abruptly", "winds left", "winds right", "sharp bend left", "sharp bend right", "slopes up or passes stairs", "slopes down or passes stairs", "doubles back"]

    veer = random.choice(veerChart)

    extrasChart = {
        2 : "nothing",
        3 : "an intersection",
        4 : "a side passage",
        5 : "nothing",
        6 : "a door or arch or gap in the wall",
        7 : "special",
        8 : "nothing",
    }

    roll = random.randint(1,4) + random.randint(1,4)
    extras = extrasChart[roll]

    specialChart = [
        "obstacle blocking path", "water", "pit", "chasm or stairs", "skylight or light source", "treasure", "useful item", "stairs", "shaft"
    ]
    if extras == "special":
        extras = random.choice(specialChart)

    result = "[Passage] " + veer + " [Special] " + extras
    return result

def howFarIsIt(subtype='same room'):

    rolls = [random.randint(1,4), random.randint(1,4)]
    if subtype == 'same room':
        chart = {
            -3 : "Touch.",
            -2 : "Arm's reach.",
            -1 : "A few steps away.",
             0 : "Melee range.",
             1 : "Throwing knife range.",
             2 : "A normal move away.",
             3 : "Other side of the room.",
        }
    elif subtype == 'same area':
        chart = {
            -3 : "Same room.",
            -2 : "Next room/space.",
            -1 : "Within a handful of rooms/spaces.",
             0 : "Just past a handful of rooms/spaces.",
             1 : "About half the area away.",
             2 : "More than half the area away.",
             3 : "As far as it's possible to go and still be in this area.",
        }
    elif subtype == 'same region':
        chart = {
            -3 : "Same room.",
            -2 : "Two weeks' travel.",
            -1 : "Within a week's travel.",
             0 : "Within " + random.choice(['two', 'three', 'four']) + " days of travel.",
             1 : "Within " + random.choice(['two', 'three']) + " weeks of travel.",
             2 : "Within " + random.choice(['two', 'three', 'four']) + " months of travel.",
             3 : "Same area.",
        }
    else:
        chart = {
            -3 : "Impossibly close.",
            -2 : "Same area",
            -1 : "Same region.",
             0 : "Close.",
             1 : "Close.",
             2 : "Impossibly far.",
             3 : "Distance is irrelevant or meaningless.",
        }

    diff = rolls[0] - rolls[1]

    result = "[How Far?] " + chart[diff]
    return result
