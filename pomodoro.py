from tkinter import *
import math
# COLORS
GREEN = "#809A6F"
MAROON = "#A25B5B"
BEIGE = "#CC9C75"
LIGHT_GREEN = "#D5D8B5"
timer = None
reps = 0
check_mark = "︎"


# Clock
def timer_reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(text, text="00:00")


def start_timer():
    global reps
    global check_mark
    reps += 1
    if reps == 1 or reps == 3 or reps == 5:
        count_down(25 * 60)
        title.config(text="WORK")
    elif reps == 2 or reps == 4:
        count_down(5 * 60)
        title.config(text="BREAK")
        check_mark = check_mark + "✔︎"
        check_label.config(text=check_mark)
    elif reps == 6:
        count_down(10 * 60)
        title.config(text="BREAK")
        check_mark = check_mark + "✔︎"
        check_label.config(text=check_mark)
    elif reps == 7:
        title.config(text="GOOD JOB!")


def count_down(count):
    global timer
    count = count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
        new_text = f"{minutes}:{seconds}"
        canvas.itemconfig(text, text=new_text)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=GREEN)

title = Label(text="TIMER", bg=GREEN, fg=MAROON, font="Courier 50")
title.grid(row=0, column=1)

canvas = Canvas(window, width=200, height=240, bg=GREEN, highlightthickness=0)

img = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=img)
text = canvas.create_text(100, 140, text="00:00", font="courier 40")
canvas.grid(row=1, column=1)

start = Button(text="Start", highlightbackground=GREEN, command=start_timer)
start.grid(row=2, column=0)
reset = Button(text="Reset", highlightbackground=GREEN, command=timer_reset)
reset.grid(row=2, column=2)

check_label = Label(text=check_mark, bg=GREEN, fg=BEIGE)
check_label.grid(row=3, column=1)


window.mainloop()