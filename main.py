from tkinter import *

root=Tk()#object
root.geometry("900x500")#wxh
root.minsize(300,100)
root.maxsize(1200,900)

text=Label(text="This is tkinter class")
text.pack()#all labels will be packed
photo=PhotoImage(file="Doraemon-PNG-HD.png")#for png image
label=Label(image=photo)
label.pack()
root.iconbitmap("./iso_20225.ico")



# from PIL import Image, ImageTk  #for jpg image
# root.title("hello")
# image=Image.open("website.jpg")
# photo=ImageTk.PhotoImage(image)
# label=Label(image=photo)
# label.pack()
# root.mainloop()  #last pe rhega



# label=Label(text=''' HI,My name is Palak \n HI,My name is Palak \n HI,My name is Palak
# \n HI,My name is Palak \n HI,My name is Palak \n HI,My name is Palak \n
# HI,My name is Palak \n HI,My name is Palak \n HI,My name is Palak \n''',
# bg="pink",fg="white",padx=113,pady=100,font="Constantia 20 bold",borderwidth=10,relief=GROOVE)#sunken,ridge,raised
# # label.pack(anchor="nw")#ne
# label.pack(side=LEFT,fill=Y)



# f1=Frame(root,bg="pink",borderwidth=5,relief=GROOVE)
# f1.pack(side=LEFT,fill=Y)
# f2=Frame(root,bg="blue",borderwidth=5,relief=GROOVE)
# f2.pack(side=TOP,fill=X)
# l=Label(f1,text="Hello Tkinter")
# l.pack(pady=150)
# l=Label(f2,text="This is the main project",font="Castellar 17 bold",fg="black")
# l.pack(pady=100)



# name="Duggu"
# age=20
# print(f"My name is {name} and my age is {age}")
#
#
#
# canvas_width=800
# canvas_height=400
# root.geometry(f"{canvas_width}x{canvas_height}")
#
root.mainloop()