from tkinter import*
import pandas
import random

time = 3
new_card = None


def change_card():
    generate_card()
    canvas.itemconfig(card_pic, image=image3)
    canvas.itemconfig(text1, text="French", fill="black")
    canvas.itemconfig(text2, text=new_card["French"], fill="black")
    timer(time)


def timer(value):
    clock = None
    if value >= 0:
        clock = window.after(1000, timer, value - 1)
        canvas.itemconfig(text3, text=f"Time: {value}")
    if value == 0:
        show_meaning()
        canvas.itemconfig(text3, text="")
        canvas.after_cancel(clock)


def show_meaning():
    canvas.itemconfig(card_pic, image=image4)
    canvas.itemconfig(text1, text="English", fill="white")
    canvas.itemconfig(text2, text=new_card["English"], fill="white")


def generate_card():
    global new_card
    file_data = pandas.read_csv("./data/french_words.csv")
    to_learn = file_data.to_dict(orient="records")
    new_card = random.choice(to_learn)


window = Tk()
window.title("My Flash Card Application for learning French")
window.config(width=900, height=726, padx=50, pady=50, bg="#B1DDC6")

image1 = PhotoImage(file="./images/right.png")
image2 = PhotoImage(file="./images/wrong.png")
image3 = PhotoImage(file="./images/card_front.png")
image4 = PhotoImage(file="./images/card_back.png")

button1 = Button(image=image1, highlightthickness=0, bg="#B1DDC6", command=change_card)
button1.place(x=55, y=550)

button2 = Button(image=image2, highlightthickness=0, bg="#B1DDC6", command=change_card)
button2.place(x=600, y=550)

canvas = Canvas()
canvas.config(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_pic = canvas.create_image(400, 263, image=image3)
text1 = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text2 = canvas.create_text(400, 265, text="", font=("Ariel", 50, "bold"))
text3 = canvas.create_text(150, 365, text="Time: ", font=("Ariel", 25, "bold"))
canvas.place(x=1, y=1)

change_card()

window.mainloop()
