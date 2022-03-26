import os
import sqlite3

"""
Module: controller - has all the controller/utility functions used by the GUI EVENTS.
Description: the functions prefixed with `run` are meant for script exec.

"""

# database driver
try:
    db = sqlite3.connect('../data/register.db')
    print("Database created successfully")
    db.execute('''CREATE TABLE REGISTER
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             DATE_TIME            DATE     NOT NULL);''')

    print("Table created successfully")
except sqlite3.Error as er:
    print(f'Sqlite3 encountered an error, {er}')


def run_registration():
    """Registers new users id and as many photos for training."""
    for f in os.listdir("../"):
        if f == 'image_capture.py':
            os.system('python ../image_capture.py')
        break


def run_camera():
    """Test the camera before starting visual recognition."""
    for f in os.listdir("../"):
        if f == 'camera_test.py':
            os.system('python ../camera_test.py')
        break


def run_face_train():
    """Train the model using the captured images."""
    for f in os.listdir("../"):
        if f == 'face_training.py':
            os.system('python ../face_training.py')
        break


def run_recognizer_register():
    """Recognize the user script."""
    for f in os.listdir("../"):
        if f == 'recognizer.py':
            os.system('python ../recognizer.py')
        break
