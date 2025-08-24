import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    tittle.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timertext, text="00:00")
    checkmarks.config(text="")

# ---------------------------- PLAY SOUND ------------------------------- #
def play_alarm():
    window.bell()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def starttimer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        tittle.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        tittle.config(text="Break", fg=PINK)
    else:
        countdown(work)
        tittle.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timertext, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        play_alarm()  # 🔔 Play built-in alarm
        starttimer()
        marks = "✓" * (reps // 2)
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tittle = Label(window, text="TIMER", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
tittle.grid(row=0, column=1)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timertext = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="START", highlightthickness=0, bg=WHITE, fg=GREEN, command=starttimer)
start.grid(row=2, column=0)

reset = Button(text="RESET", highlightthickness=0, bg=WHITE, fg=RED, command=reset_timer)
reset.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

window.mainloop()