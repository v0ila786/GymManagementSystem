import customtkinter
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import subprocess
import pyodbc
from datetime import datetime

# Create a pop-up window to display
Edit_Profile = customtkinter.CTk()
Edit_Profile.geometry("1000x700")  
Edit_Profile.resizable(True, True)
customtkinter.set_appearance_mode("Dark")
Edit_Profile.title("Edit Profile")
Edit_Profile.configure(fg_color="#24272C")

# open customer dashboard
def open_customer_dashboard():
    Edit_Profile.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/customerdashboard.py'])

# Establish connection with the database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# get userID of logged in user
def get_user_ID_of_logged_in_person():
    sql_query = "SELECT UserID From LoggedInUser"
    cursor.execute(sql_query)
    userID = cursor.fetchone()[0]
    return(userID)

# Function to get dob of logged in user
def get_logged_in_user_dob():
    sql_query_dob = "SELECT CustomerDateOfBirth FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query_dob, (get_user_ID_of_logged_in_person(),))
    dob_result = cursor.fetchone()

    if dob_result is not None and dob_result[0] is not None:
        return dob_result[0]
    else:
        print("Error: Could not retrieve valid date of birth.")
        return None


# Displaying Equipment Details
Edit_Profile_label = customtkinter.CTkLabel(Edit_Profile, text="Edit Profile", font=customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color='transparent', text_color="#12A85C")
Edit_Profile_label.pack(pady=10)

# User Name
name_label = customtkinter.CTkLabel(Edit_Profile, text="User Name:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
name_label.place(relx=0.37, rely=0.15, anchor="center")

name_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="e.g aiffa_aamir", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
name_entry.place(relx=0.70, rely=0.15, anchor="e")

name_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
name_line.place(relx=0.70, rely=0.17, anchor="e")
name_line.update()

# Password
password_label = customtkinter.CTkLabel(Edit_Profile, text="Password:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
password_label.place(relx=0.37, rely=0.25, anchor="center")

password_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="Enter your password", show="*", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
password_entry.place(relx=0.70, rely=0.25, anchor="e")

password_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
password_line.place(relx=0.70, rely=0.27, anchor="e")
password_line.update()

# Contact Number
contact_label = customtkinter.CTkLabel(Edit_Profile, text="Contact Number:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
contact_label.place(relx=0.33, rely=0.35, anchor="center")

contact_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="Enter your contact number", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
contact_entry.place(relx=0.70, rely=0.35, anchor="e")

contact_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
contact_line.place(relx=0.70, rely=0.37, anchor="e")
contact_line.update()

# Date of Birth (DOB)
dob_label = customtkinter.CTkLabel(Edit_Profile, text="Date of Birth:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
dob_label.place(relx=0.35, rely=0.45, anchor="center")

#dob day option menu
dob_day_option_menu = customtkinter.CTkOptionMenu(Edit_Profile, values=[str(i) for i in range(1, 32)], width=60, fg_color="#000000", button_color="#000000")
dob_day_option_menu.place(relx = 0.48, rely = 0.45, anchor = "center")

#dob month option menu
dob_month_option_menu = customtkinter.CTkOptionMenu(Edit_Profile, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], width=100, fg_color="#000000", button_color="#000000")
dob_month_option_menu.place(relx = 0.57, rely = 0.45, anchor = "center")

#dob year option menu
dob_year_option_menu = customtkinter.CTkOptionMenu(Edit_Profile, values=[str(i) for i in range (1950, 2025)], width = 60, fg_color="#000000", button_color="#000000")
dob_year_option_menu.place(relx = 0.67, rely = 0.45, anchor = "center")

# Set values for day, month, and year option menus based on dob
dob_result = get_logged_in_user_dob()
if dob_result is not None:
    dob_day_option_menu.set(str(dob_result.day))
    dob_month_option_menu.set(dob_result.strftime('%B'))
    dob_year_option_menu.set(str(dob_result.year))
else:
    print("Error: Unable to set date of birth values.")

# Height
height_label = customtkinter.CTkLabel(Edit_Profile, text="Height:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
height_label.place(relx=0.37, rely=0.55, anchor="center")

height_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="Enter your height in cm", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
height_entry.place(relx=0.70, rely=0.55, anchor="e")

height_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
height_line.place(relx=0.70, rely=0.57, anchor="e")
height_line.update()

# Weight
weight_label = customtkinter.CTkLabel(Edit_Profile, text="Weight:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
weight_label.place(relx=0.37, rely=0.65, anchor="center")

weight_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="Enter your weight in kg", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
weight_entry.place(relx=0.70, rely=0.65, anchor="e")

weight_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
weight_line.place(relx=0.70, rely=0.67, anchor="e")
weight_line.update()


# Submit Button
def submit():
    # Assuming you have access to the necessary entry widgets or variables
    name = name_entry.get()
    password = password_entry.get()
    contact = contact_entry.get()
    dob_day = dob_day_option_menu.get()
    dob_month = dob_month_option_menu.get()
    dob_year = dob_year_option_menu.get()
    height = height_entry.get()
    weight = weight_entry.get()

    # Combine the dob values into a single string in the format "YYYY-MM-DD"
    dob_str = f"{dob_year}-{dob_month}-{dob_day}"

    # Build the SQL update query dynamically based on non-empty fields
    sql_update_profile = "UPDATE Customers SET "
    values = []

    if name:
        sql_update_profile += "CustomerUsername = ?, "
        values.append(name)
    if password:
        sql_update_profile += "CustomerPassword = ?, "
        values.append(password)
    if contact:
        sql_update_profile += "CustomerContactNumber = ?, "
        values.append(contact)
    if dob_str:
        sql_update_profile += "CustomerDateOfBirth = ?, "
        values.append(dob_str)
    if weight:
        sql_update_profile += "CustomerWeight = ?, "
        values.append(weight)
    if height:
        sql_update_profile += "CustomerHeight = ?, "
        values.append(height)

    # Remove the trailing comma and add the WHERE clause
    sql_update_profile = sql_update_profile.rstrip(', ') + " WHERE CustomerID = ?"
    values.append(get_user_ID_of_logged_in_person())

    # Execute the update query
    cursor.execute(sql_update_profile, tuple(values))
    cursor.commit()

    # Show a message box indicating success
    messagebox.showinfo("Submission", "Profile updated successfully!")


submit_button = customtkinter.CTkButton(Edit_Profile, text="Submit", width=200, hover_color="#191717", corner_radius=18, font=customtkinter.CTkFont("Arial", 20), bg_color="transparent", fg_color="#12A85C", command=submit)
submit_button.place(relx=0.65, rely=0.85, anchor="center")

back_button = customtkinter.CTkButton(Edit_Profile, text="Back", width=200, hover_color="#191717", corner_radius=18, font=customtkinter.CTkFont("Arial", 20), bg_color="transparent", fg_color="#12A85C", command=open_customer_dashboard)
back_button.place(relx = 0.35, rely = 0.85, anchor = 'center')

Edit_Profile.mainloop()
