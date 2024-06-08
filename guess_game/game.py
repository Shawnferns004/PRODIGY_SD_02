import customtkinter as ctk
import tkinter as tk
import random

attempts =0
answer = random.randint(1,99)

app = ctk.CTk()
app.geometry("600x470+700+150")
app.title("Guess the Number")


f = ctk.CTkFrame(
    app,
    width=580,
    height=450,
    corner_radius=10,
).place(x=10,y=10)


lbl = ctk.CTkLabel(
    f,
    text="Guess the Number between 1 and 99",
    bg_color="#2b2b2b",
    font=("Poppins",18,"bold"),

).place(x=130,y=20)

num_entry = ctk.CTkEntry(
    f,
    width=400,
    height=40,
    font=("Poppins",15,"bold"),
)
num_entry.place(x=110,y=70)

check_btn = ctk.CTkButton(
    f,
    width=100,
    height=40,
    text="Check",
    hover=False,
    fg_color="#6895D2",
    text_color="black",
    corner_radius=15,
    command=lambda:check(),
    bg_color="#2b2b2b",
    font=("Poppins",20,"bold"),
)
check_btn.place(x=260,y=150)

quit_btn_2 = ctk.CTkButton(
    f,
    width=100,
    height=40,
    text="QUIT",
    hover=False,
    fg_color="#FF6969",
    text_color="black",
    corner_radius=15,
    command=app.destroy,
    bg_color="#2b2b2b",
    font=("Poppins",20,"bold"),
)


quit_btn = ctk.CTkButton(
    f,
    width=100,
    height=40,
    text="QUIT",
    hover=False,
    fg_color="#FF6969",
    text_color="black",
    corner_radius=15,
    command= app.destroy,
    bg_color="#2b2b2b",
    font=("Poppins",20,"bold"),
)
quit_btn.place(x=260,y=210)

att = tk.StringVar()
att.set("Attempt  ⟼  0")
war_lbl = tk.Label(
    f,
    textvariable=att,
    font=("Poppins",12,"bold"),
    bg="#2b2b2b",
    fg="white"
).place(x=260,y=280)


chk = tk.StringVar()
chk.set("")
chk_lbl = tk.Label(
    f,
    textvariable=chk,
    font=("Poppins",12,"bold"),
    bg="#2b2b2b",
    fg="white"
).place(x=265,y=320)

win = tk.StringVar()
win.set("")
win_lbl = tk.Label(
    f,
    textvariable=win,
    font=("Poppins",12,"bold"),
    bg="#2b2b2b",
    fg="white"
).place(x=230,y=320)

hint = tk.StringVar()
hint.set("")
hint_lbl = tk.Label(
    f,
    textvariable=hint,
    font=("Poppins",12,"bold"),
    bg="#2b2b2b",
    fg="#D0F288"
).place(x=260,y=380)

def check():
    global attempts
    global answer

    attempts += 1
    guess = int(num_entry.get())
    if answer == guess:
        win.set("You Win! Congrats!!")
        chk.set("")
        hint.set("")
        check_btn.place_forget()
        quit_btn.place_forget()
        quit_btn_2.place(x=260,y=150)
    elif guess < answer:
        att.set("Attempt  ⟼  "+str(attempts))
        chk.set("Incorrect")
        hint.set("GO HIGHER!")
    elif guess>answer:
        att.set("Attempt  ⟼  "+str(attempts))
        chk.set("Incorrect")
        hint.set("GO LOWER!")


app.mainloop()