for i in range(1):
    from tkinter import *
    import sys

    root = Tk()

    xyz = 0

    list_1 = [
        "Rushil",
        "Purva",
        "Prafulla",
        "Aanya"
    ]

    fgh = ("Enter a username if name not in list:-",list_1)

    names_lbl1 = Label(root,text=fgh).grid(row=97,column=1)
    lbl3 = Label(root,text="or click NEXT").grid(row=99,column=1)
    lbl1 = Label(root,text=names_lbl1).grid(row=98,column=1)
    def next_screen():
        root.destroy()
    def new_user():
        new_user_terminal = input("ENTER YOUR USER HERE:- ")
        list_1.append(new_user_terminal)
        print("DONE ! ADDED NEW USER",list_1)
    b1 = Button(root,text="username not in list click here",command=new_user).grid(row=102,column=1)
    next_1 = Button(root,text="NEXT",command=next_screen).grid(row=101,column=1)
    

    root.mainloop()

    root_2 = Tk()

    clicked1 = StringVar()
    clicked1.set("Rushil")
    root_3 = Tk()
    grade = OptionMenu(root_2,clicked1,*list_1)
    grade.grid(row=20,column=1)
    global chat
    chat = Entry(root_2,width=40 ,borderwidth=5)
    chat.grid(row=20,column=2)
    phto = PhotoImage(file="C:\\Users\\rushil\\Pictures\\Camera Roll\\Pika.png")
    clckd = clicked1.get()
    def send():
        global entry
        global entry_name
        entry = str(chat.get())
        entry_name = str(clicked1.get())
        entry_final = ("|"+str(entry_name)+"|:-"+str(entry))
        B = Label(root_3,text=entry_final).pack()


    send = Button(root_2,image=phto,command=send).grid(row=20,column=3)

    root_2.mainloop()
    root_3.mainloop()