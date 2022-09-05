from tkinter import *
from Classes.Ball import Ball
from Classes.Paddle import Paddle
from Classes.Score import Score
import time

tk = Tk()
start = True
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

score = Score(canvas, 'green')
paddle=Paddle(canvas, 'blue')
ball=Ball(canvas, paddle, 'red', score)
gameovermessage = canvas.create_text(225,200,text = 'Game Over :(', state = HIDDEN)


while 1:
    if ball.hit_bottom == False and paddle.start == True:
        ball.draw()
        paddle.draw()
    if ball.hit_bottom == True:
        time.sleep(0.5)
        canvas.itemconfig(gameovermessage, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)