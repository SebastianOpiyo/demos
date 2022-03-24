import sys
import os
from tkinter import *
from tkinter import ttk
from controller import register_name


# TODO: handle exceptions with try-except


def run_registration():
    """Registers new users id and as many photos for training."""
    for f in os.listdir("../"):
        if f == 'image_capture.py':
            os.system('python ../image_capture.py')
        break


def run_camera():
    for f in os.listdir("../"):
        if f == 'camera_test.py':
            os.system('python ../camera_test.py')
        break


def run_face_train():
    for f in os.listdir("../"):
        if f == 'face_training.py':
            os.system('python ../face_training.py')
        break


def run_recognizer_register():
    for f in os.listdir("../"):
        if f == 'recognizer.py':
            os.system('python ../recognizer.py')
        break


class VisualRecognitionGui:

    def __init__(self, root):
        root.title("Facial Recognition Registration Application")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Test Camera", command=run_camera).grid(column=5, row=2, sticky=S)
        ttk.Button(mainframe, text="Check-in", command=run_recognizer_register).grid(column=5, row=5,
                                                                                         sticky=(N, W, E, S))
        ttk.Button(mainframe, text="Train", command=run_face_train).grid(column=5, row=7, sticky=W)
        ttk.Button(mainframe, text="Register User", command=run_registration).grid(column=5, row=9, sticky=W)
        ttk.Button(mainframe, text="Exit Camera", command=register_name).grid(column=5, row=11, sticky=S)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", register_name)


root = Tk()
VisualRecognitionGui(root)
root.mainloop()
#
# if __name__ == "__main__":
#     run_camera()
