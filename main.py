# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


import cv2
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)


start_time = None
total_working_time = 0

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        start_time = None
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            if len(eyes) > 0:
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                if start_time is None:
                    start_time = time.time()
                else:
                    total_working_time += time.time() - start_time
                    start_time = time.time()

                    
                    hours = int(total_working_time / 3600)
                    minutes = int(total_working_time / 60) % 60
                    seconds = int(total_working_time % 60)
                    milliseconds = int((total_working_time - int(total_working_time)) * 1000)

                    # Print the productive time in hours, minutes, and seconds format
                    print("Productive time: {:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds))

               # print("Productive time: {:.2f} seconds".format(total_working_time))

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Total working time: {:.2f} seconds".format(total_working_time))
