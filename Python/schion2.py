from tkinter import*
root=Tk()
e=Entry(root,width=50)
e.pack()
e.insert(0,"enter your name:")



def myclick():
    hello= "Hello"+ e.get()
    Mylabel=Label(root,text="hello")
    Mylabel.pack()
mybutton=Button(root,text="enter your name",command=myclick)
mybutton.pack()   


root.mainloop()