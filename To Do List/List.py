import tkinter as tk
from tkinter import *
root=Tk()
root.title("Code Soft To-Do-List")
root.geometry("400x650+450+30")
root.resizable(width=False, height=False)


task_list=[]

# Function for Adding Task in To Do List
def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert  (END,task)


# Function for Deleting Task in To Do List
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")

        listbox.delete(ANCHOR)



# Function for UPdating Task in To Do List
def updateTask():
    selected_index = listbox.curselection()
    if selected_index:
        updated_task = task_entry.get()
        
        if updated_task:
            listbox.delete(selected_index)
            listbox.insert(selected_index, updated_task)
            task_list[selected_index[0]] = updated_task
            
            task_entry.delete(0, END)
            # Update the tasklist.txt file
            with open("tasklist.txt", "w") as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")

    

def openTaskFile():
    try:

        with open("tasklist.txt","r")as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)

    except:
        file=open('tasklist.txt','w')
        file.close()

#icon
Image_icon=PhotoImage(file="mainlogo.png")
root.iconphoto(False,Image_icon)


#top bar
TopImage=PhotoImage(file="topBar.png")
Label(root, image=TopImage).pack()

dockImage=PhotoImage(file="dock.png")
Label(root,image=dockImage,bg="#006D77").place(x=30,y=25)

noteImage=PhotoImage(file="tasklogo.png")
Label(root,image=noteImage,bg="#006D77").place(x=340,y=20)

heading=Label(root,text="To Do List", font="arial 20 bold",fg="white", bg="#006D77")
heading.place(x=130,y=20)

#main
frame=Frame(root,width=400, height=500, bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

#Add
def addButton_enter(event):
    button.config(image=Addhover_image)

def addButton_leave(event):
    button.config(image=Addnormal_image)


Addnormal_image = tk.PhotoImage(file="add1.png")
Addhover_image = tk.PhotoImage(file="add2.png")

button=Button(frame, image=Addnormal_image, bg="white", bd=0,cursor="hand2", command=addTask)
button.place(x=330,y=0)
button.bind("<Enter>",addButton_enter)
button.bind("<Leave>",addButton_leave)



#listbox
frame1=Frame(root,bd=3,width=700, height=200, bg="#006d77")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial',12),width=40, height=15, bg="#006d77", fg="white", cursor="hand2", selectbackground="#83C5BE", selectforeground="black")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
openTaskFile()


#delete

def delButton_enter(event):
    delButton.config(image=Delhover_image)

def delButton_leave(event):
    delButton.config(image=Delnormal_image)


Delnormal_image = tk.PhotoImage(file="del1.png")
Delhover_image = tk.PhotoImage(file="del2.png")

delButton=Button(root,image=Delnormal_image,bg="white",text="Delete",font=('arial',10),fg="#006D77",compound="top",bd=0,cursor="hand2", command=deleteTask)
delButton.place(x=235,y=560)
delButton.bind("<Enter>", delButton_enter)
delButton.bind("<Leave>", delButton_leave)


#update 

# Hover Property for button
def Updateon_enter(event):
    upButton.config(image=Uphover_image)

def Updateon_leave(event):
    upButton.config(image=Upnormal_image)


Upnormal_image = tk.PhotoImage(file="update.png")
Uphover_image = tk.PhotoImage(file="updatehov.png")

upButton=Button(root,image=Upnormal_image,bg="white",text="Update",font=('arial',10),fg="#006D77",compound="top",bd=0, cursor="hand2", command=updateTask)
upButton.place(x=100,y=560)
upButton.bind("<Enter>", Updateon_enter)
upButton.bind("<Leave>", Updateon_leave)

root.mainloop()