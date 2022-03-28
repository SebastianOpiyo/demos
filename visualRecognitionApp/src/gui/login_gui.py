from tkinter import *
from tkinter import messagebox
import sqlite3


def login():
    """Login GUI"""
    ws = Tk()
    ws.title('Login')
    ws.config(bg='#0B5A81')

    f = ('Times', 14)

    left_frame = Frame(
        ws,
        bd=2,
        bg='#CCCCCC',
        relief=SOLID,
        padx=10,
        pady=10
    )

    Label(
        left_frame,
        text="Enter Email",
        bg='#CCCCCC',
        font=f).grid(row=0, column=0, sticky=W, pady=10)

    Label(
        left_frame,
        text="Enter Password",
        bg='#CCCCCC',
        font=f
    ).grid(row=1, column=0, pady=10)

    email_tf = Entry(
        left_frame,
        font=f
    )
    pwd_tf = Entry(
        left_frame,
        font=f,
        show='*'
    )

    # Addition
    def login_response():
        username, pwd = "", ""
        try:
            con = sqlite3.connect('../data/userdata.db')
            c = con.cursor()
            for row in c.execute("Select * from record"):
                username = row[1]
                pwd = row[5]

        except Exception as ep:
            messagebox.showerror('', ep)

        uname = email_tf.get()
        upwd = pwd_tf.get()
        check_counter = 0
        if uname == "":
            warn = "Username can't be empty"
        else:
            check_counter += 1
        if upwd == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            if uname == username and upwd == pwd:
                messagebox.showinfo('Login Status', 'Logged in Successfully!')

            else:
                messagebox.showerror('Login Status', 'invalid username or password')
        else:
            messagebox.showerror('', warn)

    login_btn = Button(
        left_frame,
        width=15,
        text='Login',
        font=f,
        relief=SOLID,
        cursor='hand2',
        command=login_response
    )

    email_tf.grid(row=0, column=1, pady=10, padx=20)
    pwd_tf.grid(row=1, column=1, pady=10, padx=20)
    login_btn.grid(row=2, column=1, pady=10, padx=20)
    left_frame.pack()

    ws.mainloop()
    return email_tf, pwd_tf


