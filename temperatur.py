import tkinter as tk

#declare the variables
temp_c = None
temp_f = None

# this function is called whenever the button is pressed
def convert():
    global temp_c
    global temp_f
    # convert celsius to fahrenheint and update label (through variable)
    try :
        val = temp_c.get()
        temp_f.set((val*9.0/5)+32)
    except:
        pass

#create the main window
root = tk.Tk()
root.title("Temperature converter")
#create the main container
frame = tk.Frame(root)

#lay out the main container, specify that we want to grow with the window size
frame.pack(fill =tk.BOTH, expand=True)

#allow middle cell of grid to grow when window is resized
frame.columnconfigure(1,weight=1)
frame.rowconfigure(1, weight=1)

#variable for holding temperature data
temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()


#create widgets 
entry_celcius = tk.Entry(frame, width = 7, textvariable = temp_c)
label_unitc = tk.Label(frame, text= "C")
label_equal = tk.Label(frame, text = "is equal to")
label_fahrenheit = tk.Label(frame, textvariable= temp_f)
label_unitf = tk.Label(frame, text = "F")
button_convert = tk.Button(frame, text = "Convert", command=convert)

#lay out widgets
entry_celcius.grid(row =0, column =1, padx=5, pady =5)
label_unitc.grid(row=0, column = 2, padx=5, pady= 5,sticky= tk.W)
label_equal.grid(row = 1, column = 0, padx = 5, pady = 5, sticky =tk.E)
label_fahrenheit.grid(row = 1, column = 1, )
label_unitf.grid(row= 2, column = 2, padx = 5, pady =5, sticky =tk.W)
button_convert.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady =5, sticky = tk.E )

#please cursor in entry box by default
entry_celcius.focus()

#run forever
root.mainloop()