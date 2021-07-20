from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys

root = Tk()
root.title("Calculator")
btnList = [
    "7", "8", "9", "+", "*",
    "4", "5", "6", "-", "/",
    "1", "2", "3", "=", ".", 
    "0", "±", "C", "(", ")"
    ]
row = 1
col = 0
for i in btnList:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row = row, column = col)
    col += 1
    if col > 4:
        col = 0
        row += 1

calcEntry = Entry(root, width = 33)
calcEntry.grid(row = 0, column = 0, columnspan = 5)
    
def calc(key):
    global mem
    if key == "=":
        yes = '-+0123456789.*/()'
        if calcEntry.get()[0] not in yes:
            calcEntry.insert(END, "First symbol is not a number!")
            messagebox.showerror("Error!", "You did not enter a number! Bruh!")
        try:
            result = eval(calcEntry.get())
            calcEntry.delete(0, END)
            calcEntry.insert(END, str(result))
        except:
            calcEntry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of the data.")
    elif key == "C":
        calcEntry.delete(0, END)
    elif key == "±":
        if "=" in calcEntry.get():
            calcEntry.delete(0, END)
        try:
            if calcEntry.get()[0] == "-":
                calcEntry.delete(0)
            else:
                calcEntry.insert(0, "-")
        except IndexError:
                pass
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit
    elif key == "(":
        calcEntry.insert(END, "(")
    elif key == ")":
        calcEntry.insert(END, ")")
    else:
        if "=" in calcEntry.get():
            calcEntry.delete(0, END)
        calcEntry.insert(END, key)

root.mainloop()