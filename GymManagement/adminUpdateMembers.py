import customtkinter
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

# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open admin dashboard
def open_admin_dashboard():
    Edit_Profile.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])

# Establish a connection to the SQL Server database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# Define a function to update user details in the database
def update_user_profile(user_id, values):
    try:
        # Connect to the database
        connection = pyodbc.connect(connection_str)
        cursor = connection.cursor()

        # Build the SQL update query dynamically based on non-empty fields
        sql_update_profile = "UPDATE Customers SET "
        sql_update_profile += ", ".join(f"{key} = ?" for key in values.keys())
        sql_update_profile += " WHERE CustomerID = ?"

        # Execute the SQL query
        cursor.execute(sql_update_profile, list(values.values()) + [user_id])

        # Commit the changes to the database
        connection.commit()

        # Show a message box indicating success
        messagebox.showinfo("Submission", "Profile updated successfully!")

    except pyodbc.Error as e:
        # Show an error message box if there's an issue with the database update
        messagebox.showerror("Error", f"Database Error: {e}")

    finally:
        # Close the database connection
        cursor.close()
        connection.close()

# title
Edit_Profile_label = customtkinter.CTkLabel(Edit_Profile, text="Update User Profile", font=customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color='transparent', text_color="#3d85c6")
Edit_Profile_label.pack(pady=10)

# User Name
name_label = customtkinter.CTkLabel(Edit_Profile, text="User Name:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
name_label.place(relx=0.37, rely=0.15, anchor="center")

name_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="e.g joe", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
name_entry.place(relx=0.70, rely=0.15, anchor="e")

name_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
name_line.place(relx=0.70, rely=0.17, anchor="e")
name_line.update()

# Password
password_label = customtkinter.CTkLabel(Edit_Profile, text="Password:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
password_label.place(relx=0.37, rely=0.25, anchor="center")

password_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="*********", show="*", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
password_entry.place(relx=0.70, rely=0.25, anchor="e")

password_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
password_line.place(relx=0.70, rely=0.27, anchor="e")
password_line.update()

# Contact Number
contact_label = customtkinter.CTkLabel(Edit_Profile, text="Contact Number:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
contact_label.place(relx=0.33, rely=0.35, anchor="center")

contact_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="03332701550", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
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


# Height
height_label = customtkinter.CTkLabel(Edit_Profile, text="  Height:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
height_label.place(relx=0.37, rely=0.55, anchor="center")

height_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="eg 160 (cm)", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
height_entry.place(relx=0.70, rely=0.55, anchor="e")

height_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
height_line.place(relx=0.70, rely=0.57, anchor="e")
height_line.update()

# Weight
weight_label = customtkinter.CTkLabel(Edit_Profile, text="Weight:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
weight_label.place(relx=0.37, rely=0.65, anchor="center")

weight_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="eg 45 (kg)", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
weight_entry.place(relx=0.70, rely=0.65, anchor="e")

weight_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
weight_line.place(relx=0.70, rely=0.67, anchor="e")
weight_line.update()

# user id to update
user_id_label = customtkinter.CTkLabel(Edit_Profile, text="Enter USER ID:", font=customtkinter.CTkFont("Arial", 25), bg_color='transparent', text_color="#FFFFFF")
user_id_label.place(relx=0.33, rely=0.73, anchor="center")

id_entry = customtkinter.CTkEntry(Edit_Profile, placeholder_text="eg : 1", width=250, height=30, font=customtkinter.CTkFont("Arial", 20), fg_color="#000000", border_width=0, text_color="white")
id_entry.place(relx=0.70, rely=0.73, anchor="e")

id_line = customtkinter.CTkFrame(Edit_Profile, width=250, height=3, fg_color="white")
id_line.place(relx=0.70, rely=0.75, anchor="e")
id_line.update()


# Submit Button
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
    userid = id_entry.get()

    # Combine the dob values into a single string in the format "YYYY-MM-DD"
    dob_str = f"{dob_year}-{dob_month}-{dob_day}"

    # Build the SQL update query dynamically based on non-empty fields
    sql_update_profile = "UPDATE Customers SET "
    values = {}

    if name:
        sql_update_profile += "CustomerUsername = ?, "
        values["CustomerUsername"] = name
    if password:
        sql_update_profile += "CustomerPassword = ?, "
        values["CustomerPassword"] = password
    if contact:
        sql_update_profile += "CustomerContactNumber = ?, "
        values["CustomerContactNumber"] = contact
    if dob_str:
        sql_update_profile += "CustomerDateOfBirth = ?, "
        values["CustomerDateOfBirth"] = dob_str
    if weight:
        sql_update_profile += "CustomerWeight = ?, "
        values["CustomerWeight"] = weight
    if height:
        sql_update_profile += "CustomerHeight = ?, "
        values["CustomerHeight"] = height

    # Call the function to update the user profile in the database
    update_user_profile(userid, values)

    # Show a message box indicating success
    messagebox.showinfo("Submission", "Profile updated successfully!")


submit_button = customtkinter.CTkButton(Edit_Profile, text="Update", width=200, hover_color="#191717", corner_radius=18, font=customtkinter.CTkFont("Arial", 20), bg_color="transparent", fg_color="#3d85c6", command=submit)
submit_button.place(relx=0.60, rely=0.83, anchor="center")

back_button = customtkinter.CTkButton(Edit_Profile, text="Back", width=200, hover_color="#191717", corner_radius=18, font=customtkinter.CTkFont("Arial", 20), bg_color="transparent", fg_color="#3d85c6",command=open_admin_dashboard)
back_button.place(relx = 0.36, rely = 0.83, anchor = 'center')

Edit_Profile.mainloop()