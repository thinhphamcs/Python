# Note:
# Error will be the guess number > 100. Will fix

# Import tkinter and random module
import tkinter
import random
# From tkinter import messagebox for showinfo
# and * for everything else
from tkinter import *
from tkinter import messagebox

# =========================================== #

# set master = Tk() class
master = Tk()
# Edit the title
master.title("Guess the correct number")
# Create an entry box
entry = Entry(master)
entry.pack()  # pack it up
# Read more about this
entry.focus_set()

# =========================================== #

# Generate random number for correct number
number = random.randint(0, 100)
# Convert number to int
convert_to_int = int(number)
# Then convert it to string so it matches
# with the user input STRING data
correct_number = str(convert_to_int)
# print(correct_number)


# =========================================== #


def guessing():  # Define guessing function
    # entry.get will get me the data from user
    guessed_number = entry.get()
    # print(guessed_number)
    # For breaking the loop
    stop = 0
    # Loop to create a random number
    while True:
        # If statement
        if guessed_number < correct_number:
            messagebox.showinfo("Guessing", "Guess Higher")
        # else if statement
        elif guessed_number == correct_number:
            messagebox.showinfo("Guessing", "Good Job!")
        # else statement
        else:
            messagebox.showinfo("Guessing", "Guess Lower")
        # Break the loop
        if stop == 0:
            break


def quit():  # Define quit function
    exit()

# =========================================== #


# GUI for the guess button
guess_button = Button(master, text="Guess the number", width=25, command=guessing)
guess_button.pack()
# GUI for the quit button
quit_button = Button(master, text="Quit", width=25, command=quit)
quit_button.pack()
# Read about this
master.mainloop()
