import os

"""
Module: controller - has all the controller/utility functions used by the GUI EVENTS.
Description: the functions prefixed with `run` are meant for script exec.

"""


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
