"""
Real Time Face Recogition
- Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc
- LBPH computed model (trained faces) should be on trainer/ dir.
"""

import cv2
import csv
import sqlite3
from datetime import datetime
from data.db import db


# Write user and time of reporting to csv file & sqlite db.
def write_to_csv(user_name: str):
    time = datetime.now()
    report_date = time.strftime("%b %d, %Y")
    time_stamp = time.strftime("%H:%M:%S")
    data = [user_name, report_date, time_stamp]
    # Database execution here.

    try:
        db_cursor = db.cursor()
        params = (user_name, report_date, time_stamp)
        db_cursor.execute("INSERT INTO REGISTER VALUES (NULL, ?, ?, ?)", params)
        db.commit()
        db_cursor.close()
        # List users in db
        select_cursor = db.cursor()
        select_cursor.execute("select * from REGISTER ")
        print(select_cursor.fetchall())
        select_cursor.close()
    except sqlite3.ProgrammingError as e:
        pass

    # Csv entry done here
    with open('register/attendance.csv', mode='w') as attendance_file:
        attendance_writer = csv.writer(attendance_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        attendance_writer.writerow(data)


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./recognizers/trainer.yml')
cascadePath = "./cascades/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Sebastian ', 'Opiyo', 'Ilza', 'Z', 'W']

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    # img = cv2.flip(img, -1)  # Flip vertically in case the image is inverted
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Check if confidence is less than 100 ==> "0" is perfect match
        if confidence < 100:
            id_name = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            write_to_csv(id_name)  # write to db instead
        else:
            id_name = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            write_to_csv(id_name)

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
