import tkinter
from tkinter import *

def openTaskFile():
    try:
        global task_list
        with open('taskList.txt','r') as taskFile:
            tasks = taskFile.readlines()
            for task in tasks:
                if task != '\n':
                    task_list.append(task)
                    listBox.insert(END,task)
    except:
        file = open('taskList.txt','w')
        file.close()

def addTask():
    global task_list
    task = task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open('taskList.txt','a') as taskFile:
            taskFile.write(f"\n{task}")
        task_list.append(task)
        listBox.insert(END,task)

def deleteTask():
    global task_list
    task = str(listBox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('taskList.txt','w') as taskFile:
            for tas in task_list:
                taskFile.write(tas+'\n')
        listBox.delete(ANCHOR)

root = Tk()
root.title("To Do List")
iconTitle = PhotoImage(file='image/task.png')
root.iconphoto(False,iconTitle)
root.geometry('400x650+1300+100')
root.resizable(False,False)

task_list = []

topBg = PhotoImage(file='image/topbar.png')
Label(root,image=topBg).pack()
topDock = PhotoImage(file='image/dock.png')
Label(root, image=topDock,bg='#32405B').place(x = 30, y = 25)
topIcon = PhotoImage(file='image/task.png')
Label(root, image=topIcon,bg='#32405B').place(x = 340, y = 21)
heading = Label(root, text = 'ALL TASK',font='arial 20 bold',fg='white',bg='#32405B')
heading.place(x = 130, y = 21)

frame = Frame(root, width=400,height=50,bg='white')
frame.place(x = 0, y = 180)
task = StringVar()
task_entry = Entry(frame, width=18, font='arial 20',bd=0)
task_entry.place(x = 10, y = 7)
task_entry.focus()

buttonAdd = Button(frame, text='ADD',font='arial 20 bold',width=6, bg='#5A95FF',fg='#FFF',bd=0,command=addTask)
buttonAdd.place(x=300,y=0)

frameList = Frame(root, width=700, height=280,bd=3,bg='#32405B' )
frameList.pack(pady=(160,0)) #what is 0
listBox = Listbox(frameList, font='arial 12',width=40,height=16,bg='#32405B',fg='white',cursor='hand2',selectbackground='#5A95FF')
listBox.pack(side=LEFT,fill=BOTH,padx=2)
scrollBar = Scrollbar(frameList)
scrollBar.pack(side=RIGHT,fill=BOTH)
listBox.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=listBox.yview)

openTaskFile()

deleteIcon = PhotoImage(file='image/delete.png')
buttonDel = Button(root, image=deleteIcon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()