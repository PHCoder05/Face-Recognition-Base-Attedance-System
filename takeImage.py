import csv
import os
import cv2
import numpy as np
import pandas as pd
import datetime
import time

def validate_email(email):
    if '@' not in email:
        return False
    else:
        domain = email.split('@')[1]
        if '.' not in domain:
            return False
    return True
# Check if the given email already exists in the CSV file
def check_email_exists(email):
    with open('StudentDetails/studentdetails.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            if email == row[2]:
                return True
    return False

# take Image of user
def TakeImage(l1, l2, l3, haarcasecade_path, trainimage_path, message, err_screen, text_to_speech):
    # Check if all the input fields are provided
    if l1 == "" and l2 == "" and l3 == "":
        t = 'Please enter your enrollment number, name and email.'
        text_to_speech(t)
    
    # Check if the enrollment number is provided
    elif l1 == "":
        t = 'Please enter your enrollment number.'
        text_to_speech(t)
    
    # Check if the name is provided
    elif l2 == "":
        t = 'Please enter your name.'
        text_to_speech(t)
    
    # Check if the email is provided
    elif l3 == "":
        t = 'Please enter your email.'
        text_to_speech(t)

     # Check if the email is provided
    elif l1 == ""and l2== "":
        t = 'Please enter nrollment number and name.'
        text_to_speech(t)

          # Check if the email is provided
    elif l1 == ""and l3== "":
        t = 'Please enter nrollment number and Email.'
        text_to_speech(t)
    
    # If all the input fields are provided
    else:
        # Check if the email is valid
        if not validate_email(l3):
            t = 'Please enter a valid email address.'
            text_to_speech(t)
            return
        
        # Check if the email already exists in the CSV file
        if check_email_exists(l3):
            t = 'This email already exists.'
            text_to_speech(t)
            return
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            Enrollment = l1
            Name = l2
            Email = l3
            sampleNum = 0
            directory = Enrollment + "_" + Name
            path = os.path.join(trainimage_path, directory)
            os.makedirs(path, exist_ok=True)
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum = sampleNum + 1
                    cv2.imwrite(f"{path}/" + Name + "_" + Enrollment + "_" + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum > 100:
                    break
            cam.release()
            cv2.destroyAllWindows()
            row = [Enrollment, Name, Email]
            with open('StudentDetails\studentdetails.csv', 'a+', newline='') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(row)
            res = "Images Saved for ER No:" + Enrollment + " Name:" + Name + " Email:" + Email
            message.configure(text=res)
            text_to_speech(res)
        except FileExistsError as F:
            F = "Student Data already exists"
            text_to_speech(F)
