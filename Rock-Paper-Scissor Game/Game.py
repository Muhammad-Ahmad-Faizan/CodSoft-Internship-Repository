from tkinter import *
from PIL import Image, ImageTk
from  random import randint

#main window 
root=Tk()
root.title("Rock Scissor Paper")
root.configure(background="black")
root.resizable(width=False, height=False)

#icon
Image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,Image_icon)

#picture
rockU=ImageTk.PhotoImage(Image.open("UserRock.png"))
paperU=ImageTk.PhotoImage(Image.open("UserPaper.png"))
scissorU=ImageTk.PhotoImage(Image.open("UserScissor.png"))
rockC=ImageTk.PhotoImage(Image.open("CompRock.png"))
paperC=ImageTk.PhotoImage(Image.open("CompPaper.png"))
scissorC=ImageTk.PhotoImage(Image.open("CompScissor.png"))

#insert Picture
userLabel=Label(root,image=rockU, bg="black")
compLabel=Label(root,image=rockC, bg="black")
userLabel.grid(row=1,column=4)
compLabel.grid(row=1,column=0)

#Scores
playerScore=Label(root, text=0, font=100, bg="black", fg="white")
computerScore=Label(root, text=0, font=100, bg="black", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)


#indicators
userIndicator=Label(root,font=50,text="USER", bg="black", fg="white")
compIndicator=Label(root,font=50,text="COMPUTER", bg="black",fg="white")
userIndicator.grid(row=0,column=3)
compIndicator.grid(row=0,column=1)

#messages
msg=Label(root,font=50, bg="black", fg="white")
msg.grid(row=3, column=2)


#update message
def updateMessage(x):
    msg['text']=x  

#update the user score
def updateUserScore():
    score=int(playerScore["text"])
    score+=1
    playerScore["text"]=str(score)

#update computer score
def updateCompScore():
    score=int(computerScore["text"])
    score+=1
    computerScore["text"]=str(score)

#check Winner
def checkwin(player, computer):
    if player==computer:
        updateMessage("Its a tie!!!")
    elif player =="rock":
        if computer=="paper":
            updateMessage("You Loose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Loose!")
            updateCompScore()
        else:
            updateMessage("You Win!")
            updateUserScore()
    else:
        pass


#update choices
choices=["rock","paper","scissor"]
def  updateChoice(x):
#For Computer
    compChoice= choices[randint(0,2)]
    if compChoice=='rock':
        compLabel.configure(image=rockC)
    elif compChoice=='paper':
        compLabel.configure(image=paperC)
    else:
        compLabel.configure(image=scissorC)
#For user
    if x=='rock':
        userLabel.configure(image=rockU)
    elif x=='paper':
        userLabel.configure(image=paperU)
    else:
        userLabel.configure(image=scissorU)
    
    checkwin(x, compChoice)

#buttons
rock=Button(root,width=20, height=2, text="ROCK", bg="purple", fg="white",command=lambda:updateChoice("rock")).grid(row=2, column=1)
paper=Button(root,width=20, height=2, text="PAPER", bg="skyblue", fg="black",command=lambda:updateChoice("paper")).grid(row=2, column=2)
scissor=Button(root,width=20, height=2, text="SCISSOR", bg="yellow", fg="black",command=lambda:updateChoice("scissor")).grid(row=2, column=3)


root.mainloop()