from tkinter import *
root=Tk()
#Canvas
canvas_width=800
canvas_height=1200
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Bobby Bhaiya")
can=Canvas(root,width=canvas_width,height=canvas_height)
can.pack()
#can.create_line(100,100,200,300,fill="blue")#x1,y1,x2,y2
can.create_rectangle(100,100,200,300,fill="green")
can.create_text(150,250,text="Prahlad")
# img=PhotoImage(file="Doraemon-PNG-HD.png")
# can.create_image(200,300,image=img)

root.mainloop()







