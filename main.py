from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    canvas.after_cancel(timer)
    label_timer.config(text="TIMER", fg=GREEN)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label_checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1

    if reps % 8 == 0:
        label_timer.config(text="Break", fg=RED, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_timer.config(text="Break", fg=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label_timer.config(text="Work", fg=GREEN, bg=YELLOW)
        count_down(1 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)

    #Dynamic typing

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
         global timer
         timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        print(reps)
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✓"
        label_checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=100, padx=100, bg=YELLOW)

#Create a canavas

canvas = Canvas()
canvas.config(width=200, height =224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
#assign for getting timer text to show
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Create labels
label_timer = Label()
label_timer.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

label_checkmark = Label()
label_checkmark.config(fg=GREEN, bg=YELLOW, font="bold")
label_checkmark.grid(column=1, row=3)

#Cretate buttons

button_start = Button()
button_start.config(text="Start", bg=YELLOW, width=7, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button()
button_reset.config(text="Reset", bg=YELLOW, width=7, command=reset_timer)
button_reset.grid(column=2, row=2)




window.mainloop()
