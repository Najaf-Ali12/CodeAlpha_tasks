from tkinter import *
import random
import tkinter.messagebox
root=Tk()
root.geometry("1350x760+0+0")
root.title("Number Puzzle Game")
root.configure(bg="Cadet Blue")
rootframe=Frame(root, bg="Cadet Blue", pady=2, padx=40, width=1350, height=100, relief="solid")
rootframe.grid(row=0, column=0)

lblTitle=Label(rootframe,font=("arial",80,"bold"),text="Number Puzzle Game",bd=10, bg="Cadet Blue",
                  fg="cornsilk", justify=CENTER, borderwidth=12, relief="solid", width=19)
lblTitle.grid(row=0, column=0)

Mainframe=Frame(root, bg="Cadet Blue", bd=10, width=1350, height=600, relief="solid")
Mainframe.grid(row=1, column=0,padx=30)

Buttonframe=LabelFrame(Mainframe,text="Number Puzzle ",font=("arial",12,"bold"),fg="cornsilk" ,
                  bg="Cadet Blue", bd=10, width=700, height=500, relief="solid")
Buttonframe.pack(side=LEFT)

Scoreframe=LabelFrame(Mainframe,text="Score Recorder",font=("arial",12,"bold"),fg="cornsilk",
                   bg="Cadet Blue", bd=10,padx=1, width=540, height=500, relief="solid")
Scoreframe.pack(side=RIGHT)

CountClickframe=Frame(Scoreframe,bg="Cadet Blue", bd=10,padx=10,pady=2, width=540, height=190, relief="solid")
CountClickframe.grid(row=0, column=0)

Winnerframe=Frame(Scoreframe,bg="Cadet Blue", bd=10,padx=10,pady=2, width=540, height=140, relief="solid")
Winnerframe.grid(row=1,column=0)

ResetExitframe=LabelFrame(Scoreframe,bg="Cadet Blue", bd=10,padx=10,pady=2, width=540, height=140, relief="solid")
ResetExitframe.grid(row=2,column=0)

clickcounter=0 
displayClicks=StringVar()
displayClicks.set("Total clicks"+"\n"+"0")
gameStateString=StringVar()

def UpdateCounter():
    global clickcounter,displayClicks
    displayClicks.set("Total clicks"+"\n"+str(clickcounter))
def gameStateUpdate(gameState):
    global gameStateString
    gameStateString.set(gameState)
class PuzzleButton:
    def __init__(self,text_,x,y):
        self.enterValue=text_
        self.txtIntake=StringVar()
        self.txtIntake.set(text_)
        self.x=x
        self.y=y
        self.btnNumber=Button(Buttonframe,textvariable=self.txtIntake,font=("arial",80),bd=5,
                              borderwidth=4, relief="solid",command=lambda i=self.x,j=self.y : emptySpotChecker(i,j))
        self.btnNumber.place(x=self.x*168,y=self.y*152, width=170, height=160) 

def shuffle():
    global clickcounter, btnCheckers
    nums=[]
    for x in range(12):
        x+=1
        if x==12:
            nums.append("")
        else:
            nums.append(str(x))
    for y in range(len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            num=random.choice(nums)
            btnCheckers[y][x].txtIntake.set(num)
            nums.remove(num)
    clickcounter=0
    UpdateCounter()
    gameStateUpdate("")
def iExit():
    iExit=tkinter.messagebox.askyesno("Number Puzzle","Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return
lblCountClicks=Label(CountClickframe,textvariable=displayClicks, borderwidth=4,relief="solid",
                    font=('Arial',40)).place(x=0, y=10,width=500,height=150)

lblwinner=Label(Winnerframe,textvariable=gameStateString, borderwidth=4,relief="solid",
                    font=('Arial',40)).place(x=0, y=10,width=500,height=100)

btnReset=Button(ResetExitframe,text="Reset", font=('Arial',40,"bold"), bd=5,borderwidth=4,relief="solid",
               command= shuffle).place(x=0,y=10,width=250,height=100)

btnExit=Button(ResetExitframe,text="Exit", font=('Arial',40,"bold"), bd=5,borderwidth=4,relief="solid",
               command=iExit).place(x=250,y=10,width=250,height=100)

btnCheckers=[]
name=0
for y in range(3):
    btnCheckers_=[]
    for x in range(4):
        name+=1
        if name ==12:
            name=" "
        btnCheckers_.append(PuzzleButton(str(name),x,y))
    btnCheckers.append(btnCheckers_)

shuffle()
#def emptySpotChecker(x,y):
#    global btnCheckers,clickcounter
#    if not btnCheckers[x][y].txtIntake.get()=="":
#        for i in range(-1,2):
#            newX=x+i
#            newX = max(0, min(len(btnCheckers)-1, newX))  # Limit newX to valid range
#            if btnCheckers[newX][y].txtIntake.get()=="":
#                    text=btnCheckers[x][y].txtIntake.get()
#                    btnCheckers[x][y].txtIntake.set(btnCheckers[newX][y].txtIntake.get())
#                    btnCheckers[newX][y].txtIntake.set(text)
#                    checkWinner()
#                    break
#        for j in range(-1,2):
#            newY=y+j
#            if not (newY<0 or len(btnCheckers[0])-1< newY or i==0):
#                if btnCheckers[x][newY].txtIntake.get()==" ":
#                    text=btnCheckers[x][y].txtIntake.get()
#                    btnCheckers[x][y].txtIntake.set(btnCheckers[x][newY].txtIntake.get())
#                    btnCheckers[x][newY].txtIntake.set(text)
#                    checkWinner()
#                    break
#    clickcounter+=1
#    UpdateCounter()
#
def emptySpotChecker(x, y):
    global btnCheckers, clickcounter

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(btnCheckers) and 0 <= new_y < len(btnCheckers[0]):
            if btnCheckers[new_x][new_y].txtIntake.get() == "":
                temp = btnCheckers[x][y].txtIntake.get()
                btnCheckers[x][y].txtIntake.set(btnCheckers[new_x][new_y].txtIntake.get())
                btnCheckers[new_x][new_y].txtIntake.set(temp)
                clickcounter += 1
                UpdateCounter()
                checkWinner()
                return

    clickcounter += 1
    UpdateCounter()



def checkWinner():
    lost=False
    for y in range (len(btnCheckers)):
        for x in range(len(btnCheckers[y])):
            if btnCheckers[y][x].enterValue != btnCheckers[y][x].txtIntake.get():
                lost=True
                break
            if not lost:
                gameStateUpdate("You are a winner!")
root.mainloop()
