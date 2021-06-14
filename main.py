from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Registration Screen")

window.geometry('1000x900')

window.configure(background="yellow")

Firstname = Label(window, text="First Name").grid(row=0, column=0)
LastName = Label(window, text="Last Name").grid(row=1, column=0)
Employee_id = Label(window, text="Employee id").grid(row=2, column=0)
Gender = Label(window, text="Gender").grid(row=3, column=0)
Job_title = Label(window, text="Job Title").grid(row=4, column=0)
Department = Label(window, text="Department ").grid(row=5, column=0)
Department_id = Label(window, text="Department id").grid(row=6, column=0)
Salary = Label(window, text="Salary").grid(row=7, column=0)
Email = Label(window, text="Email Id").grid(row=8, column=0)
Mobile = Label(window, text="Contact Number").grid(row=9, column=0)

Firstname1 = Entry(window).grid(row=0, column=1)
Lastname1 = Entry(window).grid(row=1, column=1)
Employee_id1 = Entry(window).grid(row=2, column=1)
Gender1 = Entry(window).grid(row=3, column=1)
Job_title1 = Entry(window).grid(row=4, column=1)
Department1 = Entry(window).grid(row=5, column=1)
Department_id1 = Entry(window).grid(row=6, column=1)
Salary = Entry(window).grid(row=7, column=1)
Email1 = Entry(window).grid(row=8, column=1)
Mobile1 = Entry(window).grid(row=9, column=1)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=11,column=0)
window.mainloop()

