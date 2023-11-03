from tkinter import *
import tkinter.messagebox as msg
root=Tk()
root.geometry("800x800")
def func():
    print("This is Python")
def help():
    print("ya sure")
    #msg.showinfo("Heading","We are more than happy to help u")#("heading","shown text")
def rate():
    v=msg.askquestion("Heading","Do you liked our app")
    if v=="yes":
        print("rate us on playstore")
    else:
        msg.showinfo("hello",)

filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="File",command=rate)
m1.add_command(label="Save",command=func)
m1.add_separator()
m1.add_command(label="Save as",command=func)
m1.add_command(label="Print",command=help)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)
root.mainloop()