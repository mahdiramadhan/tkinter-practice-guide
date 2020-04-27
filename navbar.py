from tkinter import *
from tkinter.filedialog import askopenfilename

def NewFile():
    print("New File!")

def OpenFile():
    name = askopenfilename()
    print(name)

def About():
    print("this is a simple navbar")

root = Tk()
menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File",menu = filemenu)
filemenu.add_command(label = "New", command = NewFile)
filemenu.add_command(label = "Open...", command = OpenFile)
filemenu.add_command(label = "Exit", command = root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About..." , command = About)
mainloop()
