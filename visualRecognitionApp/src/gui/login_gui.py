from tkinter import *

ws = Tk()
ws.title('PythonGuides')
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
login_btn = Button(
    left_frame,
    width=15,
    text='Login',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=None
    )

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.pack()


ws.mainloop()