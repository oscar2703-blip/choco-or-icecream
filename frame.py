from tkinter import*

root= Tk()
root.geometry("300x150")

a=Label(root,text="Chocos and Icecreams")
a.pack()

frame=Frame(root)
frame.pack()

frame1=Frame(root)
frame1.pack(side=BOTTOM)

b1=Button(frame,text="choco",fg="red",bg="white")
b1.pack(side=LEFT)

b2=Button(frame,text="Dark choco",fg="red",bg="white")
b2.pack(side=LEFT)

b3=Button(frame,text="White choco",fg="red",bg="white")
b3.pack(side=LEFT)

b4=Button(frame1,text="Pastry",fg="green",bg="white")
b4.pack(side=BOTTOM)

b5=Button(frame1,text="Cake",fg="green",bg="white")
b5.pack(side=BOTTOM)

b6=Button(frame1,text="Tiramisu",fg="green",bg="white")
b6.pack(side=BOTTOM)
root.mainloop()