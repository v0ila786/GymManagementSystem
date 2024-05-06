import customtkinter
from PIL import Image, ImageTk
import pyodbc
import datetime
import subprocess

app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

# Establish connection with the database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# open login page when sign in button is clicked
def open_login_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/login.py'])

# Function to register a user
def register():
    try:
        username = username_entry.get()
        password = password_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        contact = contact_entry.get()
        dobDay = int(dob_day_option_menu.get())
        dobMonth = dob_month_option_menu.get()
        dobYear = int(dob_year_option_menu.get())
        dob_date = datetime.datetime.strptime(f'{dobYear}-{datetime.datetime.strptime(dobMonth, "%B").month:02d}-{dobDay:02d}', '%Y-%m-%d')
        gender = gender_option_menu.get()
        sql_query = "INSERT INTO Customers (CustomerUserName, CustomerPassword, CustomerFirstName, CustomerLastName, CustomerContactNumber, CustomerDateOfBirth, CustomerGender) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_query, (username, password, first_name, last_name, contact, dob_date, gender))
        cursor.commit()
        rows_affected = cursor.rowcount
        if rows_affected > 0:
            result_label.configure(text="Entry successfully registered")
        else:
            result_label.configure(text="Failed to register entry")
    except Exception as e:
        result_label.configure(text=f"Error: {e}")


# left frame
frameLeft = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#12A85C', corner_radius=0)
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
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (65,65))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")

# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#12A85C")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "Management System", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#128A5C", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# sign up label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "SIGN UP", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
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
password_label = customtkinter.CTkLabel(frameRight, text = "Password", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
password_label.place(relx = 0.25, rely = 0.60, anchor = "center")

# password entry field
password_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g JohnDoe$1986", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
password_entry.place(relx= 0.75, rely = 0.60, anchor = "e")

# password underline
password_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
password_line.place(relx = 0.75, rely = 0.62, anchor = "e")

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
dob_label = customtkinter.CTkLabel(frameRight, text = "Birth Date", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
dob_label.place(relx = 0.25, rely = 0.76, anchor = "center")

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

#gender label
gender_label = customtkinter.CTkLabel(frameRight, text = "Gender", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
gender_label.place(relx = 0.25, rely = 0.84, anchor = "center")

#dob day option menu
gender_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['Male', 'Female'], width = 100, fg_color="#000000", button_color="#000000")
gender_option_menu.set("Male")
gender_option_menu.place(relx = 0.35, rely = 0.84, anchor = "w")

# sign up button
sign_up_button = customtkinter.CTkButton(frameRight, text = "Sign Up", corner_radius=35, fg_color="#12A85C", command=register)
sign_up_button.place(relx = 0.5, rely = 0.91, anchor = "center")

# Already Registered? label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "Already Registered? ", text_color="white", font =customtkinter.CTkFont("Arial", 15), bg_color="transparent")
sign_up_label.place(relx = 0.45, rely = 0.96, anchor = "center")

# sign in button
sign_in_button = customtkinter.CTkButton(frameRight, text = "Sign In", border_width=0, bg_color="transparent", fg_color="transparent", text_color="white", font =customtkinter.CTkFont("Arial", 15, underline=True), width = 5, hover_color="#12A85C", corner_radius=35, command=open_login_page)
sign_in_button.place(relx = 0.67, rely = 0.96, anchor = "center")

# Result label
result_label = customtkinter.CTkLabel(app, text="", font=customtkinter.CTkFont("Arial", 12), bg_color='transparent', text_color="#FFFFFF")
result_label.place(relx=0.5, rely=0.9, anchor="center")

app.mainloop()