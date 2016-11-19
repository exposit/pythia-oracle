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

        self.worldAItem = AccordionItem(title='World & Wilderness', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)
        worldMainBox = BoxLayout(orientation='vertical')

        worldMainBox.add_widget(Label(text="Make Kingdom", size_hint=(1,.10)))

        sizeBox = GridLayout(cols=2, size_hint=(1,.10))

        button = Button(text="Modern", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getKingdomSize)
        sizeBox.add_widget(button)

        button = Button(text="Medieval", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getKingdomSize)
        sizeBox.add_widget(button)

        worldMainBox.add_widget(sizeBox)

        button = Button(text="Power Structure", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont', size_hint=(1,.10))
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getKingdomPowerStructure)
        worldMainBox.add_widget(button)

        kingdomBox = GridLayout(cols=2, size_hint=(1,.20))

        button = Button(text="Known Quirk", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getKingdomKnownQuirk)
        kingdomBox.add_widget(button)

        button = Button(text="Secret Quirk", background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getKingdomSecretQuirk)
        kingdomBox.add_widget(button)

        worldMainBox.add_widget(kingdomBox)

        worldMainBox.add_widget(Label(text="Region Diagram Dungeon", size_hint=(1,.1), font_size=config.basefont90))

        regionTypeSpinner = Spinner(
            text='Random',
            values=["Random", "Scattered", "Dense", "Unsettled", "Frontier", "Desolate"],
            size_hint=(1,.10),
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            )

        regionTypeSpinner.self = self
        worldMainBox.add_widget(regionTypeSpinner)

        button = Button(text="Make a Region", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.value = 9
        button.self = self
        button.link = regionTypeSpinner
        button.randomnext = True
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getNewRegion)
        worldMainBox.add_widget(button)

        worldPointABox = GridLayout(cols=9, size_hint=(1,.2))
        for i in range(0,9):
            button = Button(text=str(i), size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
            button.value = i
            button.link = regionTypeSpinner
            button.self = self
            button.randomnext = False
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getNewRegion)
            worldPointABox.add_widget(button)

        worldMainBox.add_widget(worldPointABox)

        worldMainBox.add_widget(Label(text="Upcoming Terrain", size_hint=(1,.1), font_size=config.basefont90))

        worldPointCBox = GridLayout(cols=9, size_hint=(1,.2))
        for i in range(0,9):
            button = Button(text=str(i), size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
            button.value = i
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getUpcomingTerrain)
            worldPointCBox.add_widget(button)

        worldMainBox.add_widget(worldPointCBox)

        button = Button(text="Distance to Next Region", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=getNextRegionDistance)
        worldMainBox.add_widget(button)

        worldMainBox.add_widget(Label(text='Miscellaneous Questions', size_hint=(1,.10), font_size=config.basefont90))

        button = Button(text="What's the Weather Like?", size_hint=(1,.1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
        button.function = "weatherWeighted"
        button.self = self
        button.bind(on_press=self.pressGenericButton)
        button.bind(on_release=miscChartRoll)
        worldMainBox.add_widget(button)

        worldMainBox.add_widget(Label(text='How Far Is It?', size_hint=(1,.10), font_size=config.basefont90))

        worldFarBox = GridLayout(cols=2, size_hint=(1,.25))
        howFarList = ['same room', 'same area', 'same region', 'anywhere']
        for item in howFarList:
            button = Button(text=item, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
            button.self = self
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=pressHowFar)
            worldFarBox.add_widget(button)

        worldMainBox.add_widget(worldFarBox)

        self.worldAItem.add_widget(worldMainBox)

        return self.worldAItem

#---------------------------------------------------------------------------------------------------
# worldcrawl & wilderness panel button functions
#---------------------------------------------------------------------------------------------------

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


#---------------------------------------------------------------------------------------------------
# --> Kingdom
#
#---------------------------------------------------------------------------------------------------

def getKingdomSize(button):

    button.background_color = neutral
    self = button.self

    if button.text == "Modern":
        mod = 2
    else:
        mod = 0

    chart = [
        ("vast", "Russia", "Russia", "Russia"),
        ("massive", "China", "United States", "Canada"),
        ("great", "Australia", "India", "Kazakhstan"),
        ("major", "Mexico", "Indonesia", "Libya"),
        ("large", "Peru", "Mongolia", "South Africa"),
        ("medium", "Turkey", "Chile", "Morocco"),
        ("small", "France", "Sweden", "Germany"),
        ("small", "France", "Sweden", "Germany"),
        ("minor", "United Kingdom", "New Zealand", "Italy"),
        ("modest", "Greece", "North Korea", "Iceland"),
        ("minor", "Denmark", "Switzerland", "Slovakia"),
        ("petty", "The Bahamas", "Montenegro", "Slovenia"),
        ("city-state", "Hong Kong", "Samoa", "Barbados"),
    ]

    # result of 0 to 12
    roll = random.randint(1, 7) + random.randint(1, 7) - mod
    if roll > 12:
        roll = 11

    option = chart[roll]

    comp = random.choice([option[1], option[2], option[3]])

    result = "[Kingdom Size] " + option[0] + " (" + comp + ")"

    updateCenterDisplay(self, result)

def getKingdomPowerStructure(button):

    button.background_color = neutral
    self = button.self

    powertype = ["a democracy", "a republic", "a monarchy", "a dictatorship", "a democratic republic", "a collection of city-states", "made up of those who serve the guilds and banks", "made up of thieves", "authoritarian", "totalitarian", "in anarchy", "libertarian", "bureaucratic", "tribalism", "feudalism", "a loose collection of clans", "in service to those with wealth and trade connections", "infested with criminals at all levels", "ruled with an iron fist", "guided by enlightened self-interest", "a meritocracy", "guided by a noble class decided by birth", "guided by a citizen class decided by service"]

    primaryleader = ["the sorcerer-king", "a cabal of sorcerers", "a king", "a usurper", "a ruling council of seven", "a body of ex-soldiers", "the high king", "a gathering of clan leaders", "a war chief in war and a peace chief in peace", "a leader", "a group of noble houses", "the head of the church", "a cult leader", "a holy person", "a normally stigmatized group", "a charismatic leader", "a warlord", "a tyrant", "a dictator", "a tribunal of miltary leaders", "a tribunal of craftsmen", "an incestuous pack of feuding noble houses", "a seer", "a wizard", "a regent"]

    powergroups = ["the church", "the nobles", "the aristocracy", "the working class", "the slaves", "the serfs", "the common man", "everyone", "no one", "the nearest kingdom", "the criminal element", "the military", "a powerful guild", "a weak guild", "a powerful trade partner", "a weak trader partner", "a powerful moneylender", "the wealthy", "the honorable", "the dutiful", "those who have inherited power", "those who have earned power", "those who have taken power by force", "those who have schemed for power", "the educated", "the ill-educated", "the powerful", "the meek", "the most skilled craftsmen", "the less skilled craftsmen", "the movers and shakers", "the ruler's advisors", "a normally stigmatized class"]

    methodstopower = ["elected by peers", "public acclaim", "usurping", "hereditary", "de facto", "feared", "unopposed", "ruthlessly disposed of rivals", "a loophole in the law", "the only option", "the best hope", "a figurehead", "a wildcard", "unstable", "weak", "strong", "stable", "dependent", "independent", "assassination", "scheming", "slander and lies", "betrayal", "seduction", "vast wealth", "the last survivor", "the last of the line", "the last of the blood"]

    roll = random.randint(1,100)
    if roll <= 50:
        ptype = random.sample(powertype,2)
        ptype = ", and ".join(ptype)
    else:
        ptype = random.choice(powertype)

    powergroup = random.sample(powergroups, 2)

    result = "[Power] The government is " + ptype + ". The highest authority is " + random.choice(primaryleader) + " (" + random.choice(methodstopower) + ") with the support of " + powergroup[0] + " and the enmity of " + powergroup[1]  + "."

    updateCenterDisplay(self, result)

def getKingdomKnownQuirk(button):
    button.background_color = neutral
    self = button.self

    subject = ["The majority", "A minority", "The common folk", "The nobles", "The elite", "The rulers", "The church leaders", "The poor", "The wealthy", "The working people", "The craftspeople", "Criminals", "The servant or slave class", "The ruler's advisors", "The ruler's family and hanger-ons", "A particular noble house's members", "The ruler's most trusted allies"]

    adjective = ["ill-educated", "ill-fed", "very poor", "prosperous", "greedy", "greedy and rapacious", "frugal", "law-abiding", "[roll up a \"Defining Characteristic\" from the Actor Panel]", "feuding and belligerent", "subdued", "repressed", "imprisoned", "very traditional", "very untraditional", "proud of a local feature like a waterfall, forest, or building", "proud of a local ability like sailing, fishing, or navigating swamps", "proud of a local product like ale, wine, or wool", "proud of a local tradition like a festival, ceremony, or religious rite", "proud of a magical (spiritual) power only they possess", "subject to a magical (spiritual) curse", "cursed with ill-luck", "blessed with good luck", ]

    general = [ "Many thieves among the populace", "The land is very rocky and inhospitable", "Arable land is plentiful", "The land is rich in some valuable resource", "The land is rich in a ridiculously valuable, ridiculously rare resource", "The land is very dangerous and inhospitable, the people rugged and hardy", "Renowned for their fierce tempers", "Renowned for their pride", "Skilled swordsmen", "Duelists and poets, with quick tempers", "Renowned for women of great physical beauty", "Known for the great physical beauty of both sexes", "The people live comparatively long lives in good health", "The people tend to have few children, late in life", "The people tend to have many children", "A great oracle lives in seclusion here", "A great hero hailed from here", "A great civilization was formed here long ago"]

    for group in subject:
        for obj in adjective:
            general.append(group + " are " + obj + ".")

    result = "[Known Quirk] " + random.choice(general)

    updateCenterDisplay(self, result)

def getKingdomSecretQuirk(button):
    button.background_color = neutral
    self = button.self

    subject = ["The majority", "A minority", "The common folk", "The nobles", "The elite", "The rulers", "The church leaders", "The poor", "The wealthy", "The working people", "The craftspeople", "Thieves", "Assassins", "Criminals", "The servant or slave class", "The ruler's advisors", "The ruler's family and hanger-ons", "A particular noble house's members", "The ruler's most trusted allies"]

    adjective = ["serving dark masters", "licentious", "feuding", "in league with a neighboring kingdom", "fomenting rebellion", "seeking a replacement leader", "very untraditional", "very traditional", "hiding a magical (spiritual) power only they possess", "subject to a magical (spiritual) curse", "cursed with ill-luck", "blessed with good luck", "[roll up a \"Defining Characteristic\" from the Actor Panel]"]

    general = ["Dark magic permeates the country", "Powerful thieves' guild or mafia runs things", "The land is rich in some valuable resource", "The land is rich in a ridiculously valuable, ridiculously rare resource", "Monsters stalk the realm at night", "People go missing far more commonly than might be expected", "A rebel group has formed, diametrically opposed to one of the groups in power and headed by someone surprising", "A rare monster is somewhere nearby", "A great treasure was hidden here in ages past", "An ancient library is somewhere nearby"]

    for group in subject:
        for obj in adjective:
            general.append(group + " are " + obj + ".")

    result = "[Secret Quirk] " + random.choice(general)

    updateCenterDisplay(self, result)

# pointcrawl terrain generator
# inspired by these posts on the subject
#       http://hillcantons.blogspot.com/2014/11/reader-query-random-solo-wilderness.html
#       http://mmmnm.blogspot.com/2014/11/random-solo-worldless-wilderness.html

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