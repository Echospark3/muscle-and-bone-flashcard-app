import tkinter as tk
from tkinter import filedialog
import csv

def open_csv_data():
    file_path = 

root = tk.Tk()

root.geometry("500x500")
root.title("my human anatomy assistant")

label = tk.Label(root,text = "SUBMIT YOUR ANSWERS HERE V",font= ('Arial',18))
label.pack(padx=20, pady=30)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

nextbtn = tk.Button(root, text="Next")
nextbtn.place(x=420, y=176, height=40, width=80)

previousbtn = tk.Button(root, text="previous")
previousbtn.place(x=0, y=176, height=40, width=80)


buttonframe.pack(fill='x')










root.mainloop()
