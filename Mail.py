import calendar
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
import tkinter

def send_email(self):
    email = self.email_entry.get()
    subject = self.selected_option.get()
    file_path = f"C:\\Users\\HP\\Dropbox\\PC\\Desktop\\Final-Project\\New folder\\Attendance-Management-system-using-face-recognition-master\\Attendance\\{subject}\\attendance.csv"
    
    # Get current month and time information
    now = datetime.datetime.now()
    month_name = calendar.month_name[now.month]
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Create message object instance
    message = MIMEMultipart()
    message['From'] = 'frbasadmi2023@gmail.com'
    message['To'] = email
    message['Subject'] = f"Attendance of {subject} ({month_name} {now.year})"
    
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
    tkinter.messagebox.showinfo("Email Sent", f"Attendance sheet of {subject} for {month_name} {now.year} has been sent to {email} at {time_str}.")
