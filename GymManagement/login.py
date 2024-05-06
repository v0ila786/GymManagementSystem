import customtkinter
from PIL import Image, ImageTk
import subprocess
import pyodbc
from tkinter import messagebox


# open the sign up page when sign up button is pressed 
def open_sign_up_page():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/signup.py'])

# open the customer dashboard when sign in button pressed
def open_customer_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/customerdashboard.py'])

# open admin dashboard
def open_admin_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])

# Establish connection with the database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# function to validate login
def validate_login(username, password):
    try:
        # Check for admin login first
        sql_query_admin = "SELECT * FROM Staff WHERE EmployeeUsername = ? AND EmployeePassword = ?"
        cursor.execute(sql_query_admin, (username, password))
        admin_data = cursor.fetchone()

        if admin_data:  # Admin login successful
            messagebox.showinfo("Success", "Admin login successful.")
            logged_in_admin_id = admin_data.EmployeeID
            sql_query1 = "UPDATE LoggedInUser SET UserID = ?"
            cursor.execute(sql_query1, (logged_in_admin_id))
            cursor.commit()
            open_admin_dashboard()  # Open the appropriate dashboard
            return True

        else:  # Check for customer login
            sql_query_customer = "SELECT * FROM Customers WHERE CustomerUserName = ? AND CustomerPassword = ?"
            cursor.execute(sql_query_customer, (username, password))
            user_data = cursor.fetchone()

            if user_data:  # Customer login successful
                messagebox.showinfo("Success", "Customer login successful.")
                logged_in_customer_id = user_data.CustomerID
                sql_query2 = "UPDATE LoggedInUser SET UserID = ?"
                cursor.execute(sql_query2, (logged_in_customer_id))
                cursor.commit()
                open_customer_dashboard()  # Open the appropriate dashboard
                return True

            else:
                messagebox.showerror("Failure", "Invalid username or password.")
                return False

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return False


# GUI Container------------------------------------------------------------------------------------------------------------------------------------
app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

# left frame
frameLeft = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#12A85C', corner_radius=0)
frameLeft.grid(row = 0, column = 0, sticky = "nsew")

# right frame
frameRight = customtkinter.CTkFrame(app, width = 500, height = 700, fg_color='#24272C', corner_radius=0)
frameRight.grid(row = 0, column = 1, stick = "nsew")

# Set resizeable to full screen
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

# Login in page main image
login_page_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Boxing Man.png"), dark_image = Image.open("Pictures/Boxing Man.png"), size = (400,400))
login_page_image_label = customtkinter.CTkLabel(frameLeft, text = "", image = login_page_image)
login_page_image_label.place(relx = 0.5, rely = 0.5, anchor = "center")

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (65,65))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")

# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#12A85C")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "Management System", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#128A5C", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# sign in label
sign_in_label = customtkinter.CTkLabel(frameRight, text = "SIGN IN", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
sign_in_label.place(relx = 0.5, rely = 0.32, anchor = "center")

# username underline
username_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
username_line.place(relx = 0.75, rely = 0.46, anchor = "e")

# password underline
password_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
password_line.place(relx = 0.75, rely = 0.54, anchor = "e")

# username label
username_label = customtkinter.CTkLabel(frameRight, text = "username", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.25, rely = 0.44, anchor = "center")

# password label
password_label = customtkinter.CTkLabel(frameRight, text = "password", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
password_label.place(relx = 0.25, rely = 0.52, anchor = "center")

# username entry field
username_entry = customtkinter.CTkEntry(frameRight, placeholder_text="username...", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
username_entry.place(relx= 0.75, rely = 0.44, anchor = "e")

# password entry field
password_entry = customtkinter.CTkEntry(frameRight, placeholder_text="password...", width = 200, height = 28, fg_color="#24272C", border_width=0, show = "*", text_color="white")
password_entry.place(relx= 0.75, rely = 0.52, anchor = "e")

# login button
login_button = customtkinter.CTkButton(frameRight, text = "Login", corner_radius=35, fg_color="#12A85C", command=lambda: validate_login(username_entry.get(), password_entry.get()))
login_button.place(relx = 0.5, rely = 0.6, anchor = "center")

# sign up label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "Not Registered? ", text_color="white", font =customtkinter.CTkFont("Arial", 15), bg_color="transparent")
sign_up_label.place(relx = 0.45, rely = 0.65, anchor = "center")

# sign up button
sign_up_button = customtkinter.CTkButton(frameRight, text = "Sign Up", border_width=0, bg_color="transparent", fg_color="transparent", text_color="white", font =customtkinter.CTkFont("Arial", 15, underline=True), width = 5, hover_color="#12A85C", corner_radius=35, command=open_sign_up_page)
sign_up_button.place(relx = 0.65, rely = 0.65, anchor = "center")

# Result label
result_label = customtkinter.CTkLabel(app, text="", font=customtkinter.CTkFont("Arial", 12), bg_color='transparent', text_color="#FFFFFF")
result_label.place(relx=0.5, rely=0.9, anchor="center")

app.mainloop()