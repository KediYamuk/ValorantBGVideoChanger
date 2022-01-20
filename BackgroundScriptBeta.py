import os, sys, shutil

print('Reminder: the "pathdatabase" files are a part of this script.')

def checkVariable():
    global pathvid
    global defined
    global valorantvideo
    try:
        dbr0 = open("pathdatabase.txt", "r+") 
        dbr1 = open("pathdatabase1.txt", "r+")
        pathvid = dbr0.read()
        valorantvideo = dbr1.read()

        pathvid = pathvid.replace('"',"")
        valorantvideo = valorantvideo.replace('"',"")

        dbr0.close()
        dbr1.close()
                
        defined = True
    except:
        defined = False
    #get pathvid from file

def definePath():
    global pathvid
    global defined
    global valorantvideo
    print("Please paste the full path of the video you want to see in the Valorant main menu below.")
    pathvid = input()

 
    db = open("pathdatabase.txt", "w+")
    db.write(pathvid)
    db.close()
    #stores the path to user vid in pathdatabase.txt
 
def defineValPath():
    global pathvid
    global defined
    global valorantvideo
    print("Please paste the full path of the Valorant's original background video. Read README.txt for more information.")
    valorantvideo = input()

    db1 = open("pathdatabase1.txt", "w+")
    db1.write(valorantvideo)
    db1.close()
    #stores the path to user original valorant video in pathdatabase1.txt

def preScript():
    global pathvid
    global defined
    global valorantvideo
    if defined == False:
        definePath()
        defineValPath()
        checkVariable()



#actual script:

checkVariable()
preScript()


choicecompleted = False
if defined == True:
    while choicecompleted == False:

        print("What do you want to do?\nType 2 if you want to change the path to the Valorant background file.\nType 1 if you want to change the path to the replacement background video.\nType 0 if you want to execute the script and quit.\nType 9 if you want to quit without exectuting the script.")
        userinputchoice = input()

        if userinputchoice == "0":
            shutil.copyfile(pathvid, valorantvideo)
            choicecompleted = True
    
        elif userinputchoice == "1":
            definePath()
            choicecompleted = False

        elif userinputchoice == "2":
            defineValPath()
            choicecompleted = False

        elif userinputchoice == "9":
            exit()

        else:
            choicecompleted = False
            print("You entered an invalid number!")


else:
    print("Something went wrong.")
    os.system("pause")