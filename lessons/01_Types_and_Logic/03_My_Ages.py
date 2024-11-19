
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
q=simpledialog.askstring("How old are you?","type in here")
q=float(q)
my_age = 10.4 
if q==my_age:
    messagebox.showinfo("","You are pretty awesome!")
elif q>=0 and q<=2:
    messagebox.showinfo("","You are a baby!")
elif q>=2 and q<=5:
    messagebox.showinfo("","You are a toddler!")
elif q>=5 and q<=12:
    messagebox.showinfo("","You are a child!")
elif q>=12 and q<=18:
    messagebox.showinfo("","You are a teen!")
elif q>=18 and q<=65:
    messagebox.showinfo("","You are an adult!")
else:
    messagebox.showinfo("","You are a senior!")








































# Ask the user's age

# Use if statements to determine the age group
# and create a message

# Show the message to the user



window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
