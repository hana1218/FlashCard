from tkinter import *
from tkinter import messagebox
import random
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"
timer = NONE
current_card = {}
data_dic = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    original_data = pd.read_csv("data/french_words.csv")
    data_dic = original_data.to_dict(orient="records")
else:
    data_dic = data.to_dict(orient="records")

def flip():
    canvas.itemconfig(canvas_image,image = card_back_image)
    canvas.itemconfig(language_text, text='English', fill="white")
    canvas.itemconfig(word_text, text=current_card['English'], fill="white")



def click_right():
    data_dic.remove(current_card)
    new_data = pd.DataFrame(data_dic)
    new_data.to_csv("data/words_to_learn.csv" ,index=False)
    next_card()

def click_wrong():
    next_card()

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card =random.choice(data_dic)
    canvas.itemconfig(canvas_image,image = card_img)
    canvas.itemconfig(language_text, text='French', fill="black")
    canvas.itemconfig(word_text, text=current_card['French'], fill="black")
    flip_timer = window.after(3000,flip)

window = Tk()
window.title("Fashy")
window.config(padx= 50, pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip)

canvas = Canvas(width = 800, height = 526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_img = PhotoImage(file ="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas_image =canvas.create_image(400, 263, image=card_img)
canvas.grid(column=0,row=0, columnspan=2)

language_text = canvas.create_text(400, 150, text="title",font=("Ariel",40,"italic"))
word_text = canvas.create_text(400, 263, text="trouve",font=("Ariel",60,"bold"))

right_image = PhotoImage(file ="./images/right.png")
wrong_image = PhotoImage(file ="./images/wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness=0, command=click_wrong)
wrong_button.grid(column=0,row=1)

right_button = Button(image = right_image, highlightthickness=0, command = click_right)
right_button.grid(column=1,row=1)

next_card()
window.mainloop()

