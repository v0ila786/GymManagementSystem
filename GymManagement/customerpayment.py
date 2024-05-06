import customtkinter
from PIL import Image, ImageTk
import pyodbc
from tkinter import ttk, messagebox
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

# open customer dashboard
def open_customer_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/customerdashboard.py'])

# get userID of logged in user
def get_user_ID_of_logged_in_person():
    sql_query = "SELECT UserID From LoggedInUser"
    cursor.execute(sql_query)
    userID = cursor.fetchone()[0]
    return(userID)

# function to store payment plan in database
def make_payment():
    user_id = get_user_ID_of_logged_in_person()
    payment_plan = cpayment_option_menu.get()

    # Determine the amount based on the selected payment plan
    amount = None
    if payment_plan == 'Monthly Plan':
        amount = 8000.00
    elif payment_plan == '3 Months Plan':
        amount = 20000.00
    elif payment_plan == 'Yearly Plan':
        amount = 800000.00

    # Insert payment information into the database
    sql_query = "INSERT INTO CustomerPayments (UserID, payment_plan) VALUES (?, ?)"
    cursor.execute(sql_query, (user_id, payment_plan))
    cursor.commit()

    # Show a message box indicating success
    messagebox.showinfo("Payment Made", f"Payment of {amount} for {payment_plan} has been made.")

# left frame
frameLeft = customtkinter.CTkFrame(app, width = 450, height = 700, fg_color='#12A85C', corner_radius=0)
frameLeft.grid(row = 0, column = 0, sticky = "nsew")

# right frame
frameRight = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#24272C', corner_radius=0)
frameRight.grid(row = 0, column = 1, stick = "nsew")

# Set resizeable to full screen
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Login in page main image
login_page_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Customer Payment.png"), dark_image = Image.open("Pictures/Customer Payment.png"), size = (400,400))
login_page_image_label = customtkinter.CTkLabel(frameLeft, text = "", image = login_page_image)
login_page_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (75,75))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")


# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#12A85C")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "Manage your Payments", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#12A85C", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# first Name label
first_name_label = customtkinter.CTkLabel(frameRight, text = "Select your payment plan :", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
first_name_label.place(relx = 0.25, rely = 0.28, anchor = "center")


cpayment_option_menu = customtkinter.CTkOptionMenu(frameRight, values=['Monthly Plan', '3 Months Plan', 'Yearly Plan'], width=100, fg_color="#000000", button_color="#000000")
cpayment_option_menu.set("Monthly Plan")
cpayment_option_menu.place(relx = 0.63, rely = 0.28, anchor = "center")


# back button
back_button_user_registration = customtkinter.CTkButton(frameRight, text="Back", corner_radius=35, fg_color="#12A85C", width=160, height=30, cursor="hand2", command=open_customer_dashboard)
back_button_user_registration.place(relx=0.3, rely=0.4, anchor="center")

# payment button
register_button = customtkinter.CTkButton(frameRight, text="Make Payment", corner_radius=35, fg_color="#12A85C", width=160, height=30, cursor="hand2", command = make_payment)
register_button.place(relx=0.7, rely=0.4, anchor="center")
app.mainloop()


