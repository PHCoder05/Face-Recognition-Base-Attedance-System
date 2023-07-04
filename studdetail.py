import tkinter as tk
from tkinter import ttk
import pandas as pd

class StudentDetailsGUI:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)
        self.root = tk.Tk()
        self.root.title("Student Details")
        self.root.geometry("800x400")
        self.root.resizable(0, 0)
        self.root.config(bg="#F9F9F9")
        # Create a title label
        title_label = tk.Label(self.root, text="Student Details", font=("Helvetica", 40, "bold"), bg="#F9F9F9", fg="#333333")
        title_label.pack(pady=20)


        # Create a separator
        sep = ttk.Separator(self.root, orient="horizontal")
        sep.pack(fill="x", pady=10)
       
         
        # Create a table frame
        table_frame = tk.Frame(self.root, bg="#F9F9F9")
        table_frame.pack(padx=20, pady=20)

        # Create a canvas
        canvas = tk.Canvas(table_frame, bg="#F9F9F9")
        canvas.pack(side="left", fill="both", expand=True)

        # Create a scroll bar
        scroll_bar = ttk.Scrollbar(table_frame, orient="vertical", command=canvas.yview)
        scroll_bar.pack(side="right", fill="y")

        # Configure the canvas to use the scroll bar
        canvas.configure(yscrollcommand=scroll_bar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold the table
        table_inner_frame = tk.Frame(canvas, bg="#F9F9F9")
        canvas.create_window((0, 0), window=table_inner_frame, anchor="nw")

        # Create table header
        headers = ["Enrollment", "Name"]
        for i, header in enumerate(headers):
            label = tk.Label(table_inner_frame, text=header, font=("Helvetica", 16), bg="#F9F9F9", fg="#333333", width=20, anchor="w")
            label.grid(row=0, column=i, padx=5, pady=5)

        # Create table rows
        for i in range(len(self.df)):
            id_ = self.df.iloc[i]["Enrollment"]
            name = self.df.iloc[i]["Name"]

            id_label = tk.Label(table_inner_frame, text=id_, font=("Helvetica", 14), bg="#F9F9F9", fg="#333333", width=20, anchor="w")
            id_label.grid(row=i+1, column=0, padx=5, pady=5)

            name_label = tk.Label(table_inner_frame, text=name, font=("Helvetica", 14), bg="#F9F9F9", fg="#333333", width=20, anchor="w")
            name_label.grid(row=i+1, column=1, padx=5, pady=5)

        # Create a separator
        sep2 = ttk.Separator(self.root, orient="horizontal")
        sep2.pack(fill="x", pady=10)

        # Create a button to close the window
        close_button = tk.Button(self.root, text="Close", font=("Helvetica", 12), bg="#E0E0E0", fg="#333333", command=self.root.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    app = StudentDetailsGUI("StudentDetails/studentdetails.csv")
    app.root.mainloop()
