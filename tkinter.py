from tkinter import *
window = Tk()
window.title("Calculate your age")
window.geometry('400x200')
user_name=StringVar()
user_age=StringVar()
user_name=Label(window,bg="blue",fg="white",font="arial",width=15,text='enter name ',borderwidth=2, relief="groove")
user_name.pack()
user_name=Entry(window,bg="green",width=20,font="arial")
user_name.pack()
def printName_age():
    uName=user_name.get()
    ubyear=u_byear.get()
    age=2023-int(ubyear)
    user_name.set("welcome " +uName+" your age is ") 
    user_age.set(age)
btn=Button(window,bg="red",width=5,text="enter", font= "arial",command=printName_age)
btn.pack()
labelname=Label(window,bg="grey",fg="yellow",font="arial",width="20", textvariable= user_age)
labelname.pack()
labeleage=Label(window,bg="grey",fg="yellow",font="arial",width="20", textvariable= user_name)

labeleage.pack()
window.mainloop()
