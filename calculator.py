from tkinter import *
window = Tk()
window.title("Calculate your number")
window.geometry('400x200')
num1=StringVar()
num2=StringVar()
resultVar=StringVar()
u_first_num=Entry(window,bg="blue",fg="white",font="arial",width=15,text='1 ',borderwidth=2, relief="groove")
u_first_num.pack()
u_second_num=Entry(window,bg="blue",fg="white",font="arial",width=15,text='2 ',borderwidth=2, relief="groove")
u_second_num.pack()
u_third_num=Entry(window,bg="blue",fg="white",font="arial",width=15,text='3 ',borderwidth=2, relief="groove")
u_third_num.pack()
u_fourth_num=Entry(window,bg="blue",fg="white",font="arial",width=15,text='4',borderwidth=2, relief="groove")
u_fourth_num.pack()


def printsum():
    uFirst=u_first_num.get()
    uSecond=u_second_num.get()
    num2=int(uSecond)
    num1=int(uFirst)
    result=num1+num2
    resultVar.set(result)
btn=Button(window,bg="red",width=1,text="+", font= "arial",command=printsum)
btn.pack()
def printsub():
    uFirst=u_first_num.get()
    uSecond=u_second_num.get()
    num2=int(uSecond)
    num1=int(uFirst)
    result=num1-num2
    resultVar.set(result)
btn=Button(window,bg="red",width=1,text="-", font= "arial",command=printsub)
btn.pack()
def printmul():
    uFirst=u_first_num.get()
    uSecond=u_second_num.get()
    num2=int(uSecond)
    num1=int(uFirst)
    result=num1*num2
    resultVar.set(result)
btn=Button(window,bg="red",width=1,text="*", font= "arial",command=printmul)    
btn.pack()
def printdiv():
    uFirst=u_first_num.get()
    uSecond=u_second_num.get()
    num2=int(uSecond)
    num1=int(uFirst)
    result=num1/num2
    resultVar.set(result)
btn=Button(window,bg="red",width=1,text="/", font= "arial",command=printdiv)    
btn.pack()   
labeleage=Label(window,bg="grey",fg="yellow",font="arial",width="30", textvariable= resultVar)
labeleage.pack()
window.mainloop()