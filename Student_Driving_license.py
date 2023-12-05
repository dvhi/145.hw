# Basic tkinter template
from tkinter import *

root = Tk()

root.title("Drivers License")
root.geometry("300x400")

root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")
label_heading = canvas.create_text(150, 90, font=('Times','24','bold italic'), text="Identity Card")
label_name_tag = canvas.create_text(40, 165, font=('Times','16','bold'), text="Name : ")
label_grade_tag = canvas.create_text(40, 205, font=('Times','16','bold'), text="Grade : ")
label_subjects_tag = canvas.create_text(40, 250, font=('Times','16','bold'), text="Subjects : ")
label_name = Label(root)
label_grade = Label(root)
label_subjects = Label(root)


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID : 23864705637")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :Dhanush Vijay")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :May 26, 2002")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :287569")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :2896 Ocean Dr.")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles : Two, Four")

# Create all the labels required to be displayed



# Define the function

    
    
# Create a button

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
