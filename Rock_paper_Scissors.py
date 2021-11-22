import random
from future.moves import tkinter as tk
from future.moves.tkinter import messagebox as mb

# user_selected, computer_selected, user_points, computer_points
us = ''
cs = ''
up = 0
cp = 0
c = ''


# this function shows the goodbye window
def change():
    global w2
    w2 = tk.Tk()
    w2.title('Creator')
    canvas = tk.Canvas(w2, width=350, height=100, bg='Black')
    canvas.pack()
    final_lab = tk.Label(text="Created by Parham", font=12, fg='Green', bg='Black')
    canvas.create_window(175, 17, window=final_lab)
    final_button = tk.Button(text="ok", command=ok, bg='Black', fg='White', relief=tk.RAISED, borderwidth=8, font=4)
    canvas.create_window(175, 64, window=final_button)
    w2.mainloop()


# in the final window, there is a button labeled "ok" and will destroy the final window and ends the program
def ok():
    global w2
    w2.destroy()


# exit dialog
def Exit():
    global window
    res = mb.askquestion('Exit', 'Are you sure you want to exit the program?')
    if res == 'yes':
        window.destroy()
    else:
        pass


# choosing rock
def rock():
    global us, cs, c, up, cp, lc, lup, lcp, ls
    us = 'You chose \'Rock\' & '
    # a random number between 1 and 3
    cs = random.randrange(1, 4)
    if cs == 1:
        c = "Draw!"
        cs = 'Computer chose \'Rock\''
    elif cs == 2:
        c = "You lost!"
        cp += 1
        cs = 'Computer chose \'Paper\''
    elif cs == 3:
        c = "You won!"
        up += 1
        cs = 'Computer chose \'Scissors\''
    lc['text'] = c
    ls['text'] = us + cs
    lup['text'] = 'Your score is: ' + str(up)
    lcp['text'] = "Computer's score is: " + str(cp)


# choosing paper
def paper():
    global us, cs, c, up, cp, lc, lup, lcp, ls
    us = 'You chose \'Paper\' & '
    cs = random.randrange(1, 4)
    if cs == 2:
        c = "Draw!"
        cs = 'Computer chose \'Paper\''
    elif cs == 3:
        c = "You lost!"
        cs = 'Computer chose \'Scissors\''
        cp += 1
    elif cs == 1:
        c = "You won!"
        cs = 'Computer chose \'Rock\''
        up += 1
    lc['text'] = c
    ls['text'] = us + cs
    lup['text'] = 'Your score is: ' + str(up)
    lcp['text'] = "Computer's score is: " + str(cp)


# choosing scissors
def scissors():
    global us, cs, c, up, cp, lc, lup, lcp, ls
    us = 'You chose \'Scissors\' & '
    cs = random.randrange(1, 4)
    if cs == 3:
        c = "Draw!"
        cs = 'Computer chose \'Scissors\''
    elif cs == 1:
        c = "You lost!"
        cs = 'Computer chose \'Rock\''
        cp += 1
    elif cs == 2:
        c = "You won!"
        cs = 'Computer chose \'Paper\''
        up += 1
    lc['text'] = c
    ls['text'] = us + cs
    lup['text'] = 'Your score is: ' + str(up)
    lcp['text'] = "Computer's score is: " + str(cp)


# main window
window = tk.Tk()
window.title('Rock, Paper, Scissors')
canvas = tk.Canvas(window, width=400, height=350, bg='Yellow')
canvas.pack()

# buttons
br = tk.Button(text='Rock', relief=tk.RAISED, borderwidth=12, font=0, width=34, bg='Black', fg='White', command=rock)
canvas.create_window(202, 30, window=br)

bp = tk.Button(text='Paper', relief=tk.RAISED, borderwidth=12, font=0, width=34, command=paper)
canvas.create_window(202, 91, window=bp)

bs = tk.Button(text='Scissors', relief=tk.RAISED, borderwidth=12, font=0, width=34, bg='Gray', fg='Black',
               command=scissors)
canvas.create_window(202, 152, window=bs)

bg = tk.Button(text='Exit', relief=tk.RAISED, borderwidth=8, width=8, bg='Red', command=Exit)
canvas.create_window(41, 335, window=bg)

lc = tk.Label(text=c, fg="Black", bg='Yellow', font=0)
canvas.create_window(202, 197, window=lc)

ls = tk.Label(text=(us + cs), fg="Black", bg='Yellow')
canvas.create_window(202, 227, window=ls)

lup = tk.Label(text=('Your score is: ' + str(up)), fg="Black", bg='Yellow', font=0)
canvas.create_window(202, 257, window=lup)

lcp = tk.Label(text=("Computer's score is: " + str(cp)), fg="Black", bg='Yellow', font=0)
canvas.create_window(202, 297, window=lcp)
window.mainloop()

change()
