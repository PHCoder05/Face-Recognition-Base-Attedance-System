import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech):
    def calculate_attendance():
        # get the selected subject
        Subject = selected_option.get()
        
        # check if a subject is selected
        if Subject=="":
            t='Please enter the subject name.'
            text_to_speech(t)
        
        # change the working directory to the subject folder
        os.chdir(f"C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\{Subject}")
        
        # get all CSV files in the subject folder
        filenames = glob(f"C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\{Subject}\\{Subject}*.csv")
        
        # read each CSV file and merge them into a single DataFrame
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        
        # fill missing values with 0 and calculate the attendance percentage for each student
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
        
        # sort the DataFrame by enrollment number and save it to a CSV file
        newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv("attendance.csv", index=False)
        
        # filter students with attendance less than 70%
        low_attendance = newdf[newdf['Attendance'] < '70']
        
        # save attendance list to a separate file
        low_attendance.to_csv(f"low_attendance.csv", index=False)

        

        root = tkinter.Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="black")
        cs = f"C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\{Subject}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="#3a5978")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        text="Which Subject of Attendance?",
        bg="black",
        fg="yellow",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():
        sub =selected_option.get()
        if sub == "":
            t="Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(
            f"C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\{sub}\\low_attendance.csv"
            )


    attf = tk.Button(
        subject,
        text="View Low Attendance",
        command=Attf,
        bd=7,
        font=("times new roman", 14),
        bg="black",
        fg="yellow",
        height=2,
        width=18,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

   
    options = ["Select Subject","Javascript", "CCS", "CNS", "Linux","ETCMIT","GUI.NET"]
    selected_option = tk.StringVar(subject)
    selected_option.set(options[0])

    tx = tk.OptionMenu(
        subject,
        selected_option,
        *options,
    )
    tx.config(
        width=15,
        bd=5,
        bg="#3a5978",
        fg="yellow",
        relief=tk.RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=185, y=170)
    subject.mainloop()
