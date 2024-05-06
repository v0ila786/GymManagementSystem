import customtkinter
from PIL import Image, ImageTk
import subprocess
from datetime import datetime
import pyodbc
from tkinter import ttk, messagebox

def show_registration_message():
    messagebox.showinfo("Registration Successful", "User registered successfully!")

def open_staff_registration():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])


 # Establish a connection to the SQL Server database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()      


def register_user():
    try:
        # Retrieve user input
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        contact_number = contact_entry.get()
        dob_day_value = int(dob_day_option_menu.get())
        dob_month = dob_month_option_menu.get()
        dob_year = int(dob_year_option_menu.get())
        gender = gender_option_menu.get()
        # Convert month string to integer
        dob_month_int = datetime.strptime(dob_month, "%B").month
        # Construct the date of birth (dob) variable
        dob_date = datetime(dob_year, dob_month_int, dob_day_value).date()
        # get the payment plan
        payment_plan = payment_plan_option_menu.get()
        # Insert into Customers table
        insert_user_query = """
            INSERT INTO Customers (
                CustomerUsername, 
                CustomerPassword, 
                CustomerFirstName, 
                CustomerLastName, 
                CustomerContactNumber, 
                CustomerDateOfBirth, 
                CustomerGender
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_user_query, (
            username,
            password,
            first_name,
            last_name,
            contact_number,
            dob_date,
            gender
        ))

        # Get the newly inserted UserID
        cursor.execute("SELECT @@IDENTITY AS UserID;")
        next_user_id = cursor.fetchone().UserID

        # Insert into Gymuserpayment table
        insert_payment_query = """
                    INSERT INTO CustomerPayments (
                        UserID,
                        payment_plan
                    )
                    VALUES (?, ?)
                """
        cursor.execute(insert_payment_query, (next_user_id, payment_plan))

        # Commit the transaction
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Show registration message
        show_registration_message()

        # Reset entry fields
        first_name_entry.delete(0, 'end')
        last_name_entry.delete(0, 'end')
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
        contact_entry.delete(0, 'end')
        # Add similar lines for other entry fields
    except Exception as e:
        print(f"Error: {e}")

app = customtkinter.CTk()

app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

# left frame
frameLeft = customtkinter.CTkFrame(app, width = 450, height = 700, fg_color='#0b5394', corner_radius=0)
frameLeft.grid(row = 0, column = 0, sticky = "nsew")

# right frame
frameRight = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#24272C', corner_radius=0)
frameRight.grid(row = 0, column = 1, stick = "nsew")

# Set resizeable to full screen
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Login in page main image
login_page_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Boxing Man.png"), dark_image = Image.open("Pictures/Boxing Man.png"), size = (400,400))
login_page_image_label = customtkinter.CTkLabel(frameLeft, text = "", image = login_page_image)
login_page_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (75,75))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")

# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#3d85c6")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "GYM Management (ADMIN)", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# sign up label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "NEW MEMBER REGISTRATION", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
sign_up_label.place(relx = 0.5, rely = 0.27, anchor = "center")

# first name underline
first_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
first_name_line.place(relx = 0.75, rely = 0.38, anchor = "e")

# last name underline
last_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
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
last_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g Doe", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
last_name_entry.place(relx= 0.75, rely = 0.44, anchor = "e")

# username label
username_label = customtkinter.CTkLabel(frameRight, text = "Username", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.52, anchor = "center")

# username entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g johndoe", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
username_entry.place(relx= 0.75, rely = 0.52, anchor = "e")

# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.54, anchor = "e")

#password label
username_label = customtkinter.CTkLabel(frameRight, text = "Password", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.60, anchor = "center")

# Password entry field
password_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g JohnDoe$1986", width=200, height=28, fg_color="#24272C", border_width=0, show="*", text_color="white")
password_entry.place(relx=0.75, rely=0.60, anchor="e")

# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.62, anchor = "e")

#contact label
username_label = customtkinter.CTkLabel(frameRight, text = "Contact No", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.26, rely = 0.68, anchor = "center")

# Contact entry field
contact_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g 03001234567", width=200, height=28, fg_color="#24272C", border_width=0, text_color="white")
contact_entry.place(relx=0.75, rely=0.68, anchor="e")

# contact underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.70, anchor = "e")

#dob label
username_label = customtkinter.CTkLabel(frameRight, text = "Birth Date", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.76, anchor = "center")

#dob day option menu
dob_day_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range(1, 32)], width=60, fg_color="#000000", button_color="#000000")
dob_day_option_menu.set("1")
dob_day_option_menu.place(relx = 0.41, rely = 0.76, anchor = "center")

#dob month option menu
dob_month_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], width=100, fg_color="#000000", button_color="#000000")
dob_month_option_menu.set("January")
dob_month_option_menu.place(relx = 0.595, rely = 0.76, anchor = "center")

#dob year option menu
dob_year_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range (1950, 2025)], width = 60, fg_color="#000000", button_color="#000000")
dob_year_option_menu.set("2000")
dob_year_option_menu.place(relx = 0.79, rely = 0.76, anchor = "center")

# Payment Plan label
payment_plan_label = customtkinter.CTkLabel(frameRight, text="Payment Plan", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
payment_plan_label.place(relx=0.28, rely=0.84, anchor="center")

#payment plan option menu
payment_plan_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['Monthly Plan', '3 Months Plan', 'Yearly Plan'], width=100, fg_color="#000000", button_color="#000000")
payment_plan_option_menu.set("Monthly Plan")
payment_plan_option_menu.place(relx = 0.55, rely = 0.84, anchor = "center")

# Gender label
gender_label = customtkinter.CTkLabel(frameRight, text="Gender", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
gender_label.place(relx=0.24, rely=0.91, anchor="center")

# Gender option menu
gender_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['Male', 'Female', 'Prefer Not To Say'], width=100, fg_color="#000000", button_color="#000000")
gender_option_menu.set("Male")
gender_option_menu.place(relx=0.35, rely=0.91, anchor="w")



# back button
back_button_user_registration = customtkinter.CTkButton(frameRight, text="Back", corner_radius=35, fg_color="#3d85c6", width=160, height=30, cursor="hand2", command=open_staff_registration)
back_button_user_registration.place(relx=0.3, rely=0.97, anchor="center")

# Register button
register_button = customtkinter.CTkButton(frameRight, text="Register", corner_radius=35, fg_color="#0b5394", width=160, height=30, cursor="hand2", command=register_user)
register_button.place(relx=0.7, rely=0.97, anchor="center")


app.mainloop()