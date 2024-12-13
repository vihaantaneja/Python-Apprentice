"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""
from tkinter import messagebox, simpledialog, Tk # import required modules
window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop up
x=simpledialog.askinteger("", "input1 1,2,3...")
y=simpledialog.askinteger("", "input2 1,2,3...")
z=simpledialog.askstring("", "input3 plus, minus, times, divided by, to the power of")
z=z.lower()
if z == "plus":
   messagebox.showinfo("",x+y) 
elif z == "minus":
   messagebox.showinfo("",x-y) 
elif z == "times":
   messagebox.showinfo("",x*y) 
elif z == "divided by":
   messagebox.showinfo("",x/y) 
elif z == "to the power of":
   messagebox.showinfo("",x**y) 
else:
    messagebox.showinfo("","I don't know and I don't care!") 
# Import the required modules

# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   

# Ask the user for the second number

# Ask the user for the math operation

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
