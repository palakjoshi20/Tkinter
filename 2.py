from tkinter import *
root=Tk()
# def func():
#     print("Hello World")
# def func2():
#     print("BYe World")
def func():
    f=open("palak.txt","w")
    f.write("Hello World")

root.geometry("800x600")
f1=Frame(root,bg="pink",borderwidth=5,relief=GROOVE)
f1.pack(side=LEFT,fill=Y)
b1=Button(f1,fg="black",text="print now",command=func)
b1.pack(side=LEFT)

# b2=Button(f1,fg="black",text="print now",command=func2)
# b2.pack(side=RIGHT)

root.mainloop()

































































































































