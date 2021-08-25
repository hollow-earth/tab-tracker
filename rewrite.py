from datetime import datetime, timedelta
from os import system
from pynput import keyboard

class CharacterCount:
    def elementarySchoolThing(self, tabCount):
        char = "o "
        print("")
        print("10000s :", char*(tabCount // 10000))
        print("1000s  :", char*(tabCount // 1000 - tabCount // 10000 * 10))
        print("100s   :", char*(tabCount // 100 - tabCount // 1000 * 10))
        print("10s    :", char*(tabCount // 10 - tabCount // 100 * 10))
        print("1s     :", char*(tabCount // 1 - tabCount // 10 * 10))

    def showTabCount(self, beginTime, totalTimePressed, tabCount): 
        system("cls")
        print("Number of times TAB has been pressed since", str(beginTime)[:-7] + ":")
        print(tabCount)
        print("Total time tab was held for:")
        print(totalTimePressed)
        if tabCount > 99999:
            print("You somehow managed to get over 100 000 tab presses, please get help.")

    def getTabCount(self):
        return tabCount

    #def getTime(self, t1, t2):
    #    return t1-t2

class KeyboardListen:
    def __init__(self):
        global tabCount
        self.t2 = 0
        self.t1 = 0
        self.timeHeld = 0
        self.tabCount = tabCount

    def OnTabPress(self):
        if self == keyboard.Key.tab:
            self.t2 = datetime.now()

    def OnTabRelease(self, timeNow):
        if self == keyboard.Key.tab:
            self.t1 = datetime.now()
            self.timeHeld = (self.t1 - self.t2)
            CharacterCount().showTabCount()

timeNow = datetime.now()
totalTime = timedelta(milliseconds = 0)
tabCount = 0

with keyboard.Listener(on_press=KeyboardListen.OnTabPress, on_release=KeyboardListen.OnTabRelease) as listener:
    listener.join()
    #totalTime += CharacterCount().getTime()

#while True:
#    CharacterCount(timeNow, tabCount).showTabCount()
#    CharacterCount(timeNow, tabCount).elementarySchoolThing(tabCount)