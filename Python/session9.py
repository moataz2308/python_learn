from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.title("learn with codemy.com")
root.iconbitmap('/Users/passant/Moataz/game-boy.ico')
my_img1=ImageTk.PhotoImage(Image.open('/Users/passant/Moataz/game-boy.png'))
my_img2=ImageTk.PhotoImage(Image.open('/Users/passant/Moataz/game-boy.png'))
my_img3=ImageTk.PhotoImage(Image.open('/Users/passant/Moataz/game-boy.png'))
my_img4=ImageTk.PhotoImage(Image.open('/Users/passant/Moataz/game-boy.png'))

image_list=[my_img1,my_img2,my_img3,my_img4]



my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forword(image_number):
    
    global my_label
    global button_forword
    global button_back


    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forword=Button(root,text=">>",command=lambda: forword(image_number+1))
    button_back=Button(root,text="<<",command=lambda: back(image_number-1))
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1 ,column=0)
    button_forword.grid(row= 1,column=2)

    if image_number== 5:
        button_forword=Button(root,text=">>",state=DISABLED)


def back():
    global my_label
    global button_forword
    global button_back

    button_back=Button(root,text="<<",command=back)
    button_exit=Button(root,text="EXIT PROGRAM",command=root.exit)
    button_forword=Button(root,text=">>",command=lambda:forword(2))

    button_back.grid(row=1 ,column=0)
    button_exit.grid(row= 1,column=1)
    button_forword.grid(row= 1,column=2)
    



root.mainloop()
