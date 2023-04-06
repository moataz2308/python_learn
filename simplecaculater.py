from tkinter import*
root=Tk()
root.title("simple calculater")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)




def button_click():
    e.delete(0,END)
button_1=Button(root,text="1",padx=40,pady=20,command=button_click)
button_2=Button(root,text="2",padx=40,pady=20,command=button_click)
button_3=Button(root,text="3",padx=40,pady=20,command=button_click)
button_4=Button(root,text="4",padx=40,pady=20,command=button_click)
button_5=Button(root,text="5",padx=40,pady=20,command=button_click)
button_6=Button(root,text="6",padx=40,pady=20,command=button_click)
button_7=Button(root,text="7",padx=40,pady=20,command=button_click)
button_8=Button(root,text="8",padx=40,pady=20,command=button_click)
button_9=Button(root,text="9",padx=40,pady=20,command=button_click)
button_0=Button(root,text="0",padx=40,pady=20,command=button_click)
button_add=Button(root,text="1",padx=39,pady=20,command=button_click)
button_equal=Button(root,text="1",padx=91,pady=20,command=button_click)
button_clear=Button(root,text="1",padx=79,pady=20,command=button_click)
   

root.mainloop()