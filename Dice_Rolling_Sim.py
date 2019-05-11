# Import tkinter and random module
import tkinter
import random
# from tkinder module import (a message box) or * for everything
from tkinter import *
from tkinter import messagebox

# =========================================== #

master = Tk()  # Call class tkinter

# =========================================== #


def roll_dice():  # Define the roll dice function
    # I need an array to store the dice faces
    numbers = []
    # For breaking the loop
    stop = 0
    # Loop to run through the faces
    while True:
        # the random faces between 1 and 6
        # will be added back to the array
        numbers.append(random.randint(1, 6))
        # Print it out on page
        label.config(text=str(numbers))
        # Print it out in console.
        print("The dice number is:", numbers)
        # messagebox.showinfo("Your dice number is: ", numbers)
        # Break the loop
        if stop == 0:
            break


def roll_again():  # Define the roll again function
    roll_dice()

# =========================================== #


# Label Title
master.title("Dice Rolling")
label = Label(master, fg="black")
label.pack()
# Roll again button
roll_again_button = Button(master, text='Roll Again', width=25, command=roll_again)
roll_again_button.pack()
# Quit button
quit_button = Button(master, text="Quit", width=25, command=quit)
quit_button.pack()
#
master.mainloop()
