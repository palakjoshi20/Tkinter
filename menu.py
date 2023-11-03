from tkinter import *
root=Tk()
root.geometry("800x800")
def func():
    print("Hey Duggu")
filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="File",command=func)
m1.add_command(label="Save",command=func)
m1.add_separator()
m1.add_command(label="Save as",command=func)
m1.add_command(label="Print",command=func)
root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)


m2=Menu(filemenu)
m2=Menu(filemenu,tearoff=0)
m2.add_command(label="File",command=func)
m2.add_command(label="Save",command=func)
m2.add_separator()
m2.add_command(label="Save as",command=func)
m2.add_command(label="Print",command=func)
root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m2)

root.mainloop()



