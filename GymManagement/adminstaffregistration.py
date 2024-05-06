import customtkinter
from PIL import Image, ImageTk
import pyodbc
import subprocess
from tkinter import messagebox

app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Staff Management")

# Establish a connection to the SQL Server database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open admin dashboard
def open_admin_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])

# Function to handle registration button click event
def register_button_click():
    try:
        # Retrieve data entered by the user
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        designation = desig_menu.get() 
        # Retrieve selected designation from option menu
        contact = contact_entry.get()  
        dob = dob_year_option_menu.get() + '-' + str(dob_month_option_menu.get()) + '-' + dob_day_option_menu.get()  # Assuming you have separate day, month, year option menus for date of birth
        # Retrieve other data fields similarly...
        gender = gender_option_menu.get()

        # Construct SQL INSERT statement
        sql_insert = "INSERT INTO Staff (EmployeeFirstName, EmployeeLastName, EmployeeUsername, EmployeePassword, EmployeeDesignation, EmployeeConatct, EmployeeDateOfBirth,  EmployeeGender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

        # Execute the INSERT statement
        cursor = connection.cursor()
        cursor.execute(sql_insert, (first_name, last_name, username, password, designation, contact, dob, gender))
        connection.commit()
        cursor.close()

        # Show success message box
        messagebox.showinfo("Success", "Registration successful!")

    except Exception as e:
        # Show error message box and print SQL error
        error_message = f"Error during registration:\n{str(e)}"
        messagebox.showerror("Error", error_message)
        print(error_message)


# left frame
frameLeft = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#0b5394', corner_radius=0)
frameLeft.grid(row = 0, column = 0, sticky = "nsew")

# right frame
frameRight = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#24272C', corner_radius=0)
frameRight.grid(row = 0, column = 1, stick = "nsew")

# Set resizeable to full screen
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Login in page main image
login_page_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Staff.png"), dark_image = Image.open("Pictures/Staff.png"), size = (400,400))
login_page_image_label = customtkinter.CTkLabel(frameLeft, text = "", image = login_page_image)
login_page_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (65,65))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")

# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#3d85c6")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "Management System", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# sign up label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "STAFF REGISTERATION", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
sign_up_label.place(relx = 0.5, rely = 0.27, anchor = "center")

# first name underline
first_name_line = customtkinter.CTkFrame(frameRight, width=197, height=3, bg_color="white")  # Set background color to white
first_name_line.place(relx=0.75, rely=0.38, anchor="e")


# last name underline
last_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, bg_color="white")
last_name_line.place(relx = 0.75, rely = 0.46, anchor = "e")

# first Name label
first_name_label = customtkinter.CTkLabel(frameRight, text = "First Name", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
first_name_label.place(relx = 0.25, rely = 0.36, anchor = "center")

# last name label
last_name_label = customtkinter.CTkLabel(frameRight, text = "Last Name", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
last_name_label.place(relx = 0.25, rely = 0.44, anchor = "center")

# first name entry field
first_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g John", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
first_name_entry.place(relx= 0.75, rely = 0.36, anchor = "e")

# last name entry field
last_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g Doe", width = 200, height = 28, fg_color="#24272C", border_width=0,  text_color="white")
last_name_entry.place(relx= 0.75, rely = 0.44, anchor = "e")

# username label
username_label = customtkinter.CTkLabel(frameRight, text = "Username", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.52, anchor = "center")

# username entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g johndoe", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
username_entry.place(relx= 0.75, rely = 0.52, anchor = "e")

# password label
password_label = customtkinter.CTkLabel(frameRight, text="Password", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF", )
password_label.place(relx=0.25, rely=0.60, anchor="center")

# password entry field
password_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g JohnDoe$1986", width=200, height=28, fg_color="#24272C", border_width=0, text_color="white", show="*")
password_entry.place(relx=0.75, rely=0.60, anchor="e")

# password underline
password_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
password_line.place(relx=0.75, rely=0.62, anchor="e")


# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.62, anchor = "e")

#contact label
contact_label = customtkinter.CTkLabel(frameRight, text = "Contact No", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
contact_label.place(relx = 0.25, rely = 0.68, anchor = "center")

# contact entry field
contact_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g 03001234567", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
contact_entry.place(relx= 0.75, rely = 0.68, anchor = "e")

# contact underline
contact_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
contact_line.place(relx = 0.75, rely = 0.70, anchor = "e")

#dob label
DoB_label = customtkinter.CTkLabel(frameRight, text = "Birth Date", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
DoB_label.place(relx = 0.25, rely = 0.76, anchor = "center")

#dob day option menu
dob_day_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range(1, 32)], width=60, fg_color="#000000", button_color="#000000")
dob_day_option_menu.set("1")
dob_day_option_menu.place(relx = 0.41, rely = 0.76, anchor = "center")

#dob month option menu
dob_month_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], width=100, fg_color="#000000", button_color="#000000")
dob_month_option_menu.set("01")
dob_month_option_menu.place(relx = 0.595, rely = 0.76, anchor = "center")

#dob year option menu
dob_year_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range (1950, 2025)], width = 60, fg_color="#000000", button_color="#000000")
dob_year_option_menu.set("2000")
dob_year_option_menu.place(relx = 0.79, rely = 0.76, anchor = "center")

#gender label
gender_label = customtkinter.CTkLabel(frameRight, text = "Gender", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
gender_label.place(relx = 0.23, rely = 0.84, anchor = "center")

#gender option menu
gender_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['Male', 'Female'], width = 100, fg_color="#000000", button_color="#000000")
gender_option_menu.set("Male")
gender_option_menu.place(relx = 0.31, rely = 0.84, anchor = "w")

# Register button
register_button = customtkinter.CTkButton(frameRight, text="REGISTER", corner_radius=35, fg_color="#0b5394", command=register_button_click)
register_button.place(relx=0.29, rely=0.91, anchor="center")


# back button
back_button = customtkinter.CTkButton(frameRight, text = "Go Back", corner_radius=35, fg_color="#0b5394", command=open_admin_dashboard)
back_button.place(relx = 0.65, rely = 0.91, anchor = "center")


#designation label
desig_label = customtkinter.CTkLabel(frameRight, text = "Designation", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
desig_label.place(relx = 0.63, rely = 0.84, anchor = "center")


#Designation
desig_menu = customtkinter.CTkOptionMenu(frameRight, values=['Trainer', 'Non-Functional', 'Functional'], width = 100, fg_color="#000000", button_color="#000000")
desig_menu.set("Trainer")
desig_menu.place(relx = 0.75, rely = 0.84, anchor = "w")


app.mainloop()