import os
from tkinter import messagebox

"""
Module: controller - has all the controller/utility functions used by the GUI EVENTS.
Description: the functions prefixed with `run` are meant for script exec.

"""


def run_registration():
    """Registers new users id and as many photos for training."""
    try:
        for f in os.listdir("../"):
            if f == 'image_capture.py':
                os.system('python ../image_capture.py')
                print("Successfully ran the user registration script")
                messagebox.showinfo("Success", "Registration Successful!")
                break
    except (FileNotFoundError, FileExistsError) as e:
        print(f'File Error, {e}')
        messagebox.showerror("File Not Found", e)


def run_camera():
    """Test the camera before starting visual recognition."""
    try:
        for f in os.listdir("../"):
            if f == 'camera_test.py':
                os.system('python ../camera_test.py')
                print("Successfully tested the camera")
                messagebox.showinfo("Success", "Camera Is Cool!")
                break
    except (FileNotFoundError, FileExistsError) as e:
        print(f'File Error: {e}')
        messagebox.showerror("File Not Found", e)


def run_face_train():
    """Train the model using the captured images."""
    try:
        for f in os.listdir("../"):
            if f == 'face_training.py':
                os.system('python ../face_training.py')
                messagebox.showinfo("Success", "Model Training script ran successfully")
                break
    except (FileNotFoundError, FileExistsError) as e:
        print(f'File Error: {e}')
        messagebox.showerror("File Not Found", e)


def run_recognizer_register():
    """Recognize the user script."""
    try:
        for f in os.listdir("../"):
            if f == 'recognizer.py':
                os.system('python ../recognizer.py')
                print("Recognition script ran successfully")
                messagebox.showinfo("Success", "Recognition script ran successfully")
                break
    except (FileExistsError, FileNotFoundError) as e:
        print(f'File Error: {e}')
        messagebox.showerror("File Not Found", e)


def exit_app():
    pass


if __name__ == '__main__':
    run_camera()
    # run_registration()
