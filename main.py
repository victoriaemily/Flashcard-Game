BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import time 

try:
    DataFrame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    DataFrame = pandas.read_csv("data/french_words.csv")
dict = DataFrame.to_dict(orient="records")
current_card = {}
missed_words = []

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict)
    canvas.itemconfig(card_img, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word,text=current_card['French'], fill="black")
    window.after(3000, func=flip_card)
def next_card_right():
    dict.remove(current_card)
    data = pandas.DataFrame(dict)
    data.to_csv("data/words_to_learn.csv")
    next_card()
def flip_card():
    canvas.itemconfig(card_img, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word,text=current_card['English'], fill="white")    

window = Tk()
window.title("Flashcard Game")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=next_card_right)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)


card_img = canvas.create_image(400,263, image=card_front)
canvas.grid(column = 0, row = 0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title = canvas.create_text(400,150, text="", font=("Arial",40,"italic"))
word = canvas.create_text(400,263, text="", font=("Arial",60,"bold"))

right_button.grid(column=1,row=1)
wrong_button.grid(column=0,row=1)

next_card()


window.mainloop()