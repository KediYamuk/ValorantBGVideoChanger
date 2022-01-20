import os, sys

print('Reminder: the "pathdatabase" file in the parent directory of this directory is a part of this script.')

def checkVariable():
    global pathvid
    global defined
    try:
        with open("..\..\pathdatabase.txt", "r") as db:
            pathvid = read.db()
            defined = True
    except:
        defined = False
    #get pathvid from file

def openRiot():
    global pathvid
    global defined
    try:
        os.startfile("RiotClientServices.exe")

    except FileNotFoundError:
        print("You need to put this file into the Riot Client Folder. Read README.txt for more info.")
        os.system("pause")
    #lauches riot client

def definePath():
    global pathvid
    global defined
    print("Please paste the full path of the DIRECTORY of the video you want to replace the Valorant background video with below (dont put an extra \ pls).")
    pathvidfoldera = input()
    pathvidfolder = pathvidfoldera.decode('unicode_escape')
    print("Paste the video name below. (with the extention included)") 
    vidnamea = input()
    os.system("cd C:/")
    os.rename('"' + pathvidfolder + "\\" + vidname + '"' , '"' + pathvidfolder + "\\HomeScreen" + '"')
    pathvid = pathvidfolder + "\HomeScreen"

    #THIS IS SO AWFUL I HATE MYSELF FOR DOING THISJSDHFLYJHSGFS

    try:
        with open("..\..\pathdatabase.txt", "x") as db0:
            db0.close()
    except:
        print("SOMETHING WENT WRONG WHILE SAVING THE PATH TO THE DATABASE")
    with open("..\..\pathdatabase.txt", "w") as db:
        db.write(pathvid)
        db.close()
    #(re)defining variable

#actual script:

checkVariable()

if defined == True:

    print("What do you want to do? Type 1 if you want to change the path to the background video. Type 2 if you want to execute the script.")
    userinputchoice = input()

    if userinputchoice == "2":
        openRiot()
        os.system('copy /s /y  "'+ pathvid +'"  "..\VALORANT\live\ShooterGame\Content\Movies\Menu\HomeScreen.mp4" ')
    
    if userinputchoice == "1":
        definePath()

    else:
        print("You entered an invalid number! Please run the script again.")
        #PUT AN EXCEPTION HERE DUMBASS
        os.system("pause")


if defined == False:
    definePath()