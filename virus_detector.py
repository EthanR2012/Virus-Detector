from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x500')

# Function for displaying warning message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed") 
def msg():
    messagebox.showwarning("Alert!", "Stop! Virus Found.")

# Adding button widget to window
button = Button(root, text="Scan for Virus", command=msg)
button.pack()
root.mainloop()