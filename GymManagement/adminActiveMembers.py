import customtkinter
from PIL import Image, ImageTk
import pyodbc
import subprocess
from tkinter import ttk, messagebox

appnew = customtkinter.CTk()
appnew.geometry("1000x700")
appnew.resizable(True, True)
customtkinter.set_appearance_mode("dark")
appnew.title("Fat Man Gym Management System")

# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open admin dashboard
def open_admin_dashboard():
    appnew.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])

# Create a treeview to display the data
columns = ["UserID", "CustomerFirstName", "CustomerLastName", "Status"]
tree = ttk.Treeview(appnew, columns=columns, show="headings")

# Add column headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=220)  # Adjust the width as needed

tree.place(relx=0.1, rely=0.2, anchor="nw")

# Establish a connection to the SQL Server database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# Create a connection and cursor
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# Execute the SQL query
query = """
    SELECT
        gu.CustomerID,
        gu.CustomerFirstName,
        gu.CustomerLastName,
        gp.status
    FROM
        Customers gu
    JOIN
        CustomerPayments gp ON gu.CustomerID = gp.UserID
    WHERE
        gp.status = 'active';
"""
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

# Modify the data before inserting into the treeview
for row in rows:
    modified_row = [str(item).strip("()") for item in row]
    tree.insert("", "end", values=modified_row)

cursor.close()
connection.close()

# Debug print statement
print("Fetching and displaying data completed.")

# FRAMES -----------------------------------------------------------------------------------------------------------------------------------------------------

# top frame
top_frame = customtkinter.CTkFrame(appnew, width=2000, height=80, fg_color="#34383e", corner_radius=0)
top_frame.grid(row=0, column=0, columnspan=2)

# GYM NAME -----------------------------------------------------------------------------------------------------------------------------------------------------

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size=(55, 55))
logo_image_label = customtkinter.CTkLabel(top_frame, text="", image=logo_image)
logo_image_label.place(relx=0.03, rely=0.5, anchor="center")

# gym name label
gym_name_label = customtkinter.CTkLabel(top_frame, text="ACTIVE  MEMBERS",
                                        font=customtkinter.CTkFont("Doubledecker DEMO", 40, "bold"),
                                        bg_color='transparent', text_color="#3d85c6")
gym_name_label.place(relx=0.17, rely=0.5, anchor="center")


# Cash image
cash_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Staff.png"), dark_image=Image.open("Pictures/Staff.png"),
                                    size=(300, 300))
cash_image_label = customtkinter.CTkLabel(appnew, text="", image=cash_image)
cash_image_label.place(relx=0.8, rely=0.7, anchor="center")

# Create "back" button
back = customtkinter.CTkButton(appnew, text="Back",command=open_admin_dashboard)
back.place(relx=0.3, rely=0.7, anchor="nw")

appnew.mainloop()