from datetime import datetime, timedelta
from os import system
from pynput import keyboard

tabCount = 0
totalTime = timedelta(milliseconds = 0)
t1 = 0
t0 = 0
resetFlag = False

initialTime = datetime.now()

def showTabCount(tabCount): 
    system("cls")
    print("Number of times TAB has been pressed since", str(initialTime)[:-7] + ":")
    print(tabCount)
    print("Total time tab was held for:")
    print(totalTime)
    elementarySchoolThing(tabCount)
    if tabCount > 99999:
        print("You somehow managed to go over 100 000 tab presses, please get help.")
    #graphicalRepresentation(tabCount)

def elementarySchoolThing(tabCount):
    print("")
    print("10000s :", "◼ "*(tabCount // 10000))
    print("1000s  :", "◼ "*(tabCount // 1000 - tabCount // 10000 * 10))
    print("100s   :", "◼ "*(tabCount // 100 - tabCount // 1000 * 10))
    print("10s    :", "◼ "*(tabCount // 10 - tabCount // 100 * 10))
    print("1s     :", "◼ "*(tabCount // 1 - tabCount // 10 * 10))

"""def graphicalRepresentation(tabCount):
    charactersPerLine = 50
    lines = tabCount // charactersPerLine
    charLastLine = tabCount % charactersPerLine

    print("\n")
    for i in range(0,lines):
        print("◼ "*charactersPerLine)
    print("◼ "*charLastLine)"""

def OnTabPress(key):
    if key == keyboard.Key.tab:
        global resetFlag
        global t1

        if resetFlag == False:
            resetFlag = True
            t1 = datetime.now()
        return

def OnTabRelease(key):
    if key == keyboard.Key.tab:
        global tabCount
        global resetFlag
        global totalTime

        resetFlag = False
        t2 = datetime.now()
        totalTime += t2-t1
        tabCount += 1
        showTabCount(tabCount)

while True:
    with keyboard.Listener(on_press=OnTabPress, on_release=OnTabRelease) as listener:
        listener.join()