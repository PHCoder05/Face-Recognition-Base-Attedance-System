import calendar
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
from PIL import Image, ImageTk
# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import filedialog
import smtplib
from email.mime.base import MIMEBase
from email import encoders


# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

haarcasecade_path = "C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\haarcascade_frontalface_alt.xml"
trainimagelabel_path = (
    "C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance"

import os
from tkinter import *
from tkinter import ttk

# Creating a tkinter window
# root = Tk()
# root.geometry('1366x768')
# root.title("Facial Recognition Attendance System Login")


# # Loading the image
# image = Image.open("photo_2023-04-05_23-34-27.jpg")
# background = ImageTk.PhotoImage(image)

# # Displaying the image
# background_label = Label(root, image=background)
# background_label.place(relwidth=1, relheight=1)

# # # Creating a background image
# # bg = PhotoImage(file="background.png")
# # background = Label(root, image=bg)
# # background.place(relwidth=1, relheight=1)

# # Creating a frame for the login form
# login_frame = Frame(root, bd=5)
# login_frame.place(relx=0.5, rely=0.5, anchor='center')

# # Creating a label for the login form
# login_label = Label(login_frame, text="Login to Access the System", font=("Helvetica", 24))
# login_label.pack(pady=20)

# # Creating a label and entry box for the username
# username_label = Label(login_frame, text="Username:", font=("Helvetica", 14))
# username_label.pack(pady=10)
# username_entry = Entry(login_frame, width=30, font=("Helvetica", 14))
# username_entry.pack(pady=5)

# # Creating a label and entry box for the password
# password_label = Label(login_frame, text="Password:", font=("Helvetica", 14))
# password_label.pack(pady=10)
# password_entry = Entry(login_frame, width=30, show='*', font=("Helvetica", 14))
# password_entry.pack(pady=5)

# # Creating a function for authentication
# def login():
#     username = username_entry.get()
#     password = password_entry.get()
#     root.destroy()

#     # Add your authentication code here
    
#     if username == "admin" and password == "12345":
#       message_label.config(text="login Succesfully", fg="red")
#     else:
#         message_label.config(text="Invalid credentials", fg="red")

# # Creating a button for logging in
# login_button = Button(login_frame, text="Login", command=login, bg="green", fg="white", font=("Helvetica", 14))
# login_button.pack(pady=20)

# # Creating a label for error messages
# message_label = Label(login_frame, font=("Helvetica", 12))
# message_label.pack(pady=5)

# # Running the tkinter window
# root.mainloop()
                 
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d:%m:%Y")
    # print(time_string , date_string)
    clock.config (text = "Time :" + time_string  + "\n" + "Date :" + date_string)
    clock.after(200,tick)

########################################### Admin Login page #############
from tkinter import GROOVE, LEFT, Button, Entry, Frame, Label, PhotoImage, StringVar, Tk, messagebox
import tkinter
import pymysql

face = Tk()
face.title("Admin Login Page")
face.geometry("1350x700+0+0")
face.iconbitmap("Photos/Aha-Soft-Free-Large-Boss-Admin.ico")
    ##  variables for login##
username_var = StringVar()
password_var = StringVar()
oldpass_var = StringVar()
user_var = StringVar()
newpass_var = StringVar()
def login():
    if username_var.get() == "" or password_var.get() == "":
        messagebox.showerror('Error','All the fields are required', parent = face)
    else:
      
            conn = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'recognition')
            curr = conn.cursor()
            curr.execute('select * from login where username = %s and password = %s',(username_var.get(), password_var.get()))
            row = curr.fetchone()
            if row == None:
                messagebox.showerror('Error','Invalid Data')

            else:
                face.destroy()
########################## Admin login page form ####################################
bg_icon = PhotoImage(file = "Photos/background.png", master = face)
background_image = Label(face, image = bg_icon)
background_image.pack()

title = Label(face, text = "Admin Login Page" , font = ("times new roman", 30, "bold"), bg = "green", fg = "yellow", bd = 7, relief = GROOVE) 
title.place(x = 0, y = 0, relwidth = 1)

clock = Label(face , font = ("times",20,"bold"), bg = "green", relief = GROOVE)
clock.place(x = 1000, y= 600)
tick()

login_frame= Frame(face, bg = "white" )
login_frame.place(x = 400, y = 200)
logo_icon = PhotoImage(file = "Photos/logo.png", master= login_frame)
logo_image = Label(login_frame, image = logo_icon, bd = 0 ).grid( row = 0, columnspan = 3 , pady = 40, padx= 40)
user_icon = PhotoImage(file = "Photos/user.png", master = login_frame)
password_icon = PhotoImage(file = "Photos/password.png", master = login_frame)
user_label = Label(login_frame , text = "Username", image = user_icon, bg= "white", compound = LEFT, font = ("times new roman", 15, "bold")).grid( row  = 1 , column = 0, padx = 30, pady = 5)
user_entry = Entry(login_frame, font = ("times new roman", 15, "bold"), relief = GROOVE, textvariable = username_var, bg = "lightgray").grid(row = 1, column= 1, padx= 10, pady = 5)
password_label = Label(login_frame, text = "Password", image = password_icon, bg ="white", compound = LEFT, font = ("times new roman", 15, "bold")).grid(row = 2, column = 0, padx = 30, pady = 5)
password_entry = Entry(login_frame, show = "*", font = ("times new roman", 15,"bold"), relief = GROOVE, textvariable = password_var, bg = "lightgray").grid(row = 2, column = 1, padx = 20, pady = 5)
submit_btn = Button(login_frame, text = "Log In",width = 10, activebackground = "blue", activeforeground = "white", command = login , font = ("times new roman", 20, "bold"),relief = GROOVE, bg = "green").grid(row = 3, column = 1, pady =25, padx = 25) 
face.mainloop()      


window = Tk()
window.title("Face recognizer")
window.geometry("1350x800+0+0")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
# window.configure(background="white")
from PIL import Image, ImageTk

img =Image.open('C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\UI_Image\\bgImage1.jpg')
bg = ImageTk.PhotoImage(img)
window.geometry("1600x716")

# Add image
label = Label(window, image=bg)
label.place(x = 0,y = 0)

# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="white")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="#0000b3",
        bg="white",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="#0000b3",
        bg="white",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.Resampling.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="black",)
l1.place(x=470, y=10)

titl = tk.Label(
    window, text="Smart College!!", bg="black", fg="yellow", font=("arial", 27),
)
titl.place(x=525, y=12)

# a = tk.Label(
#     window,
#     text="Welcome to the Face Recognition Based\nAttendance Management System",
#     bg="white",
#     fg="#0000b3",
#     bd=10,
#     font=("arial", 35),
# )
# a.pack()

# ri = Image.open("UI_Image/register.jpg")
# r = ImageTk.PhotoImage(ri)
# label1 = Label(window, image=r)
# label1.image = r
# label1.place(x=380, y=270)

# vi = Image.open("UI_Image/verifyy.jpg")
# v = ImageTk.PhotoImage(vi)
# label3 = Label(window, image=v)
# label3.image = v
# label3.place(x=650, y=270)

# ai = Image.open("UI_Image/attendance.jpg")
# a = ImageTk.PhotoImage(ai)
# label2 = Label(window, image=a)
# label2.image = a
# label2.place(x=980, y=270)




def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x520")
    ImageUI.configure(background="#3a5978")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="black", fg="yellow", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#3a5978",
        fg="yellow",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

 # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=8,
        relief=RIDGE,
        font=("times", 11,"bold"),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#3a5978",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12,"bold"),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#3a5978",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

 
    txt4 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#3a5978",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt4.place(x=250, y=270)

    # year
    lbl3 = tk.Label(
        ImageUI,
        text="Email",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12,"bold"),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#3a5978",
        fg="yellow",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=340)

    # Notification
    lbl5 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12,"bold"),
    )
    lbl5.place(x=120, y=340)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        l3 = txt4.get()
        takeImage.TakeImage(
            l1,
            l2,
            l3,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")
        txt4.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18,"bold"),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=120, y=430)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18,"bold"),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=430)



r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 12, "bold"),
    bg="#3a5978",
    fg="yellow",
    height=1,
    width=19,
)
r.place(x=660, y=540)

def quit():
    window.destroy()
    
def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication

# def send_report():
#     # Define the sender and recipient email addresses
#     sender_email = "frbasadmi2023@gmail.com"
#     recipient_email = "pankajhadole4@gmail.com"

#     # Define the email subject and body
#     subject = "Monthly Report"
#     body = "Attached is the report for the month of April."

#     # Define the file path of the report file
#     report_file_path = "C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\CCS\\attendance.csv"

#     # Create a MIME multipart message object
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = recipient_email
#     message["Subject"] = subject

#     # Add the email body to the message
#     message.attach(MIMEText(body, "plain"))

#     # Open the report file and add it as an attachment to the message
#     with open(report_file_path, "rb") as report_file:
#         report_part = MIMEApplication(report_file.read(), Name="report.pdf")
#         report_part["Content-Disposition"] = f"attachment; filename={report_file_path}"
#         message.attach(report_part)

#     # Send the email using SMTP
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     smtp_username = "frbasadmi2023@gmail.com"
#     smtp_password = "zxdswaqjibzhsqec"

#     with smtplib.SMTP(smtp_server, smtp_port) as smtp:
#         smtp.starttls()
#         smtp.login(smtp_username, smtp_password)
#         smtp.sendmail(sender_email, recipient_email, message.as_string())
def send_report():
    class AttendanceSheetSender:
        def __init__(self):
           self.root = tk.Tk()
           self.root.title("Attendance Sheet Sender")
           self.root.geometry("400x300")
           self.root.configure(bg="#3a5978")

           tk.Label(self.root, text="Email Address:").grid(row=0, column=0, padx=10, pady=10)
           self.email_entry = tk.Entry(self.root)
           self.email_entry.grid(row=0, column=1, padx=10, pady=10)

           tk.Label(self.root, text="Select Subject:").grid(row=1, column=0, padx=10, pady=10)
           self.options = ["Select Subject","Javascript", "CCS", "CNS", "Linux","ETCMIT","GUI.NET"]
           self.selected_option = tk.StringVar(self.root)
           self.selected_option.set(self.options[0])
           self.subject_menu = tk.OptionMenu(self.root, self.selected_option, *self.options)
           self.subject_menu.grid(row=1, column=1, padx=10, pady=10)

           tk.Label(self.root, text="Attendance Type:").grid(row=2, column=0, padx=10, pady=10)
           self.attendance_options = ["attendance", "low_attendance"]
           self.select_attendance = tk.StringVar(self.root)
           self.select_attendance.set(self.attendance_options[0])
           self.attendance_menu = tk.OptionMenu(self.root, self.select_attendance, *self.attendance_options)
           self.attendance_menu.grid(row=2, column=1, padx=10, pady=10)

           tk.Button(self.root, text="Send Email", command=self.send_email).grid(row=3, column=1, padx=10, pady=10)


        def send_email(self):
            email = self.email_entry.get()
            sub = self.selected_option.get()
            type = self.select_attendance.get()

              
            file_path = f"C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\{sub}\\{type}.csv"

            if not os.path.exists(file_path):
                messagebox.showerror("File Not Found", f"Attendance sheet for {sub} not found!")
                return
            
            # Get current month and time information
            now = datetime.datetime.now()
            month_name = calendar.month_name[now.month]
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                    # Create message object instance
            message = MIMEMultipart()
            message['From'] = 'frbasadmi2023@gmail.com'
            message['To'] = email


            if(self.select_attendance.get()=="attendance"):   

             message['Subject'] = f"Attendance of {sub} ({month_name} {now.year})"
        
             # Add body to email
             bodyi = f"Hi,\n\nPlease find the attendance sheet for {sub} attached.\n\nThanks and regards,\nAttendance System"
             message.attach(MIMEText(bodyi, 'plain'))

            if not(self.select_attendance.get()=="attendance"):
                 message['Subject'] = f"You Have Low Attendance of {sub} ({month_name} {now.year})"
        
             # Add body to email
                 body = f"Hi,\n\nPlease find the attendance sheet for {sub} attached.\n\nThanks and regards,\nAttendance System"
                 message.attach(MIMEText(body, 'plain'))

            # Attach attendance sheet to email
            with open(file_path, "rb") as f:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', "attachment; filename= %s" % "attendance_sheet.csv")
                message.attach(attachment)

            # Create SMTP session
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login('frbasadmi2023@gmail.com', 'zxdswaqjibzhsqec')

            # Send mail
            text = message.as_string()
            session.sendmail('frbasadmi2023@gmail.com', email, text)
            session.quit()

            # Show success message
            messagebox.showinfo("Email Sent", "Attendance sheet has been sent to {}!".format(email))

    if __name__ == "__main__":
        app = AttendanceSheetSender()
        app.root.mainloop()
import tkinter as tk
from tkinter import ttk
import pandas as pd
import tkinter as tk
from tkinter import ttk
import pandas as pd

def studentdetails():

    class StudentDetailsGUI:
        def __init__(self, filename):
            self.df = pd.read_csv(filename)

            self.root = tk.Tk()
            self.root.title("Student Details")
            self.root.bg="#3a5978"
            self.root.configure(bg="#3a5978")

            # Create a frame for the table
            table_frame = tk.Frame(self.root)
            table_frame.pack(padx=10, pady=10)

            # Create a label for the table
            table_label = tk.Label(table_frame, text="Student Details", font=("Helvetica", 18, "bold"), fg="#333333")
            table_label.pack(padx=10, pady=10)

            # Create a frame for the inner table
            table_inner_frame = tk.Frame(table_frame)
            table_inner_frame.pack()

            # Create table headers
            id_header = tk.Label(table_inner_frame, text="Enrollment", font=("Helvetica", 14, "bold"), bg="#E0E0E0", fg="#333333", width=20, anchor="w")
            id_header.grid(row=0, column=0, padx=5, pady=5)

            name_header = tk.Label(table_inner_frame, text="Name", font=("Helvetica", 14, "bold"), bg="#E0E0E0", fg="#333333", width=20, anchor="w")
            name_header.grid(row=0, column=1, padx=5, pady=5)

            if "Email" in self.df.columns:
                email_header = tk.Label(table_inner_frame, text="Email", font=("Helvetica", 14, "bold"), bg="#E0E0E0", fg="#333333", width=30, anchor="w")
                email_header.grid(row=0, column=2, padx=5, pady=5)

            # Create table rows
            for i in range(len(self.df)):
                id_ = self.df.iloc[i]["Enrollment"]
                name = self.df.iloc[i]["Name"]
                email = self.df.iloc[i]["Email"] if "Email" in self.df.columns else ""

                id_label = tk.Label(table_inner_frame, text=id_, font=("Helvetica", 14), bg="#F9F9F9", fg="#333333", width=20, anchor="w")
                id_label.grid(row=i+1, column=0, padx=5, pady=5)

                name_label = tk.Label(table_inner_frame, text=name, font=("Helvetica", 14), bg="#F9F9F9", fg="#333333", width=20, anchor="w")
                name_label.grid(row=i+1, column=1, padx=5, pady=5)

                email_label = tk.Label(table_inner_frame, text=email, font=("Helvetica", 14), bg="#F9F9F9", fg="#333333", width=30, anchor="w")
                email_label.grid(row=i+1, column=2, padx=5, pady=5) if "Email" in self.df.columns else None

            # Create a separator
            sep2 = ttk.Separator(self.root, orient="horizontal")
            sep2.pack(fill="x", pady=10)

            # Create a button to close the window
            close_button = tk.Button(self.root, text="Close", font=("Helvetica", 12), bg="#E0E0E0", fg="#333333", command=self.root.destroy)
            close_button.pack(pady=10)

        def run(self):
            self.root.mainloop()

    if __name__ == "__main__":
        app = StudentDetailsGUI("C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\StudentDetails\\studentdetails.csv")
        app.root.mainloop()


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 12,"bold"),
    bg="#3a5978",
    fg="yellow",
    height=1,
    width=19,
)
r.place(x=878, y=540)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 12,"bold"),
    bg="#3a5978",
    fg="yellow",
    height=1,
    width=19,
)
r.place(x=1099, y=540)
r = tk.Button(
    window,
    bd=10,
    text="Send Report ",
    command=send_report,
    font=("times new roman", 12,"bold"),
    bg="#3a5978",
    fg="yellow",
    height=1,
    width=19,
)
r.place(x=660, y=610)

r = tk.Button(
    window,
    text="EXIT ",
    command=quit,
    bd=10,
    font=("times new roman", 12,"bold"),
    bg="#3a5978",
    fg="yellow",
    height=1,
    width=19,
)
r.place(x=878, y=610)

r = tk.Button(
    window,
    text="student List ",
    command=studentdetails,
    bd=10,
    font=("times new roman", 12,"bold"),
    bg="#3a5978",
    fg="yellow",
    height=1,
    width=19,
)
r.place(x=1099, y=610)


window.mainloop()
