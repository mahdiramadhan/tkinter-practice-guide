import tkinter as tk

#create the main window
root = tk.Tk()
root.title("Hello tkinter")

#create label
label = tk.label(root,text="Hello, World")

#lay out label
label.pack()

#run forever
root.mainloop()