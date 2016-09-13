'''

==============

Pythia-Oracle 0.5.0

The MIT License (MIT)
Copyright (c) 2016 exposit

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''

import kivy
kivy.require('1.8.0')

# override config values, I'm sure there's a tidier way to do this
kivy.config.Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#kivy.config.Config.set ( 'graphics', 'width', 1280 )
#kivy.config.Config.set ( 'graphics', 'height', 725 )
kivy.config.Config.set ( 'graphics', 'resizable', 0)

# uncomment the next line and comment out the previous four if you want fullscreen
#kivy.config.Config.set ( 'graphics', 'fullscreen', 'auto')

from imports import *
from main import MainScreen
import config

class TitleScreen(Screen):

    def __init__ (self,**kwargs):
        super (TitleScreen, self).__init__(**kwargs)

        # super().__init__(**kwargs)

        Builder.load_file('style.kv')

        Window.clearcolor = (neutral[0]*.75, neutral[1]*.75, neutral[2]*.75,.5)

        texture = ObjectProperty()

        self.texture = Image(source='resources' + os.sep + 'bg_title' + os.sep + styles.curr_palette["name"].replace (" ", "_") + '_1.png').texture
        self.texture.wrap = 'repeat'
        self.texture.uvsize = (4, 4)

        with self.canvas:
            Rectangle(pos=(0,0), size=Window.size, texture=self.texture)

        self.mainAnchor = AnchorLayout(anchor_x='center', anchor_y='center')

        # first thing, try to open styles
        try:
            with open("." + os.sep + "resources" + os.sep + "defaults" + os.sep + "current_game.txt", "r") as config_file:
                gamename = config_file.read()
                config.curr_game_dir = "." + os.sep + "saves" + os.sep + gamename.strip() + os.sep
        except:
            pass

        try:
            with open(config.curr_game_dir + "config.txt", "r") as config_file:
                tempDict = json.load(config_file)
                for i in tempDict['general']:
                    config.general[i] = tempDict['general'][i]
                for i in tempDict['user']:
                    config.user[i] = tempDict['user'][i]
                for i in tempDict['adventure']:
                    config.modvar[i] = tempDict['adventure'][i]
        except:
            pass

        self.mainBox = BoxLayout(orientation='vertical', size_hint_x=.8, size_hint_y=.6, spacing=20)
        #with self.mainBox.canvas:
        #    Rectangle(pos=(440,400), size=(320,195), texture=self.subtexture)

        self.preTitleLabel = ClickLabel(text=config.general['pretitle'], font_size=22, font_name='Miamanueva', halign="center", background_normal='', background_color=(0,0,0,0), background_down='', background_color_down=(0,0,0,0))
        self.preTitleLabel.bind(on_press=self.changePreTitle)
        #self.preTitleLabel.bind(on_press=self.pressGenericButton)

        self.currentLabel = Label(text=string.capwords(config.curr_game_dir.split(os.sep)[-2]), font_size="36dp", font_name='Cormorant', halign="center")

        self.postTitleLabel = ClickLabel(text=config.general['posttitle'], font_size="22dp", font_name='Miamanueva', halign="center", background_normal='', background_color=(0,0,0,0), background_down='', background_color_down=(0,0,0,0))
        self.postTitleLabel.bind(on_press=self.changePostTitle)
        #.postTitleLabel.bind(on_press=self.pressGenericButton)

        self.startButton = Button(text="Start", background_normal='', background_color=accent1, background_down='', background_color_down=accent2, font_name='Cormorant', font_size="22dp")
        self.startButton.bind(on_press=self.pressStart)
        self.startButton.bind(on_release=self.releaseStart)

        palettes = []

        for item in styles.palette:
            palettes.append(styles.palette[item]['name'])

        self.paletteSpinner = Spinner(
            text=styles.curr_palette['name'],
            values=palettes,
            background_normal='',
            background_color=accent1,
            background_down='',
            background_color_down=accent2,
            size_hint=(.5, 1),
            font_name='Cormorant',
            font_size="22dp",
            )

        self.paletteSpinner.bind(text=self.changePalette)

        self.loadButton = Button(text="Load", background_normal='', background_color=accent1, background_down='', background_color_down=accent2, font_name='Cormorant', font_size="18dp")
        self.loadButton.bind(on_press=self.pressGenericButton)
        self.loadButton.bind(on_release=self.releaseLoad)

        self.newButton = Button(text="New Game", background_normal='', background_color=accent1, background_down='', background_color_down=accent2, font_name='Cormorant', font_size="18dp")
        self.newButton.bind(on_press=self.pressGenericButton)
        self.newButton.bind(on_release=self.newGame)

        self.newModuleButton = Button(text="New Game With Module", background_normal='', background_color=accent1, background_down='', background_color_down=accent2, font_name='Cormorant', font_size="18dp")
        self.newModuleButton.bind(on_press=self.pressGenericButton)
        self.newModuleButton.bind(on_release=self.newGameModule)

        self.mainBox.add_widget(self.preTitleLabel)
        self.mainBox.add_widget(self.currentLabel)
        self.mainBox.add_widget(self.postTitleLabel)
        self.mainBox.add_widget(Label(text=""))
        self.mainBox.add_widget(self.startButton)
        self.mainBox.add_widget(self.loadButton)
        self.mainBox.add_widget(self.newButton)
        self.mainBox.add_widget(self.newModuleButton)

        self.paletteBox = BoxLayout(orientation='horizontal')
        self.paletteBox.add_widget(self.paletteSpinner)
        self.paletteSample = Image(source="." + os.sep + "resources" + os.sep + "bg_sample" + os.sep + str(styles.curr_palette['name']).replace (" ", "_") + ".png", allow_stretch=True, keep_ratio=False, size_hint=(.5,1))
        self.paletteBox.add_widget(self.paletteSample)

        self.mainBox.add_widget(self.paletteBox)

        self.mainAnchor.add_widget(self.mainBox)

        self.add_widget(self.mainAnchor)

        saves = glob.glob("." + os.sep + "saves" + os.sep + "*" + os.sep)

        self.savesBox = BoxLayout(orientation="vertical")
        for savefolder in saves:
            timestamp = " (%s)" % time.ctime(os.path.getmtime(savefolder + "main.txt"))
            title = savefolder.split(os.sep)[-2]
            if title == "quicksave":
                gamename = title + " " + timestamp
            else:
                try:
                    with open(savefolder + "config.txt", "r") as config_file:
                        tempDict = json.load(config_file)
                        pre = tempDict['general']['pretitle'].replace('\n', ' ')
                        post = tempDict['general']['posttitle'].replace('\n', ' ')
                except:
                    pre = ""
                    post = ""
                gamename = pre + " " + title + " " + post + timestamp
            btn = Button(text=gamename, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
            btn.game = savefolder
            self.savesBox.add_widget(btn)
            btn.bind(on_release=self.choseGameToLoad)
            btn.bind(on_press=self.pressGenericButton)

        self.savesPopup = Popup(title='Saves',
            content=self.savesBox,
            size_hint=(None, None), size=("800dp", "530dp"),
            auto_dismiss=True)

        self.newGameBox = BoxLayout(orientation="vertical")
        self.newGameNameInput = TextInput(text="", multiline=False)
        self.newGameBox.add_widget(self.newGameNameInput)

        self.newGameStatus = Label(text="Enter a new name.")
        self.newGameBox.add_widget(self.newGameStatus)

        btn = Button(text="Confirm", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.newGameBox.add_widget(btn)
        btn.bind(on_release=self.makeNewGame)
        btn.bind(on_press=self.pressGenericButton)

        self.newGamePopup = Popup(title='New Game',
            content=self.newGameBox,
            size_hint=(None, None), size=("400dp", "400dp"),
            auto_dismiss=True)

        self.preTitleBox = BoxLayout(orientation="vertical")
        self.preTitleNameInput = TextInput(text="", multiline=False)
        self.preTitleBox.add_widget(self.preTitleNameInput)

        btn = Button(text="Confirm", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.preTitleBox.add_widget(btn)
        btn.bind(on_release=self.confirmPreTitle)
        btn.bind(on_press=self.pressGenericButton)

        self.preTitlePopup = Popup(title='Pre Title',
            content=self.preTitleBox,
            size_hint=(None, None), size=("200dp", "150dp"),
            auto_dismiss=True)

        self.postTitleBox = BoxLayout(orientation="vertical")
        self.postTitleNameInput = TextInput(text="", multiline=False)
        self.postTitleBox.add_widget(self.postTitleNameInput)

        btn = Button(text="Confirm", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.postTitleBox.add_widget(btn)
        btn.bind(on_release=self.confirmPostTitle)
        btn.bind(on_press=self.pressGenericButton)

        self.postTitlePopup = Popup(title='Post Title',
            content=self.postTitleBox,
            size_hint=(None, None), size=("200dp", "150dp"),
            auto_dismiss=True)

        # make a new game with a module
        available_modules = glob.glob("." + os.sep + "resources" + os.sep + "modules" + os.sep + "*" + os.sep)

        self.modulesBox = BoxLayout(orientation="vertical")
        for modfolder in available_modules:
            modname = modfolder.split(os.sep)[-2]
            btn = Button(text=modname, size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
            btn.module = modfolder
            self.modulesBox.add_widget(btn)
            btn.bind(on_release=self.choseModuleToLoad)
            btn.bind(on_press=self.pressGenericButton)

        btn = Button(text="None", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        btn.module = "None"
        self.modulesBox.add_widget(btn)
        btn.bind(on_release=self.choseModuleToLoad)
        btn.bind(on_press=self.pressGenericButton)

        self.modulesPopup = Popup(title='Modules',
            content=self.modulesBox,
            size_hint=(None, None), size=("800dp", "530dp"),
            auto_dismiss=True)

        self.newModGameBox = BoxLayout(orientation="vertical")
        self.newModGameNameInput = TextInput(text="", multiline=False)
        self.newModGameBox.add_widget(self.newModGameNameInput)

        self.newModGameStatus = Label(text="Enter a new name.")
        self.newModGameBox.add_widget(self.newModGameStatus)

        btn = Button(text="Confirm", size_hint=(1,1), background_normal='', background_color=neutral, background_down='', background_color_down=accent2, font_name='Fantasque-Sans')
        self.newModGameBox.add_widget(btn)
        btn.bind(on_release=self.makeNewModGame)
        btn.bind(on_press=self.pressGenericButton)

        self.newModGamePopup = Popup(title='New Game with Module',
            content=self.newModGameBox,
            size_hint=(None, None), size=("400dp", "400dp"),
            auto_dismiss=True)

    def pressStart(self, *args):
        self.startButton.background_color = accent2
    def releaseStart(self, *args):
        self.startButton.background_color = accent1
        if os.path.exists(config.curr_game_dir):
            self.manager.transition = SlideTransition(duration=1,clearcolor=(primary[0], primary[1], primary[2], 1), direction="up")
            self.manager.current = 'mainscn'
            # now update so the last opened game will be opened again next time
            config.curr_game_dir = config.curr_game_dir.strip()
            try:
                with open("." + os.sep + "resources" + os.sep + "defaults" + os.sep + "current_game.txt", "w") as config_file:
                    gamename = config.curr_game_dir.split(os.sep)[-2]
                    config_file.write(gamename)
            except:
                pass
        else:
            self.newGamePopup.open()
            self.newGameStatus.text = "no game loaded"

    def changePalette(self, *args):
        args[0].background_color = accent1
        self.paletteSample.source = "." + os.sep + "resources" + os.sep + "bg_sample" + os.sep + str(args[1]).replace (" ", "_") + ".png"
        for item in styles.palette:
            if styles.palette[item]['name'] == args[1]:
                try:
                    with open("." + os.sep + "resources" + os.sep + "defaults" + os.sep + "current_palette.txt", "w") as config_file:
                        config_file.write(item)
                except:
                    pass

    def changePreTitle(self, *args):
        #args[0].background_color = ''
        #self.preTitlePopup.open()
        pass

    def changePostTitle(self, *args):
        #args[0].background_color = ''
        #self.postTitlePopup.open()
        pass

    def confirmPreTitle(self, *args):
        args[0].background_color = ''
        self.preTitleLabel.text = self.preTitleNameInput.text
        config.general['pretitle'] = self.preTitleNameInput.text
        self.preTitlePopup.dismiss()

    def confirmPostTitle(self, *args):
        args[0].background_color = ''
        self.postTitleLabel.text = self.postTitleNameInput.text
        config.general['posttitle'] = self.postTitleNameInput.text
        self.postTitlePopup.dismiss()

    def releaseLoad(self, *args):
         self.savesPopup.open()
         args[0].background_color = accent1

    def choseGameToLoad(self, *args):
        args[0].background_color = accent1
        title = args[0].game
        config.curr_game_dir = title
        self.savesPopup.dismiss()
        self.releaseStart()

    def choseModuleToLoad(self, *args):
        args[0].background_color = accent1
        title = args[0].module
        config.curr_module = title
        self.modulesPopup.dismiss()
        self.newModGamePopup.open()

    def newGame(self, *args):
        args[0].background_color = accent1
        self.newGamePopup.open()

    def makeNewGame(self, *args):
        args[0].background_color = accent1
        folder_name = self.newGameNameInput.text
        if folder_name == "":
            self.newGamePopup.dismiss()

        try:
            newpath = '.' + os.sep + 'saves' + os.sep + folder_name + os.sep
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            else:
                self.newGameStatus.text = "Folder exists."
                return

            f = file(newpath + "main.txt", "w")
            f = file(newpath + "main_status.txt", "w")
            f = file(newpath + "threads.txt", "w")
            f = file(newpath + "threads_status.txt", "w")
            f = file(newpath + "actors.txt", "w")
            f = file(newpath + "actors_status.txt", "w")
            f = file(newpath + "config.txt", "w")
            f = file(newpath + "tracks.txt", "w")
            f = file(newpath + "pcs.txt", "w")

            config.curr_game_dir = newpath

            saveconfig(self, config.curr_game_dir)

        except:

            print("[makeNewGame] Couldn't make a new directory for some reason.")

        self.newGamePopup.dismiss()
        self.releaseStart()

    def newGameModule(self, *args):
        args[0].background_color = accent1
        self.modulesPopup.open()

    def makeNewModGame(self, *args):

        args[0].background_color = accent1
        folder_name = self.newModGameNameInput.text
        if folder_name == "":
            self.newModGamePopup.dismiss()

        #try:
        newpath = '.' + os.sep + 'saves' + os.sep + folder_name + os.sep
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        else:
            self.newModGameStatus.text = "Folder exists."
            return

        fileList = [ "main.txt", "main_status.txt", "threads.txt", "threads_status.txt", "actors.txt", "actors_status.txt", "tracks.txt", "pcs.txt", "adventure.txt", "modlogic.py", "modpanel.py" ]

        config.curr_game_dir = newpath

        for item in fileList:
            f = file(newpath + item, "w")
            try:
                with open(config.curr_module + item) as fi:
                    lines = fi.readlines()
                    with open(newpath + item, "w") as fum:
                        fum.writelines(lines)
            except:
                pass

        # now parse the config and save as a config
        mod = config.curr_module + "modconfig.py"
        filename = mod.split('/')[-1]
        pyfile = filename.split('.')[0]
        modconfig = imp.load_source( pyfile, mod)

        tempDict = {}
        tempDict['general'] = config.general
        tempDict['user'] = config.user
        tempDict['module'] = modconfig.modvar
        with open(newpath + 'config.txt', "w") as fum:
            json.dump(tempDict, fum)

        loadconfig(self, config.curr_game_dir)

        #except:
        #    print("[makeNewModGame] Couldn't make a new directory for some reason.")

        self.newModGamePopup.dismiss()
        self.releaseStart()

    def pressGenericButton(self, *args):
        args[0].background_color = accent2

class OracleApp(App):

    def build(self):

        self.title = 'Pythia-Oracle'

        #Window.clearcolor = (1, 1, 1, 1)

        # define colors used in style.kv here; is there a way to change this without restart?
        self.accent1_r = accent1[0]
        self.accent1_g = accent1[1]
        self.accent1_b = accent1[2]

        self.basefontsize = config.general['basefontsize']

        self.textcolor = styles.textcolor

        screenmanager = ScreenManager()
        screenmanager.transition = SlideTransition(duration=1, clearcolor=(primary[0], primary[1], primary[2], 1), direction="left")
        titlescn = TitleScreen(name='titlescn')
        mainscn = MainScreen(name='mainscn')
        screenmanager.add_widget(titlescn)
        screenmanager.add_widget(mainscn)

        #return Builder.load_string(kv)

        return screenmanager

    def on_start(self):
        #print("APP STARTING")
        #makeBackup()
        pass

    def on_stop(self):
        #print("APP STOPPING")
        quicksave(self, config.curr_game_dir)
        pass

if __name__ == '__main__':
    OracleApp().run()
