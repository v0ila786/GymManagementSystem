import customtkinter
from PIL import Image, ImageTk
import pyodbc
import subprocess
from datetime import datetime
from tkinter import messagebox

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

# Function to calculate the duration between two dates
def calculate_duration(start_date, end_date):
    duration = (end_date - start_date).days
    return duration

# get userID of logged in user
def get_user_ID_of_logged_in_person():
    sql_query = "SELECT UserID From LoggedInUser"
    cursor.execute(sql_query)
    userID = cursor.fetchone()[0]
    return(userID)

# Function to track the cycle
def track_cycle():
    try:
        # Get user ID of logged-in person
        customer_userID = get_user_ID_of_logged_in_person()

        # Get start and end dates from the option menus
        start_date_str = f"{cts_month_option_menu.get()} {cts_day_option_menu.get()}"
        end_date_str = f"{cte_month_option_menu.get()} {cte_day_option_menu.get()}"

        # Convert string dates to datetime objects
        start_date = datetime.strptime(start_date_str, "%B %d")
        end_date = datetime.strptime(end_date_str, "%B %d")

        # Calculate duration
        duration = calculate_duration(start_date, end_date)

        # Insert data into CycleTracking table
        insert_query = """
            INSERT INTO CycleTracking (CustomerID, StartDate, EndDate, Duration)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query, (customer_userID, start_date, end_date, duration))
        connection.commit()

        messagebox.showinfo("Success", "Cycle tracking information saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#open customer dashboard
# open the customer dashboard when sign in button pressed
def open_customer_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/customerdashboard.py'])


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
login_page_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Menstrual Calender.png"), dark_image = Image.open("Pictures/Menstrual Calender.png"), size = (450,450))
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
heading_line = customtkinter.CTkFrame(frameRight, width = 290, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "TRACK YOUR CYCLE", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# details heading
sign_up_label = customtkinter.CTkLabel(frameRight, text = "Enter Details", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
sign_up_label.place(relx = 0.5, rely = 0.25, anchor = "center")


#dob day option menu
cts_day_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range(1, 32)], width=60, fg_color="#000000", button_color="#000000")
cts_day_option_menu.set("1")
cts_day_option_menu.place(relx = 0.75, rely = 0.36, anchor = "center")

#dob month option menu
cts_month_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], width=100, fg_color="#000000", button_color="#000000")
cts_month_option_menu.set("January")
cts_month_option_menu.place(relx = 0.595, rely = 0.36, anchor = "center")

# first  label
first_name_label = customtkinter.CTkLabel(frameRight, text = "Start Date", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
first_name_label.place(relx = 0.25, rely = 0.36, anchor = "center")

# last label
last_name_label = customtkinter.CTkLabel(frameRight, text = "End Date", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
last_name_label.place(relx = 0.25, rely = 0.44, anchor = "center")


#dob day option menu
cte_day_option_menu = customtkinter.CTkOptionMenu(frameRight, values=[str(i) for i in range(1, 32)], width=60, fg_color="#000000", button_color="#000000")
cte_day_option_menu.set("1")
cte_day_option_menu.place(relx = 0.75, rely = 0.44, anchor = "center")

#dob month option menu
cte_month_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], width=100, fg_color="#000000", button_color="#000000")
cte_month_option_menu.set("January")
cte_month_option_menu.place(relx = 0.595, rely = 0.44, anchor = "center")

# back button
back_button_user_registration = customtkinter.CTkButton(frameRight, text="Back", corner_radius=35, fg_color="#3d85c6", width=160, height=30, cursor="hand2", command=open_customer_dashboard)
back_button_user_registration.place(relx=0.3, rely=0.7, anchor="center")

#  button
register_button = customtkinter.CTkButton(frameRight, text="Track", corner_radius=35, fg_color="#0b5394", width=160, height=30, cursor="hand2", command=track_cycle)
register_button.place(relx=0.7, rely=0.7, anchor="center")

app.mainloop()