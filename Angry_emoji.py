from tkinter import *
root = Tk()
'''center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    '''

myCanvas = Canvas(root,bg="lime", height=300, width=300)
myCanvas.pack()
#x=150,y=150,r=100
myCanvas.create_oval(50,50,250,250,fill="crimson",width=5)
#x=110,y=155,r=15
myCanvas.create_oval(95,110,130,160,fill="black")
#x=180,y=155,r=15
myCanvas.create_oval(165,110,200,160,fill="black")
#x=150,y=18,r=100
myCanvas.create_arc(50,-88,250,118,start=230,extent=80,style='arc',width=5)
#x=150,y=220,r=50
arc = myCanvas.create_arc(100, 170, 200, 270, start=30, extent=120,style="arc",width=5)

myCanvas.create_text(150,30,text="Angry Face")
root.mainloop()
