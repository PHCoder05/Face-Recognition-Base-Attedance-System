
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