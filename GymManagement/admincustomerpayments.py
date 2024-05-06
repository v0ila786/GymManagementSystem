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


# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open admin dashboard
def open_admin_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])

# Declare tree as a global variable
tree = None
total_earnings_label = None
def fetch_and_display_data():
    global tree
    
    # Establish a connection to the SQL Server database
    server = 'localhost'
    database = 'Fat Man Gym'
    username = 'sa'
    password = 'AmalAsim@2002'
    connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
    connection = pyodbc.connect(connection_str)
    cursor = connection.cursor()


    # Execute the SQL query
    query = """
    SELECT CP.UserID, CP.payment_id, C.CustomerUserName, CP.payment_plan, CP.amount, CP.status
    FROM CustomerPayments AS CP
    JOIN Customers AS C ON CP.UserID = C.CustomerID;
    """
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Create a treeview to display the data
    columns = ["UserID","Payment ID", "Customer UserName", "Payment Plan", "Amount", "Status"]
    tree = ttk.Treeview(app, columns=columns, show="headings")
    tree.tag_configure('mytag', font=('Helvetica', 30))



    # Add column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)  # Adjust the width as needed

    # Modify the data before inserting into the treeview
    for row in rows:
        modified_row = [str(item).strip("()") for item in row]
        tree.insert("", "end", values=modified_row)

    tree.place(relx=0.05, rely=0.2, anchor="nw")

    cursor.close()
    connection.close()

    # Debug print statement
    print("Fetching and displaying data completed.")

    # Update the total earnings label after fetching data
    update_total_earnings_label()

def update_total_earnings_label():
    # Execute the query to get total earnings
    total_earnings_query = "SELECT SUM(CAST(amount AS DECIMAL(10, 2))) AS total FROM CustomerPayments WHERE status = 'Active';"

    try:
        
        # Establish a connection to the SQL Server database
        server = 'localhost'
        database = 'Fat Man Gym'
        username = 'sa'
        password = 'AmalAsim@2002'
        connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
        connection = pyodbc.connect(connection_str)
        cursor = connection.cursor()

        # Execute the query to get total earnings
        cursor.execute(total_earnings_query)
        total_earnings_result = cursor.fetchone()

        # Get the total earnings from the result
        total_earnings = total_earnings_result.total if total_earnings_result and hasattr(total_earnings_result, 'total') else 0.0

        # Debug print statement
        print("Total Earnings:", total_earnings)

        # Update the text of the total earnings label
        #app.title(f"Fat Man Gym Management System - Total Earnings: ${total_earnings:.2f}")

    except pyodbc.Error as ex:
        messagebox.showerror("Error", "Failed to execute the query:\n" + str(ex))

    finally:
        cursor.close()
        connection.close()


# Function to handle the "Make Payment" button click
def make_payment():
    global tree

    # Get the selected item
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showinfo("Make Payment", "Please select a row to make a payment.")
        return

    # Extract the user ID and payment ID from the selected row
    selected_row = tree.item(selected_item, 'values')
    user_id = int(selected_row[0])  # Extract the UserID (integer) from the first position
    payment_id = selected_row[1]

    try:
        
        # Establish a connection to the SQL Server database
        server = 'localhost'
        database = 'Fat Man Gym'
        username = 'sa'
        password = 'AmalAsim@2002'
        connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
        connection = pyodbc.connect(connection_str)
        cursor = connection.cursor()

        update_query = "UPDATE CustomerPayments SET status = 'Active' WHERE UserID = ? AND payment_id = ?"
        cursor.execute(update_query, (user_id, payment_id))

        connection.commit()

    except pyodbc.Error as ex:
        messagebox.showerror("Error", "Failed to update payment status:\n" + str(ex))

    finally:
        cursor.close()
        connection.close()

    # Refresh the table to reflect the updated status
    fetch_and_display_data()


# FRAMES -----------------------------------------------------------------------------------------------------------------------------------------------------

# top frame
top_frame = customtkinter.CTkFrame(app, width=2000, height=80, fg_color="#34383e", corner_radius=0)
top_frame.grid(row=0, column=0, columnspan=2)

# GYM NAME -----------------------------------------------------------------------------------------------------------------------------------------------------

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size=(55, 55))
logo_image_label = customtkinter.CTkLabel(top_frame, text="", image=logo_image)
logo_image_label.place(relx=0.03, rely=0.5, anchor="center")

# gym name label
gym_name_label = customtkinter.CTkLabel(top_frame, text="GYM - PAYMENT RECORDS",
                                        font=customtkinter.CTkFont("Doubledecker DEMO", 40, "bold"),
                                        bg_color='transparent', text_color="#3d85c6")
gym_name_label.place(relx=0.19, rely=0.5, anchor="center")


# Cash image
cash_image = customtkinter.CTkImage(light_image=Image.open("Pictures/cash.png"), dark_image=Image.open("Pictures/cash.png"),
                                    size=(300, 300))
cash_image_label = customtkinter.CTkLabel(app, text="", image=cash_image)
cash_image_label.place(relx=0.9, rely=0.6, anchor="center")




# Create "Make Payment" button
make_payment_button = customtkinter.CTkButton(app, text="Make Payment", command=make_payment)
make_payment_button.place(relx=0.1, rely=0.7, anchor="nw")

# Create "back" button
make_payment_button = customtkinter.CTkButton(app, text="Back", command=open_admin_dashboard)
make_payment_button.place(relx=0.3, rely=0.7, anchor="nw")

# Call the fetch_and_display_data function to display the table automatically
fetch_and_display_data()

app.mainloop()