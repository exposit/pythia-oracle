# -*- coding: utf-8 -*-
##---------------------------------------------------------------------------------------------------
#
#  Secrets Panel
#
##---------------------------------------------------------------------------------------------------
import imports
from imports import *
import config

def exclude():
    return False

def onEnter(self):

    self.secretLabels = []
    self.secretButtons = []

    #entry = [interval, self.secretTextField.text, result]
    if len(config.general['secrets']) > 0:

        for i in range(len(config.general['secrets'])):

            # make a timer entry and a button to remove it
            trigger = Label(text=str(config.general['secrets'][i][1]), size_hint=(.75, None), height="40dp")
            self.secretDisplayGrid.add_widget(trigger)
            self.secretLabels.append(trigger)

            button = Button(text="Del", size_hint=(.25, None), height="40dp")
            button.bind(on_release=removeTrigger)
            button.self = self
            button.index = i
            self.secretDisplayGrid.add_widget(button)
            self.secretButtons.append(button)

def initPanel(self):

    self.secretAItem = AccordionItem(title='Secrets & Triggers', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.secretMainBox = BoxLayout(orientation='vertical')

    secretTextList = [
        'almost certain', 'very probable', 'probable', 'likely', 'possibly', 'even odds', 'doubtful', 'somewhat unlikely', 'probably not', 'improbable', 'almost certainly not' ]

    secretIntervalList = ['random', 'now', 'soon', 'later', 'much later']

    self.secretMainBox.add_widget(Label(text="Trigger Presets", size_hint=(1,.10)))

    for item in secretIntervalList:
        button = Button(text=item, size_hint=(1,.10))
        button.self = self
        button.bind(on_press=pressGenericButton)
        button.bind(on_release=addPresetTrigger)
        self.secretMainBox.add_widget(button)

    self.secretMainBox.add_widget(Label(text="Add Pass/Fail Trigger", size_hint=(1,.10)))

    # timers are made of a name, an interval, and a success/fail
    self.secretBaseBox = GridLayout(cols=2, size_hint=(1,.25))

    self.secretBaseBox.add_widget(Label(text="Trigger Name: ", size_hint=(1,.10), font_size=config.basefont75))
    self.secretNameField = TextInput(text="", size_hint=(1,None), height=config.tallheight)
    self.secretBaseBox.add_widget(self.secretNameField)

    self.secretBaseBox.add_widget(Label(text="Check Result: ", size_hint=(1,.10), font_size=config.basefont75))
    self.secretSuccessSpinner = Spinner(
    text='Fail',
    values=['Succeed', 'Fail'],
    background_normal='',
    background_color=accent1,
    background_down='',
    background_color_down=accent2,
    size_hint=(.25,1),
    )
    self.secretSuccessSpinner.self = self
    self.secretBaseBox.add_widget(self.secretSuccessSpinner)

    self.secretBaseBox.add_widget(Label(text="Odds: ", size_hint=(1,.10), font_size=config.basefont75))
    self.secretTextSpinner = Spinner(
    text='even odds',
    values=secretTextList,
    background_normal='',
    background_color=accent1,
    background_down='',
    background_color_down=accent2,
    size_hint=(.25,1),
    )
    self.secretTextSpinner.self = self
    self.secretBaseBox.add_widget(self.secretTextSpinner)

    self.secretBaseBox.add_widget(Label(text="Time: ", size_hint=(1,.10), font_size=config.basefont75))
    self.secretIntervalSpinner = Spinner(
    text='Random',
    values=secretIntervalList,
    background_normal='',
    background_color=accent1,
    background_down='',
    background_color_down=accent2,
    size_hint=(.25,1),
    )
    self.secretIntervalSpinner.self = self
    self.secretBaseBox.add_widget(self.secretIntervalSpinner)

    self.secretMainBox.add_widget(self.secretBaseBox)

    self.secretAddButton = Button(text="Add", size_hint=(1,.15))
    self.secretAddButton.bind(on_release=addCustomTrigger)
    self.secretAddButton.bind(on_press=pressGenericButton)
    self.secretAddButton.self = self
    self.secretMainBox.add_widget(self.secretAddButton)

    # this is where active timers are displayed
    self.secretDisplay = ScrollView(size_hint=(1, 1))
    self.secretDisplayGrid = GridLayout(cols=2, spacing=5, size_hint_y=None, size_hint_x=1)
    self.secretDisplayGrid.bind(minimum_height = self.secretDisplayGrid.setter('height'))
    self.secretDisplay.add_widget(self.secretDisplayGrid)
    self.secretMainBox.add_widget(self.secretDisplay)

    self.secretAItem.add_widget(self.secretMainBox)

    return self.secretAItem

#---------------------------------------------------------------------------------------------------
# secret functions
#---------------------------------------------------------------------------------------------------

def pressGenericButton(button):
    button.background_color = accent2

def addPresetTrigger(button, *args):
    button.background_color = neutral

    self = button.self
    time = button.text

    text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    if time == "now":
        interval = 1
    elif time == "soon":
        interval = random.randint(1, 5)
    elif time == "later":
        interval = random.randint(5, 10)
    elif time == "much later":
        interval = random.randint(10, 15)
    else:
        interval = random.randint(1, 15)

    typeList = ['Action', 'Social', 'Weird', 'World', 'Plot', 'Random']

    eventsList = []
    testsList = []
    extrasList = []

    for i in range(len(typeList)):
        eventsList.append("Random Event, " + typeList[i])

    testList = ['Perception', 'Wisdom', 'Knowledge', 'Search', 'Listen', 'Intelligence', 'Awareness', 'Spot']
    degreeList = ['hard', 'easy', 'standard']

    for i in range(len(testList)):
        for item in degreeList:
            testsList.append("Test of " + testList[i] + ", difficulty, " + item)

    extrasList = ["Actor Move", "Plot Move"]

    if random.randint(1,100) <= 50:
        result = random.choice(eventsList + extrasList)
    else:
        result = random.choice(eventsList + testsList + extrasList)

    entry = [interval, "Trigger " + "(" + text + ")", result]

    # make a new entry in the config.general list
    config.general['secrets'].append(entry)

    # make the new buttons
    trigger = Label(text=config.general['secrets'][-1][1], size_hint=(.75, None), height="40dp")
    self.secretDisplayGrid.add_widget(trigger)
    self.secretLabels.append(trigger)

    button = Button(text="Del", size_hint=(.25, None), height="40dp")
    button.bind(on_release=removeTrigger)
    button.index = len(self.secretLabels)-1
    button.self = self
    self.secretDisplayGrid.add_widget(button)
    self.secretButtons.append(button)

def addCustomTrigger(button, *args):
    button.background_color = neutral
    self = button.self
    # get values of the two spinners
    time = self.secretIntervalSpinner.text
    likely = self.secretTextSpinner.text
    success = self.secretSuccessSpinner.text

    # parse the values to get our limiter, and if there's anything really there
    secretTextList = [
        'almost certain', 'very probable', 'probable', 'likely', 'possibly', 'even odds', 'doubtful', 'somewhat unlikely', 'probably not', 'improbable', 'almost certainly not' ]

    secretOddsList = [99, 97, 94, 88, 75, 50, 25, 12, 6, 3, 1]

    secretIntervalList = ['random', 'now', 'soon', 'later', 'much later']

    if time == "now":
        interval = 1
    elif time == "soon":
        interval = random.randint(1, 5)
    elif time == "later":
        interval = random.randint(5, 10)
    elif time == "much later":
        interval = random.randint(10, 15)
    else:
        interval = random.randint(1, 15)

    roll = random.randint(1, 100)
    index = secretTextList.index(likely)
    odds = secretOddsList[index]

    if roll <= odds:
        result = "You missed something and it suddenly comes into play!"
    else:
        result = "Nothing."

    entry = [interval, self.secretNameField.text, result]

    if success == "Succeed":
        # you succeeded on your check, return info now
        updateCenterDisplay(self, "[" + self.secretNameField.text + "] " + result, 'result')

    else:
        # make a new entry in the config.general list
        config.general['secrets'].append(entry)

        # make the new buttons
        trigger = Label(text=config.general['secrets'][-1][1], size_hint=(.75, None), height="40dp")
        self.secretDisplayGrid.add_widget(trigger)
        self.secretLabels.append(trigger)

        button = Button(text="Del", size_hint=(.25, None), height="40dp")
        button.bind(on_release=removeTrigger)
        button.index = len(self.secretLabels)-1
        button.self = self
        self.secretDisplayGrid.add_widget(button)
        self.secretButtons.append(button)

def removeTrigger(button, *args):
    # remove the widget
    self = button.self
    self.secretDisplayGrid.remove_widget(self.secretLabels[button.index])
    self.secretDisplayGrid.remove_widget(button)
    # clear the trigger from config.general
    del config.general['secrets'][button.index]
    del self.secretLabels[button.index]
    del self.secretButtons[button.index]
