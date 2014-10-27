from Tkinter import *

root = Tk()
root.title("Test")

def quit(event):
    root.destroy()

m = Menu(root)
root.config(menu=m)

fm = Menu(m, tearoff=0)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Quit", command=quit, accelerator='Ctrl+Q')

root.bind('<Control-Q>', quit)
root.bind('<Control-q>', quit)

root.mainloop()
