"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.



 # Keeps the window open


# TODO: 
import random
from tkinter import messagebox, simpledialog, Tk # import required modules
import random
window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
a=0
b=0
for i in range(50):
    x=random.randint(-1000,1000)
    y=random.randint(-1000,1000)
    z=simpledialog.askinteger("math quiz", f"{str(x)}x{str(y)}")
    if x * y == z:
        a=a+1
        messagebox.showinfo("math quiz","true")
    else:
        b=b+1
        messagebox.showinfo("math quiz","false")
if a>=b:
    messagebox.showinfo("math quiz","you win")
else:
    messagebox.showinfo("math quiz","you lose")
"""
# TODO: 
from tkinter import messagebox, simpledialog, Tk # import required modules
window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop up
x=simpledialog.askinteger("", "input1")
y=simpledialog.askinteger("", "input2")
messagebox.showinfo("",x+y)


