from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.title("learn with codemy.com")
root.iconbitmap('/Users/passant/Moataz/game-boy.ico')
my_img=ImageTk.PhotoImage(Image.open('/Users/passant/Moataz/game-boy.png'))
my_label=Label(image=my_img)
my_label.pack()



button_quit=Button(root,text="exit programm",command=root.quit)
button_quit.pack()


root.mainloop
