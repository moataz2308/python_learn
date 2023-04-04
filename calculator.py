from tkinter import *
window = Tk()
window.title("Calculate your number")
window.geometry('400x200')
num1=StringVar()
num2=StringVar()
resultVar=StringVar()
u_first_num=Entry(window,bg="blue",fg="white",font="arial",width=15,text='1 ',borderwidth=2, relief="groove")
u_first_num.pack() 



btn2=Button(window,bg="red",width=1,text="1", font= "arial")
btn2.pack()
btn2.place(x=25, y=-30)


btn3=Button(window,bg="red",width=1,text="2", font= "arial")    
btn3.pack()
btn3.place(x=25, y=-60)



btn=Button(window,bg="red",width=1,text="3", font= "arial")    
btn.pack()   
btn.place(x=25, y=90)



btn=Button(window,bg="red",width=1,text="4", font= "arial")    
btn.pack()   
btn.place(x=25, y=120)

btn=Button(window,bg="red",width=1,text="5", font= "arial")    
btn.pack()   
btn.place(x=25, y=150)

btn=Button(window,bg="red",width=1,text="6", font= "arial")    
btn.pack()   

btn.place(x=25, y=180)

btn=Button(window,bg="red",width=1,text="7", font= "arial")    
btn.pack()   

btn.place(x=25, y=210)

btn=Button(window,bg="red",width=1,text="8", font= "arial")    
btn.pack()   

btn.place(x=25, y=240)

btn=Button(window,bg="red",width=1,text="9", font= "arial")    
btn.pack()   

btn.place(x=25, y=270)


btn=Button(window,bg="red",width=1,text="0", font= "arial")    
btn.pack()   

btn.place(x=25, y=300)

btn=Button(window,bg="red",width=1,text="1", font= "arial")    
btn.pack()   

btn.place(x=25, y=330)

btn=Button(window,bg="red",width=1,text="2", font= "arial")    
btn.pack()   

btn.place(x=25, y=360)

btn=Button(window,bg="red",width=1,text="=", font= "arial")
btn.pack()

btn.place(x=102, y=220)

btn=Button(window,bg="red",width=1,text="+", font= "arial")
btn.pack()

btn.place(x=102, y=250)

btn=Button(window,bg="red",width=1,text="-", font= "arial")
btn.pack()

btn.place(x=102, y=280)

btn=Button(window,bg="red",width=1,text=".", font= "arial")
btn.pack()

btn.place(x=102, y=310)

btn=Button(window,bg="red",width=1,text="/", font= "arial")
btn.pack()

btn.place(x=102, y=330)

btn=Button(window,bg="red",width=1,text="AC", font= "arial")
btn.pack()

btn.place(x=102, y=360)


labeleage=Label(window,bg="grey",fg="yellow",font="arial",width="30", textvariable= resultVar)
labeleage.pack()
window.mainloop() 