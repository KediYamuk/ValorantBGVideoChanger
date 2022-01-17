import os, sys, subprocess

def checkVariable():
    pass
    #reading txt file to check if pathvid is defined
    #if defined:
    #defined = True
    #if not
    #defined = False

def callVariable():
    pass
    #grabbing pathvid from txt file

def openRiot():
    try:
        os.startfile("RiotClientServices.exe")

    except FileNotFoundError:
        print("You need to put this file into the Riot Client Folder. Read README.txt for more info.")
        os.system("pause")

def definePath():
    print("Please paste the full path to the video below.")
    pathvid = input()
    #(re)defining variable

checkVariable()

defined = True
if defined == True:

    print("What do you want to do? Type 1 if you want to change the path to the background video. Type 2 if you want to execute the script.")
    userinputchoice = input()

    if userinputchoice == "2":
        pass
#        openRiot()
#        code to replace valorant bgv with user bgv (ACTUAL SCRIPT)
    
    if userinputchoice == "1":
        pass
#        definePath()

    else:
        print("You entered an invalid number! Please run the script again. (Will be fixed in a further patch.)")
        os.system("pause")


if defined == False:
    definePath()