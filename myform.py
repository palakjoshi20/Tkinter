from tkinter import *
root=Tk()
def getvalues():
      print(uservalue.get())
      print(passvalue.get())
      f=open("bobby.txt","a")
      f.write(uservalue.get() + "\n")
      f.write(passvalue.get() +"\n")

text=Label(text="Registration Form")
text.pack()
name=Label(root,text="Username")
rno=Label(root,text="Password")
root.geometry("800x600")
name.grid(row=0,column=1)#grid also works to pack label
rno.grid(row=1,column=1)
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=2)
passentry.grid(row=1,column=2)
Button(text="Submit",command=getvalues).grid(row=2,column=1)



root.mainloop()