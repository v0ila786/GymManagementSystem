import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import pyodbc
import sys
import subprocess

app = customtkinter.CTk()
app.geometry("1300x700+45+1")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Add Equipment")

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


# Function to add equipment to the database
def add_equipment_to_database():
    try:
        name = name_entry.get()
        quantity = int(Quantity_entry.get())
        supplier = supplier_entry.get()
        price = int(priceStart_range_entry.get())
        equipment_type = Types_entry.get()
        image_path = image_path_entry.get()

        # Construct SQL INSERT statement
        sql_insert = """
        INSERT INTO Equipment2 (name, quantity, supplier, price, equipment_type, image_path)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        # Print and execute the SQL statement
        print(sql_insert, (name, quantity, supplier, price, equipment_type, image_path))
        cursor.execute(sql_insert, (name, quantity, supplier, price, equipment_type, image_path))

        # Commit the transaction
        connection.commit()
        # Clear entry fields
        name_entry.delete(0, tk.END)
        Quantity_entry.delete(0, tk.END)
        supplier_entry.delete(0, tk.END)
        priceStart_range_entry.delete(0, tk.END)
        Types_entry.delete(0, tk.END)
        image_path_entry.delete(0, tk.END)
    except Exception as e:
        print("Error occurred:", e)
    

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
login_page_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Dark Gym aesthetics.jpg"), dark_image = Image.open("Pictures/Dark Gym aesthetics.jpg"), size = (800,800))
login_page_image_label = customtkinter.CTkLabel(frameLeft, text = "", image = login_page_image)
login_page_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/addeq.jpg"), dark_image=Image.open("Pictures/addeq.jpg"), size = (65,65))
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
sign_up_label = customtkinter.CTkLabel(frameRight, text = "Add Equipment", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
sign_up_label.place(relx = 0.5, rely = 0.27, anchor = "center")

# name label
name_label = customtkinter.CTkLabel(frameRight, text="Equipment Name", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
name_label.place(relx=0.25, rely=0.36, anchor="center")

# name entry field
name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g Dumbells", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
name_entry.place(relx=0.75, rely=0.36, anchor="e")

# name underline
name_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
name_line.place(relx=0.75, rely=0.38, anchor="e")

# quantity label
Quantity_label = customtkinter.CTkLabel(frameRight, text="Quantity", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
Quantity_label.place(relx=0.25, rely=0.44, anchor="center")

# quantity entry field
Quantity_entry = customtkinter.CTkEntry(frameRight, placeholder_text="8", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
Quantity_entry.place(relx=0.75, rely=0.44, anchor="e")

# quantity underline
Quantity_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
Quantity_line.place(relx=0.75, rely=0.46, anchor="e")

# supplier label
supplier_label = customtkinter.CTkLabel(frameRight, text="Supplier", font=customtkinter.CTkFont("Arial", 20, "bold"), bg_color="transparent")
supplier_label.place(relx=0.25, rely=0.52, anchor="center")

# supplier entry field
supplier_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g. ABC Suppliers", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
supplier_entry.place(relx=0.75, rely=0.52, anchor="e")

# supplier underline
supplier_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
supplier_line.place(relx=0.75, rely=0.54, anchor="e")

# price range label
priceStart_range_label = customtkinter.CTkLabel(frameRight, text="Equipment Price", font=customtkinter.CTkFont("Arial", 20, "bold"), bg_color="transparent")
priceStart_range_label.place(relx=0.25, rely=0.60, anchor="center")

# price range start entry field
priceStart_range_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g. $500", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
priceStart_range_entry.place(relx=0.75, rely=0.60, anchor="e")

# price range underline
priceStart_range_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
priceStart_range_line.place(relx=0.75, rely=0.62, anchor="e")

# types label
Types_label = customtkinter.CTkLabel(frameRight, text="Types", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
Types_label.place(relx=0.25, rely=0.68, anchor="center")

# types entry field
Types_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g. Cardio", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
Types_entry.place(relx=0.75, rely=0.68, anchor="e")

# types underline
types_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
types_line.place(relx=0.75, rely=0.70, anchor="e")

# image path label
image_path_label = customtkinter.CTkLabel(frameRight, text="Image Path", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
image_path_label.place(relx=0.25, rely=0.74, anchor="center")

# image path entry field
image_path_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g. path/to/your/image.png", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
image_path_entry.place(relx=0.75, rely=0.74, anchor="e")

# image path underline
image_path_line = customtkinter.CTkFrame(frameRight, width=197, height=3, fg_color="white")
image_path_line.place(relx=0.75, rely=0.76, anchor="e")

# add button
add_button = customtkinter.CTkButton(frameRight, text="ADD", corner_radius=35, fg_color="#3d85c6", hover_color="#191717", command=add_equipment_to_database)
add_button.place(relx=0.29, rely=0.91, anchor="center")

#back function------------------------------------------------------------------------------------------------------------------------- 


# back button
back_button = customtkinter.CTkButton(frameRight, text="Go Back", corner_radius=35, fg_color="#3d85c6", hover_color="#191717", command=open_admin_dashboard)
back_button.place(relx=0.65, rely=0.91, anchor="center")





app.mainloop()