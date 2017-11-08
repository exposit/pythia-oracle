# -*- coding: utf-8 -*
#
# Pythy is a markov generator that takes text files (or your current log) and turns them into
# sentences that are hopefully inspiring.
#
# It also has a rudimentry Eliza-type program that will DM for you very badly.
#
# To use it, you must install markovify and textblob.
#
# https://github.com/jsvine/markovify
# https://textblob.readthedocs.io/en/dev/
#

import imports
from imports import *
import config

def exclude():

    flag = True
    try:
        from textblob import TextBlob
        import markovify
        flag = False
    except:
        flag = True

    # comment this line out to add in Pythy
    flag = True

    return flag

def onEnter(self):
    # grab all texts in the text folder
    if os.path.exists(config.curr_game_dir + "sources"):
        texts = glob.glob(config.curr_game_dir + "sources" + os.sep + "*")
        for txt in texts:

            checkbox = CheckBox(size_hint=(.10,None), group='default_pythy')
            checkbox.self = self
            checkbox.subtype = txt
            checkbox.bind(active=setDefaultPythySource)
            self.pythyGrid.add_widget(checkbox)

            title = os.path.basename(txt)
            title = os.path.splitext(title)[0]
            button = Button(text=title, size_hint=(.90,None), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
            button.self = self
            button.subtype = txt
            button.bind(on_press=self.pressGenericButton)
            button.bind(on_release=getRandomSentences)
            self.pythyGrid.add_widget(button)

    l = ToggleButtonBehavior.get_widgets('default_pythy')
    for button in l:
        if button.subtype == config.general['default_pythy_source']:
            button.active = True
    del l

    setBlob(self)

    self.predictLabels = []
    for i in range(config.general['pythy_predict_box_count']):
        try:
            title = config.user['predict_word_list'][i]
        except:
            title = ""
        self.predictLabels.append(Label(text=title, size_hint=(1,.2), font_name='maintextfont', font_size=config.basefont80))
        self.predictBox.add_widget(self.predictLabels[-1])

    self.nextWordLabels = []
    for i in range(config.general['pythy_next_word_count']):
        try:
            title = config.user['next_word_list'][i]
        except:
            title = ""
        self.nextWordLabels.append(Label(text=title, size_hint=(1,.2), font_name='maintextfont', font_size=config.basefont80))
        self.nextWordBox.add_widget(self.nextWordLabels[-1])

    if config.general['pythy_predict_box_count'] <= 0:
        self.pythyMainBox.remove_widget(self.predictBox)

    if config.general['pythy_next_word_count'] <= 0:
        self.pythyMainBox.remove_widget(self.nextWordBox)

    self.predictButton.text="Auto-Predict: " + str(config.general['use_pythy_auto_complete'])

# add your widgets in here; see the gui for examples
def initPanel(self):

    self.pythyAItem = AccordionItem(title='Pythy Oracle', background_normal='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', background_selected='resources' + os.sep + 'bg_bars' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_5.png', min_space = config.aiheight)

    self.pythyMainBox = BoxLayout(orientation='vertical')

    self.pythyMainBox.add_widget(Label(text="Sentence Generators", size_hint=(1,.20)))

    button = Button(text="Recent Play Log Only", size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.subtype = "use-current"
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getRandomSentences)
    self.pythyMainBox.add_widget(button)

    self.pythyScroll = ScrollView(size_hint=(1,1))

    self.pythyGrid = GridLayout(cols=2, spacing=5, size_hint=(1, None))
    self.pythyGrid.bind(minimum_height=self.pythyGrid.setter('height'))
    self.pythyGrid.bind(minimum_width=self.pythyGrid.setter('width'))

    checkbox = CheckBox(size_hint=(.10,None), group='default_pythy', allow_no_selection=False)
    checkbox.self = self
    checkbox.subtype = "use-all"
    checkbox.bind(active=setDefaultPythySource)
    self.pythyGrid.add_widget(checkbox)

    button = Button(text="Current Play Log", size_hint=(.90,None), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.subtype = "use-all"
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getRandomSentences)
    self.pythyGrid.add_widget(button)

    self.pythyScroll.add_widget(self.pythyGrid)
    self.pythyMainBox.add_widget(self.pythyScroll)

    button = Button(text="GMBot Response", size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    button.self = self
    button.bind(on_press=self.pressGenericButton)
    button.bind(on_release=getResponse)
    #self.pythyMainBox.add_widget(button)

    self.predictButton = Button(text="Use Auto-Predict: " + str(config.general['use_pythy_auto_complete']), size_hint=(1,.15), background_normal='', background_color=neutral, background_down='', background_color_down=neutral, font_name='maintextfont')
    self.predictButton.self = self
    self.predictButton.bind(on_press=self.pressGenericButton)
    self.predictButton.bind(on_release=togglePythyPredict)
    self.pythyMainBox.add_widget(self.predictButton)

    self.predictBox = GridLayout(cols=1)
    self.predictBox.add_widget(Label(text="Prediction Seeds", size_hint=(1,.15)))
    self.pythyMainBox.add_widget(self.predictBox)

    self.nextWordBox = GridLayout(cols=1)
    self.nextWordBox.add_widget(Label(text="Suggested Next Word", size_hint=(1,.15)))
    self.pythyMainBox.add_widget(self.nextWordBox)

    self.pythyAItem.add_widget(self.pythyMainBox)

    return self.pythyAItem

# functions
def getRandomSentences(button):

    self = button.self
    button.background_color = neutral

    possible_responses = []
    result = "Nothing comes to mind. Maybe if you wrote a bit more?"

    tempArray = getPlainText()

    if "use-current" in button.subtype:
        r = random.randint(3, 7) * -1
        text = " ".join(tempArray[r:])
        possible_responses = getMarkov(text)

    elif "use-all" in button.subtype:
        possible_responses = getMarkov(" ".join(tempArray))

    else:
        with open(button.subtype, 'r') as textfile:
            text=textfile.read()
        possible_responses = getMarkov(text)

    try:
        result = random.choice(possible_responses)
    except:
        pass

    updateCenterDisplay(self, result, "oracle")

transposeList = ["are", "am"], ["am", "are"], ["were", "was"], ["was", "were"], ["you", "me"], ["i", "you"], ["your", "my"], ["my", "your"], ["i've", "you've"], ["you've", "i've"],  ["i'm", "you're"], ["you're", "i'm"], ["me", "you"], ["you", "me"], ["same", "alike"], ["similar", "alike"], ["illness", "poison"], ["disease", "poison"]

def getSmell():
    return "It smells like you'd expect."

def getSound():
    return "It sounds like you'd expect."

def getTaste():
    return "It tastes like you'd expect."

def getFeel():
    return "It feels like you'd expect."

def getIntuition():
    return "It intuits like you'd expect."

def refreshRules(snippets):

    rules = {
      "alike" : "Alike in what way?",
      "poison" : "You could make a saving throw at a " + random.choice(["hard", "easy", "standard"]) + " DC.",
      "monster" : "It looks " + random.choice(['tough', 'pretty easy', 'scary']) + ". What will you do?",
      "smell" : getSmell(),
      "sound" : getSound(),
      "taste" : getTaste(),
      "feel" : getFeel(),
      "intuition" : getIntuition(),
      "can" : random.choice(["Sure.", "No way.", "Roll for it.", "Yes.", "No."]),
    }

    return rules

def getMarkov(text):

    import markovify

    sentences = []
    text_model = markovify.Text(text)
    for i in range(5):
        if config.general['pythy_sentence_model'] == "short":
            sentence = text_model.make_short_sentence(140)
        elif config.general['pythy_sentence_model'] == "long":
            sentence = text_model.make_sentence()
        else:
            sentence = random.choice([text_model.make_sentence(), text_model.make_short_sentence(140)])
        if sentence:
            sentences.append(sentence)
    return sentences

def getResponse(button):

    from textblob import TextBlob
    from textblob import Word

    self = button.self
    button.background_color = neutral

    tempArray = getPlainText()

    blobs = []
    proper_names = []
    # pick the most recent block and two random earlier ones; weight it towards recent
    usable_blocks = [tempArray[-2]] + random.sample(tempArray[:-1], 2)
    for block in usable_blocks:
        blob = TextBlob(block)
        # do a quick tag noun check for proper nouns
        for word, tag in blob.tags:
            if tag == "NNP":
                proper_names.append(word)
        if len(blob.noun_phrases) > 0:
            blobs = blobs + blob.noun_phrases

    snippets = random.sample(blobs, len(blobs))

    snippets = [x.capitalize() if x in proper_names else x for x in snippets]

    possible_responses = []

    # first, responses from the memory
    if len(config.user['memory']) > 0:
        possible_responses.append("Earlier \"" + random.choice(config.user['memory']) + "\" came up. Tell me more.")

    config.user['memory'] = config.user['memory'] + snippets

    possible_responses.append("\"" + snippets[0].capitalize() + "\" from earlier becomes relevant.")

    # and finally, go through the last text block looking for keywords that might trigger specific responses
    text = usable_blocks[0]
    rules = refreshRules(snippets)

    for item in transposeList:
        text = text.replace(item[0], item[1])

    for key in rules:
        if key in text:
            possible_responses.append(rules[key])

    answer = random.choice(possible_responses)

    updateCenterDisplay(self, answer, "oracle")

def autoPredict(self):

    from textblob import TextBlob

    blob = self.blob

    marker = TextBlob(self.textInput.text)

    possibles = [x for x in blob.sentences if marker.words[-1] in x]

    # first update noun phrase labels, ie, prediction seeds
    noun_phrases = []
    for item in possibles:
        noun_phrases = noun_phrases + item.noun_phrases

    noun_phrases = [x for x in noun_phrases if x != "[ i ]" and x != "[ /i ]"]

    try:
        noun_phrases = random.sample(noun_phrases, config.general['pythy_predict_box_count'])
    except:
        pass

    for i in range(len(self.predictLabels)):
        try:
            if noun_phrases[i].startswith("n't"):
                noun_phrases[i] = noun_phrases[i][4:]
        except:
            pass
        try:
            if noun_phrases[i].startswith("'s"):
                noun_phrases[i] = noun_phrases[i][3:]
        except:
            pass
        try:
            if noun_phrases[i].startswith("'d"):
                noun_phrases[i] = noun_phrases[i][3:]
        except:
            pass
        try:
            self.predictLabels[i].text = noun_phrases[i]
            config.user['predict_word_list'][i] = noun_phrases[i]
        except:
            pass

    # now update potential next word
    possible_responses = []
    result = "Nothing comes to mind. Maybe if you wrote a bit more?"

    tempArray = getPlainText()

    if "use-all" == config.general['default_pythy_source']:
        source = " ".join(tempArray)

    else:
        with open(config.general['default_pythy_source'], 'r') as textfile:
            source = textfile.read()
        source = unicode(source, 'utf-8')

    import markovify

    sentences = []
    text_model = markovify.Text(source, state_size=1)
    for i in range(5):
        try:
            sentence = text_model.make_sentence_with_start(marker.words[-1])
            if sentence:
                sentences.append(TextBlob(sentence))
        except:
            pass

    usable_words = []
    for sentence in sentences:
        usable_words.append(sentence.words[1])

    usable_words = list(set(usable_words))

    for i in range(len(self.nextWordLabels)):
        try:
            self.nextWordLabels[i].text = usable_words[i]
            config.user['next_word_list'][i] = usable_words[i]
        except:
            pass

def getPlainText():

    tempArray = []
    for i in range(len(config.textArray)):
        if config.textStatusArray[i] == "plain" and len(config.textArray[i]) > 1:
            tempArray.append(config.textArray[i])

    return tempArray

def setDefaultPythySource(checkbox, value):

    config.general['default_pythy_source'] = checkbox.subtype
    setBlob(checkbox.self)

def togglePythyPredict(button):

    button.background_color = neutral
    setBlob(button.self)

    if config.general['use_pythy_auto_complete'] == True:
        config.general['use_pythy_auto_complete'] = False
    else:
        config.general['use_pythy_auto_complete'] = True

    button.text="Auto-Predict: " + str(config.general['use_pythy_auto_complete'])

def setBlob(self):

    from textblob import TextBlob

    if config.general['default_pythy_source'] == "use-all":
        source = " ".join(getPlainText())
    else:
        with open(config.general['default_pythy_source'], 'r') as textfile:
            source=textfile.read()
        try:
            source = unicode(source, 'utf-8')
        except:
            pass

    self.blob = TextBlob(source)
