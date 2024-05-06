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


tree = None
total_earnings_label = None
global sr_no
sr_no = 1

#function to display data
def fetch_and_display_data():
    global tree
    global sr_no

 # Create a treeview to display the data
    columns = ["Finances SR.NO", "Finance Description", "Amount", "IN/OUT"]
    tree = ttk.Treeview(app, columns=columns, show="headings")
    tree.tag_configure('mytag', font=('Helvetica', 40))

    # Add column headings
    for col in columns:
        # Update column heading from "Payment Plan" to "Expenses Plan"
        if col == "Expenses Plan":
            tree.heading(col, text="Expenses Plan")
        else:
            tree.heading(col, text=col)
        tree.column(col, width=150)  # Adjust the width as needed

    # Add column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=220)  

    tree.place(relx=0.1, rely=0.2, anchor="nw")

    total_earnings = total_earnings_through_payments()
    total_expenses = total_expenses_through_inventory()
    # Insert payment record into the tree
    tree.insert("", "end", values=(sr_no, "Gym Fees", total_earnings, "IN"))
    # insert inventory record into the tree
    sr_no += 1  # Increment SR no for the next record
    tree.insert("", "end", values=(sr_no, "Gym Inventory", total_expenses, "OUT"))
   

fetch_and_display_data()

# FRAMES -----------------------------------------------------------------------------------------------------------------------------------------------------

# top frame
top_frame = customtkinter.CTkFrame(app, width=2000, height=80, fg_color="#34383e", corner_radius=0)
top_frame.grid(row=0, column=0, columnspan=2)

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size=(55, 55))
logo_image_label = customtkinter.CTkLabel(top_frame, text="", image=logo_image)
logo_image_label.place(relx=0.03, rely=0.5, anchor="center")

# gym name label
gym_name_label = customtkinter.CTkLabel(top_frame, text="GYM - FINANCES RECORDS",
                                        font=customtkinter.CTkFont("Doubledecker DEMO", 40, "bold"),
                                        bg_color='transparent', text_color="#3d85c6")
gym_name_label.place(relx=0.19, rely=0.5, anchor="center")

# Cash image
cash_image = customtkinter.CTkImage(light_image=Image.open("Pictures/expenses.png"), dark_image=Image.open("Pictures/expenses.png"),
                                    size=(400, 400))
cash_image_label = customtkinter.CTkLabel(app, text="", image=cash_image)
cash_image_label.place(relx=0.9, rely=0.8, anchor="center")





  


# Create "back" button
make_payment_button = customtkinter.CTkButton(app, text="Back", command=open_admin_dashboard)
make_payment_button.place(relx=0.3, rely=0.9, anchor="nw")

app.mainloop()