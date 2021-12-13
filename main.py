#What is exactly is a  Pomodoro? The Pomodoro technique is a time management method developed by Francesco Cirillo in the late 1980s.
# It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.
# So basically 1 Pomodoro is one set of 25 minute with 5 minutes break.
# After four Pomodoros it will be a long break traditionally 15 to 20 minutes.


#Is Pomodoro really effective?
#It's ideal for many types of work including writing, coding, design, and study. The
#technique also works if you have a lot of repetitive work to get through, such as wading
#through a busy inbox. A 25-minute Pomodoro session is long enough to get a little work
#done but not so long that it feels painful or overwhelming.

from tkinter import *
import math

root = Tk()
root.title("Pomodoro Timer")
root.iconbitmap("tom.ico")
root.config(padx=100, pady=50, bg="#f7f5dd")
title = Label(text="Pomodoro⌛", font=("Courier", 32, "bold"), fg="#A3423C", bg="#f7f5dd")

# ---------------------------- VARIABLES ------------------------------- #

WORK_TIME_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = None

# ---------------------------- FUNCTIONS ------------------------------- #

# to reset the timer
def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    tick.config(text="")

# to start the timer
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_TIME_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Rest", fg="#781D42")

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Rest", fg="#781D42")
    else:
        count_down(work_sec)
        title.config(text="Hustle")


# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = " "
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✓"
        tick.config(text=mark)


canvas = Canvas(width=260, height=223 , bg="#f7f5dd", highlightthickness=0)
apple_img = PhotoImage(file="apple.png")
canvas.create_image(130, 112, image=apple_img)
timer_text = canvas.create_text(128, 138, text="00:00", fill="white", font=("Courier", 35, "bold"))




start_button = Button(text="Start", highlightthickness=0, padx = 15, pady= 9,  command=start_timer, bg="#5DBB63", fg="white")
reset_button = Button(text="Reset", highlightthickness=0,padx = 15, pady= 9, command=reset_timer, bg="#B90E0A", fg="white")
tick = Label(font=("Courier", 12, "bold"), fg="#9bdeac", bg="#f7f5dd")


#-------------------------------put buttons on the screen-------------------#
title.grid(column=1,row=0)
canvas.grid(column=1,row=1)
start_button.grid(column=0,row=2,)
reset_button.grid(column=2,row=2)
tick.grid(column=1,row=3)

root.mainloop()