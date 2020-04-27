import tkinter

root = tkinter.Tk()

def grey (*args, **kwargs):
    root.configure(background = "grey")

def bthing():
    root.configure(background= "red")

def bthing1():
    root.configure(background= "green")

def bthing2():
    root.configure(background= "blue")

tkinter.Button(text = "Red", command = bthing).pack()
tkinter.Button(text = "Green", command = bthing1).pack()
tkinter.Button(text = "Blue", command = bthing2).pack()
root.configure(background = "white")
root.geometry("400x400")

root.mainloop()