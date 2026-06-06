from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep, timer

    start_button.config(state="normal")

    if timer is not None:
        window.after_cancel(timer)

    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    rep = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    rep += 1

    start_button.config(state="disabled")

    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if rep == 8:
        label.config(fg=RED, text="Break")
        count_down(long_break_time)
    elif rep % 2 == 0:
        label.config(fg=PINK, text="Break")
        count_down(short_break_time)
    else:
        label.config(fg=GREEN, text="Work")
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global rep
    global timer

    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(
        timer_text,
        text=f"{count_min}:{count_sec:02d}"
    )
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        text = ""
        for i in range(rep // 2):
            text += "✔"
        check_mark.config(text=text)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=60, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img,)

timer_text = canvas.create_text(100,130,text="00:00", font=(FONT_NAME, 24, "bold"), fill='white')
canvas.grid(row=1, column=1)

label = Label(window, text="Timer", bg=YELLOW, font=(FONT_NAME, 26, "bold"), fg=GREEN)
label.grid(row=0, column=1)

start_button = Button(window, text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(window, bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

if __name__ == "__main__":
    window.mainloop()