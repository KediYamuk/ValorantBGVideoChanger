import os, sys, shutil

print('Reminder: the "pathdatabase" files are a part of this script.')

def getVariable():
    global pathvid
    global defined
    global valorantvideo
    try:
        #read video path from file
        dbr0 = open("pathdatabase.txt", "r+") 
        dbr1 = open("pathdatabase1.txt", "r+")
        pathvid = dbr0.read()
        valorantvideo = dbr1.read()

        #remove quotation marks
        pathvid = pathvid.replace('"',"")
        valorantvideo = valorantvideo.replace('"',"")

        dbr0.close()
        dbr1.close()
                
        defined = True
    except:
        defined = False

def definePath():
    global pathvid
    print("Please paste the full path of the video you want to see in the Valorant main menu below.")
    pathvid = input()

    #write custom vid path into file
    db = open("pathdatabase.txt", "w+")
    db.write(pathvid)
    print("Path saved.")
    db.close()
 
def defineValPath():
    global valorantvideo
    print("Please paste the full path of the Valorant's original background video. Read README.md for more information.")
    valorantvideo = input()

    #write original vid path into file
    db1 = open("pathdatabase1.txt", "w+")
    db1.write(valorantvideo)
    print("Path saved.")
    db1.close()


def preScript():
        definePath()
        defineValPath()
        getVariable()


#actual script:

getVariable()
while defined == False:
    preScript()

print("Path read from file succesfully.")

choicecompleted = False
if defined == True:
    while choicecompleted == False:

        print("What do you want to do?\nType 2 if you want to change the path to the original background video file.\nType 1 if you want to change the path to the replacement background video file.\nType 0 if you want to execute the script and quit.\nType 9 if you want to quit without exectuting the script.")
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
