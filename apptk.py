import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
number = random.randint(1,10)

def input_function():
    guess1 == int(input("Enter guess here: "))
    return guess1

def test_function(entry):
    guess1 = int(entry)
    if guess1 == 6:
        label["text"] = "Yay, you got it on first trial!"
    else:
        test_function(entry)
        label["text"] = "Wrong. Enter your second guess!"
        guess2 = int(entry)
        if guess2 == number:
            label["text"] = "Yay, you got it on second trial!"

        else:
            label["text"] = "Wrong. Enter your final guess!"
            guess3 = int(entry)
            if guess3 == number:
                label["text"] = "Yay, you got it on final trial!" 
            else:
                label["text"]="You did not get the number on all trials. The number is {}".format(number)



canvas = tk.Canvas(root, height = "700", width = "800")
canvas.pack()

frame = tk.Frame(root, bg = "#80c1ff")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(frame, text="Check Guess!", bg = "gray", font=5, command=lambda: test_function(entry.get()))
button.place(relx=0.3, rely=0.85, relwidth=0.4, relheight = 0.1)

label1 = tk.Label(frame, text = "WELCOME TO THE GUESS GAME :)", bg = "yellow", fg="red", font = 15)
label1.place(relx=0.3, rely=0.01, relwidth=0.4, relheight = 0.1)

label2 = tk.Label(frame, text = "Enter your guess \nin the box below", bg = "#80c1ff", fg="red", font=8)
label2.place(relx=0.3, rely=0.2, relwidth=0.4, relheight = 0.1)

label3 = tk.Label(frame, text = "\n\n A number has been chosen between 1 and 10 (inclusive). \n You have 3 guesses to make in order to get the number right.\n\n Ready? Go!!\n")
label3.place(relx=0.125, rely=0.4, relwidth=0.75, relheight = 0.2)

label = tk.Label(frame)
label.place(relx=0.125, rely=0.62, relwidth=0.75, relheight = 0.2)

entry = tk.Entry(frame, bg = "gray")
entry.place(relx=0.3, rely=0.3, relwidth=0.4, relheight = 0.1)

root.mainloop()