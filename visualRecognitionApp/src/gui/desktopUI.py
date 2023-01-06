import sys
import os
from tkinter import *
from tkinter import ttk
from login_gui import login
from controller import run_camera, run_registration, run_recognizer_register, run_face_train

# we call the login first
login()


# TODO: handle exceptions with try-except

class VisualRecognitionGui:

    def __init__(self, root):
        root.geometry("800x400")
        root.title("AI Facial Registration App.")
        root.resizable(0, 0)

        # configure the grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)

        mainframe = ttk.Frame(root, padding="5 5 5 5")
        mainframe.grid(column=0, row=0, sticky="N, W, E, S")

        header = Label(mainframe, text="******* FACE RECOGNITION ATTENDANCE SYSTEM *******", font=("Arial Bold", 15))
        header.grid(column=1, row=0)

        # # TODO: Ensure the image is displayed
        image = PhotoImage(file='homeimage.png')
        image_label = Label(mainframe)
        image_label.image = image
        image_label['image'] = image_label.image
        image_label.grid(column=1, row=16)

        # Create widgets
        ttk.Button(mainframe, text="Test Camera", command=run_camera).grid(column=0, row=2, sticky=S)
        ttk.Button(mainframe, text="Check-in", command=run_recognizer_register).grid(column=2, row=2,
                                                                                     sticky="N, W, E, S")
        ttk.Button(mainframe, text="Train", command=run_face_train).grid(column=0, row=7, sticky=W)
        ttk.Button(mainframe, text="Register User", command=run_registration).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text="Quit", command=root.destroy).grid(column=1, row=15, sticky=S)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", run_registration)


window = Tk()
VisualRecognitionGui(window)
window.after(3000)
window.mainloop()
