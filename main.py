from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DARK_YELLOW = '#F7F373'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_var = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_var)
    canvas.itemconfig(timer_text,text="00.00")
    timer.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Long Break",fg=RED,highlightthickness=0)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Short Break",fg=PINK,highlightthickness=0)

    else:
        countdown(work_sec)
        timer.config(text="Work",fg=PINK,highlightthickness=0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00" #Dynamic typing method. We can change the datatype of the variable simulateously.
    if int(count_sec) <= 9 and int(count_sec)>= 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_var
        timer_var = window.after(1000,countdown,count-1)

    else:
        start_timer()
        marks = ""
        work_session = floor(reps/2)
        for _ in range(work_session):
            marks = "✔️"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
#Creating Window
window = Tk()
window.title("The Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)


#Adding the tomato image using PhotoImage and Canvas classes
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200,height=224,highlightthickness=0,bg=YELLOW)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=1)


#Creating Timer Label
timer = Label(text="Timer",fg=GREEN,font=(FONT_NAME,45,"bold"),highlightthickness=0,bg=YELLOW)
timer.grid(column=2,row=0)

#Creating Start Button
start = Button(text="Start",fg=RED,bg=DARK_YELLOW,font=(FONT_NAME,18,"bold"),command=start_timer)
start.grid(column=1,row=3)

#Creating Reset Button
reset = Button(text="Reset",fg=RED,bg=DARK_YELLOW,font=(FONT_NAME,18,"bold"),command=reset_timer)
reset.grid(column=3,row=3)

#Creating Checkmarks
check_mark = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,24,"bold"))
check_mark.grid(column=2,row=3)


window.mainloop()