import customtkinter
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import subprocess
import sys
import pyodbc

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

#fetching each row from audit table---------------------------------------------------------------------------------------------------
def fetch_audit_data():
    select_query = "SELECT * FROM EquipmentAudit"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        audit_data = cursor.fetchall()
        connection.commit()
        cursor.close()
        return audit_data if audit_data else None  # Return None if no data
    except Exception as e:
        print(f"Error fetching audit data: {e}")
        return None
#creating frame for each tuple in audit table-------------------------------------------------------------------------------------------------
def create_audit_frame(audit_tuple):
    # Extracting information from the tuple
    audit_id,history = audit_tuple
    # Making an audit frame
    new_prod = customtkinter.CTkFrame(my_frame, width=920, height=100, fg_color="#3D3B40")  # Updated color
    new_prod.pack(side="top", pady=10)

    # Adding label with audit history text to the frame
    audit_label = customtkinter.CTkLabel(new_prod,width=920, height=100, text=f"{history}", font=("Arial", 14, "bold"), bg_color="#3D3B40", text_color="#FFFFFF")
    audit_label.pack(side="left", padx=20, pady=10)

#main window---------------------------------------------------------------------------------------------------------------------------------

app = customtkinter.CTk()
app.geometry("1300x700+45+1")
app.resizable(True, True)
customtkinter.set_appearance_mode("Dark")
app.title("Fat Man Gym Management System")
app.configure(fg_color="#34383e")

# Heading label
# gym name heading--------------------------------------------------------------------------------------------------------------------------------
heading_label = customtkinter.CTkLabel(app, text="FAT MAN GYM", font=customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color='transparent', text_color="#3d85c6")  # Updated color
heading_label.pack(pady=10)

# management system label-------------------------------------------------------------------------------------------------------------------
management_system_label = customtkinter.CTkLabel(app, text="Inventory Audit Log", font=customtkinter.CTkFont("Doubledecker DEMO", 20,"bold"), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")  # Updated color
management_system_label.pack(pady=12)

# Making a scrollable frame----------------------------------------------------------------------------------------------------------------------
my_frame = customtkinter.CTkScrollableFrame(app, height=200,fg_color="#24272C")
my_frame.pack(expand=True, fill="both")

# Making heading labels------------------------------------------------------------------------------------------------------------------
heading = customtkinter.CTkFrame(my_frame, width=3000, height=200, fg_color="#3D3B40")  # Updated color
# Products label
products_label = customtkinter.CTkLabel(heading, text="Equipments & Accessories", font=("Doubledecker DEMO", 16, "bold"), text_color="#3d85c6")
products_label.pack(side="left", pady=10, padx=200)  # Add padx for spacing
# Place the heading frame within the scrollable frame
heading.pack()


# Label at the bottom of the page
bottom_label = customtkinter.CTkLabel(app, height=100)
bottom_label.pack(side="bottom", pady=1)

def list_window_pop():
    # Destroy all child widgets within the scrollable frame
    for widget in my_frame.winfo_children():
        widget.destroy()

    # Refresh the frame
    my_frame.update()
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/editInventory.py'])
    

# Add button inside the label using grid
back_toList_button = customtkinter.CTkButton(
    bottom_label,
    text="back to list",
    width=400,
    height=30,
    corner_radius=20,
    fg_color="#3d85c6",
    hover_color="#191717",  # Updated color
    command=open_admin_dashboard
)
# Place the button at the desired position using grid
back_toList_button.grid(row=0, column=0, pady=10)

# Fetching data from the database
audit_data = fetch_audit_data()

# Checking if data is available
if audit_data:
    # Iterating through each tuple and creating frames
    for audit_tuple in audit_data:
        create_audit_frame(audit_tuple)

app.mainloop()
