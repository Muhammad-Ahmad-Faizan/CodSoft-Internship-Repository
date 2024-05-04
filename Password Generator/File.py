from tkinter import *
import random
import string

root = Tk()
root.geometry("400x280+500+200")
root.title("Password Generator")
root.resizable(width=False, height=False)

#icon
Image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,Image_icon)

choice = IntVar()

def set_selection():
    pass

R1 = Radiobutton(root, text="POOR", fg="blue",variable=choice, value=1, command=set_selection)
R1.pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE",fg="green", variable=choice, value=2, command=set_selection)
R2.pack(anchor=CENTER)
R3 = Radiobutton(root, text="STRONG", fg="red",variable=choice, value=3, command=set_selection)
R3.pack(anchor=CENTER)

labelChoice = Label(root)
labelChoice.pack()

lenLabel = StringVar()
lenLabel.set("Password Length")
lentitle = Label(root, textvariable=lenLabel)
lentitle.pack()

val = IntVar()
spinlength = Spinbox(root, from_=8, to=24, textvariable=val, fg="green",width=13)
spinlength.pack()

def callback():
    password = passgen()
    Isum.config(text=password)

passgenButton = Button(root, text="Generate Password", bd=5, bg="black",fg="white",height=2, command=callback, pady=3)
passgenButton.pack()

Isum = Label(root, text="",fg="purple",font=30)
Isum.pack(side=BOTTOM)

# logic
poor = string.ascii_uppercase + string.ascii_lowercase
average = string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = "'''`~!@#$%^&*()_-+={}[]\|;:'''<>,.?/''"
advanced = poor + average + symbols

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advanced, val.get()))

root.mainloop()
