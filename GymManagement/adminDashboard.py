import customtkinter
from PIL import Image, ImageTk
import subprocess
import pyodbc
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import ttk



app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

# Establish a connection to the SQL Server database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# FUNCTIONS TO RETRIEVE VALUES -----------------------------------------------------------------------------------------------------------------------------------------------------

# function to display total earning through payments
def total_earnings_through_payments():
    try:
        # SQL query
        sql_query = " SELECT SUM(CAST(amount AS DECIMAL(10, 2))) AS total FROM CustomerPayments WHERE status = 'Active';"
        # Execute the query
        cursor.execute(sql_query)
        # Fetch the result
        result = cursor.fetchone()
        if result and result.total:
            return result.total
        else:
            print("No data found.")
    except Exception as e:
        print(f"Error: {e}")

    
# function to display total expenses through inventory
def total_expenses_through_inventory():
    try:
        sql_query = "SELECT SUM(quantity * price) AS total_inventory_value FROM Equipment2;"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        total_value = result.total_inventory_value if result else 0
        return total_value
    except Exception as e:
        print(f"Error: {e}")

# function to get number of females
def get_number_of_female_customers():
    try:
        sql_query = "SELECT COUNT(CustomerID) AS total_females FROM Customers WHERE CustomerGender = 'Female';"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        total_females = result.total_females if result else 0
        return total_females
    except Exception as e:
        print(f"Error: {e}")
    
# function to get number of males
def get_number_of_male_customers():
    try:
        sql_query = "SELECT COUNT(CustomerID) AS total_males FROM Customers WHERE CustomerGender = 'Male';"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        total_males = result.total_males if result else 0
        return total_males
    except Exception as e:
        print(f"Error: {e}")

# function to get count of trainers
def get_number_of_trainers():
    try:
        sql_query = "SELECT COUNT(EmployeeID) AS total_count FROM Staff WHERE EmployeeDesignation = 'Trainer';"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        total_count = result.total_count if result else 0
        return total_count
    except Exception as e:
        print(f"Error: {e}")

# function to get count of functional staff
def get_number_of_functional_staff():
    try:
        sql_query = "SELECT COUNT(EmployeeID) AS total_count FROM Staff WHERE EmployeeDesignation = 'Functional';"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        total_count = result.total_count if result else 0
        return total_count
    except Exception as e:
        print(f"Error: {e}")

# function to get count of non functional staff
def get_number_of_nonfunctional_staff():
    try:
        sql_query = "SELECT COUNT(EmployeeID) AS total_count FROM Staff WHERE EmployeeDesignation = 'Non-Functional';"
        cursor.execute(sql_query)
        result = cursor.fetchone()
        total_count = result.total_count if result else 0
        return total_count
    except Exception as e:
        print(f"Error: {e}")
    

# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open login page
def open_login_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/login.py'])

# open staff registration page
def open_staff_reg_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminstaffregistration.py'])

# open staff update page
def open_staff_update_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/staffupdate.py'])

# open staff delete page
def open_staff_delete_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/staffdelete.py'])

# open add member
def open_add_member_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminuserregistration.py'])

# open customer payments
def open_customer_payments():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/admincustomerpayments.py'])

# open delete customer page
def open_delete_customer():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDeleteMember.py'])

# open add inventory page
def open_add_inventory_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/addInventory.py'])

# open edit inventory
def open_edit_inventory():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/editInventory.py'])

# open gym equipment
def open_gym_equipment():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/GymEquipment.py'])

# open update members
def open_update_memebers():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminUpdateMembers.py'])  

# open gym finances 
def open_gym_finances():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/GymFinances.py'])

# open active memebers
def open_active_members():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminActiveMembers.py'])   


# FRAMES -----------------------------------------------------------------------------------------------------------------------------------------------------

# top frame
top_frame = customtkinter.CTkFrame(app, width = 1000, height = 50, fg_color="#34383e", corner_radius=0)
top_frame.grid(row = 0, column = 0, columnspan = 2)

# left frame
left_frame = customtkinter.CTkFrame(app, width = 250, height = 700, fg_color='#24272C', corner_radius=0, border_width=1)
left_frame.grid(row = 1, column = 0, sticky = "nsew")

# right frame
right_frame = customtkinter.CTkFrame(app, width = 750, height = 700, fg_color="#24272C", corner_radius=0)
right_frame.grid(row = 1, column = 1, sticky = "nsew")

# GYM NAME -----------------------------------------------------------------------------------------------------------------------------------------------------

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (45,45))
logo_image_label = customtkinter.CTkLabel(top_frame, text = "", image = logo_image)
logo_image_label.place(relx = 0.03, rely = 0.5, anchor = "center")

# gym name label
gym_name_label = customtkinter.CTkLabel(top_frame, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 40, "bold"), bg_color= 'transparent', text_color="#3d85c6")
gym_name_label.place(relx = 0.17, rely = 0.5, anchor = "center")

# MEMBERS -----------------------------------------------------------------------------------------------------------------------------------------------------

# button icons - add member
add_member_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Add Person Sign.png"), dark_image=Image.open("Pictures/Add Person Sign.png"))
update_memeber_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Update Sign.png"), dark_image=Image.open("Pictures/Update Sign.png"))
delete_memebrs_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Delete Sign.png"), dark_image=Image.open("Pictures/Delete Sign.png"))

# manage members label
manage_members_label = customtkinter.CTkLabel(left_frame, text = "Manage Members", font = customtkinter.CTkFont("Arial Unicode MS", 20))
manage_members_label.place(relx = 0.5, rely = 0.03, anchor = "center")

# add members button
add_members_button = customtkinter.CTkButton(left_frame, text = "Add Members", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image=add_member_image, command=open_add_member_page)
add_members_button.place(relx = 0.5, rely = 0.09, anchor = "center")

# update members button
update_members_button = customtkinter.CTkButton(left_frame, text = "Update Members", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = update_memeber_image, command=open_update_memebers)
update_members_button.place(relx = 0.5, rely = 0.15, anchor = "center")

# delete members button
delete_members_button = customtkinter.CTkButton(left_frame, text = "Delete Members", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = delete_memebrs_image, command=open_delete_customer)
delete_members_button.place(relx = 0.5, rely = 0.21, anchor = "center")

# STAFF -----------------------------------------------------------------------------------------------------------------------------------------------------

# manage staff label
manage_staff_label = customtkinter.CTkLabel(left_frame, text = "Manage Staff", font = customtkinter.CTkFont("Arial Unicode MS", 20))
manage_staff_label.place(relx = 0.5, rely = 0.29, anchor = "center")

# add staff button
add_members_button = customtkinter.CTkButton(left_frame, text = "Add Staff", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = add_member_image, command=open_staff_reg_page)
add_members_button.place(relx = 0.5, rely = 0.35, anchor = "center")

# update staff button
update_members_button = customtkinter.CTkButton(left_frame, text = "Update Staff", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = update_memeber_image, command=open_staff_update_page)
update_members_button.place(relx = 0.5, rely = 0.41, anchor = "center")

# delete staff button
delete_members_button = customtkinter.CTkButton(left_frame, text = "Delete Staff", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = delete_memebrs_image, command=open_staff_delete_page)
delete_members_button.place(relx = 0.5, rely = 0.47, anchor = "center")

# INVENTORY -----------------------------------------------------------------------------------------------------------------------------------------------------

# add inventory image 
add_inventory_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Plus Sign.png"), dark_image=Image.open("Pictures/Plus Sign.png"))

# manage inventory label
manage_staff_label = customtkinter.CTkLabel(left_frame, text = "Manage Inventory", font = customtkinter.CTkFont("Arial Unicode MS", 20))
manage_staff_label.place(relx = 0.5, rely = 0.55, anchor = "center")

# add inventory button
add_inventory_button = customtkinter.CTkButton(left_frame, text = "Add Inventory", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = add_inventory_image, command=open_add_inventory_page)
add_inventory_button.place(relx = 0.5, rely = 0.61, anchor = "center")

# update inventory button
update_inventory_button = customtkinter.CTkButton(left_frame, text = "Update Inventory", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = update_memeber_image, command=open_edit_inventory)
update_inventory_button.place(relx = 0.5, rely = 0.67, anchor = "center")

# delete inventory button
delete_inventory_button = customtkinter.CTkButton(left_frame, text = "Delete Inventory", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = delete_memebrs_image, command=open_edit_inventory)
delete_inventory_button.place(relx = 0.5, rely = 0.73, anchor = "center")

# SIGN OUT -----------------------------------------------------------------------------------------------------------------------------------------------------

# sign out image
sign_out_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Turn Off Sign.png"), dark_image=Image.open("Pictures/Turn Off Sign.png"))

# all finished label
personal_info_label = customtkinter.CTkLabel(left_frame, text = "All Finished?", font = customtkinter.CTkFont("Arial Unicode MS", 20))
personal_info_label.place(relx = 0.5, rely = 0.81, anchor = "center")

# sign out button
sign_out_button = customtkinter.CTkButton(left_frame, text = "Sign Out", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#3d85c6", cursor = "hand", width = 249, border_width=0.6, image = sign_out_image, command=open_login_page)
sign_out_button.place(relx = 0.5, rely = 0.87, anchor = "center")

# MAIN PANEL BUTTONS ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# active members button
active_members_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Tick Person Sign.png"), dark_image=Image.open("Pictures/Tick Person Sign.png"), size = (60,60))
active_members_button = customtkinter.CTkButton(right_frame, text = "Active\nMembers", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#3d85c6", corner_radius=20, image = active_members_image, compound='top', command= open_active_members)
active_members_button.place(relx = 0.13, rely = 0.06, anchor = "n")

# Customer Payments button
customer_payments_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Money.png"), dark_image=Image.open("Pictures/Money.png"), size = (60,60))
customer_payments_button = customtkinter.CTkButton(right_frame, text = "Customer\nPayments", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#3d85c6", corner_radius=20, image = customer_payments_image, compound='top', command=open_customer_payments)
customer_payments_button.place(relx = 0.38, rely = 0.06, anchor = "n")

# inventory button
inventory_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Dumbell Sign.png"), dark_image=Image.open("Pictures/Dumbell Sign.png"), size = (60,60))
inventory_button = customtkinter.CTkButton(right_frame, text = "Gym\nInventory", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#3d85c6", corner_radius=20, image = inventory_image, compound='top', command = open_gym_equipment)
inventory_button.place(relx = 0.62, rely = 0.06, anchor = "n")

# finances button
finances_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Dollar Sign.png"), dark_image=Image.open("Pictures/Dollar Sign.png"), size = (60,60))
finances_button = customtkinter.CTkButton(right_frame, text = "Gym\nFinances", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#3d85c6", corner_radius=20, image = finances_image, compound='top', command=open_gym_finances)
finances_button.place(relx = 0.86, rely = 0.06, anchor = "n")

# CHARTS ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

gym_fees = total_earnings_through_payments()
inventory_expenses = total_expenses_through_inventory()
females = get_number_of_female_customers()
males = get_number_of_male_customers()
trainers = get_number_of_trainers()
functional = get_number_of_functional_staff()
nonfunctional = get_number_of_nonfunctional_staff()

# expenses pie chart
def create_expenses_pie_chart(gym_fees, inventory_expenses):
    # Data for the pie chart
    labels = ['Gym Fees', 'Inventory Expenses']
    sizes = [gym_fees, inventory_expenses]
    fig, ax = plt.subplots(figsize=(3, 1), facecolor='#24272C')

    # Plot the pie chart
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops=dict(fontsize=8))
    for text, autotext in zip(texts, autotexts):
        text.set(size=5, color='white')  
        autotext.set(size=5, weight="bold", color='white') 

    ax.axis('equal')

    # Convert the plot to a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(relx=0.2, rely=0.4, anchor="center")

# Call the function to create and display the small pie chart
create_expenses_pie_chart(gym_fees, inventory_expenses)

# gender distribution pie chart
def create_gender_pie_chart(males, females):
    # Data for the pie chart
    labels = ['Males', 'Females']
    sizes = [males, females]
    fig, ax = plt.subplots(figsize=(3, 1), facecolor='#24272C')

    # Plot the pie chart
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops=dict(fontsize=8))
    for text, autotext in zip(texts, autotexts):
        text.set(size=5, color='white')  # Set label color to red
        autotext.set(size=5, weight="bold", color='white')  # Set autotext color to red

    ax.axis('equal')

    # Convert the plot to a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(relx=0.75, rely=0.4, anchor="center")

# Staff designation distribution pie chart
def create_staff_designation_pie_chart(trainers, functional, nonfunctional):
    # Data for the pie chart
    labels = ['Trainers', 'Functional', 'Non-Functional']
    sizes = [trainers, functional, nonfunctional]

    # Create a figure with a specific size and background color
    fig, ax = plt.subplots(figsize=(3, 1), facecolor='#24272C')

    # Plot the pie chart
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops=dict(fontsize=8))

    # Set label and autotext properties
    for text, autotext in zip(texts, autotexts):
        text.set(size=5, color='white')  # Set label color
        autotext.set(size=4, weight="bold", color='white')  # Set autotext color

    ax.axis('equal')

    # Convert the plot to a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(relx=0.5, rely=0.7, anchor="center")

# Call the function to create and display the small pie chart
create_gender_pie_chart(males, females)
create_expenses_pie_chart(gym_fees, inventory_expenses)
create_staff_designation_pie_chart(trainers, functional, nonfunctional)




app.mainloop()