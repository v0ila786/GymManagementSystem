import customtkinter
from PIL import Image, ImageTk
import pyodbc
from tkinter import ttk, messagebox
import subprocess

# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open admin dashboard
def open_admin_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/adminDashboard.py'])



def show_deletion_message():
    messagebox.showinfo("Successful", "User deleted successfully!")

def delete_user():
    # Get the user ID entered by the user
    user_id = first_name_entry.get()

    try:
        # Establish a connection to the SQL Server database
        server = 'localhost'
        database = 'Fat Man Gym'
        username = 'sa'
        password = 'AmalAsim@2002'
        connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
        connection = pyodbc.connect(connection_str)
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.execute("{CALL DeleteUser(?)}", (user_id,))
        connection.commit()

        # Check if any rows were affected
        rows_affected = cursor.rowcount

        cursor.close()
        connection.close()

        if rows_affected > 0:
            # Show a success message
            show_deletion_message()
        else:
            # Show a message indicating that the user doesn't exist
            messagebox.showinfo("Information", f"No user found with ID {user_id}.")

        # Reset entry fields
        first_name_entry.delete(0, 'end')

    except pyodbc.Error as e:
        # Show an error message if deletion fails
        messagebox.showerror("Error", f"Failed to delete user. Error: {str(e)}")




app = customtkinter.CTk()

app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

# left frame
frameLeft = customtkinter.CTkFrame(app, width = 450, height = 700, fg_color='#0b5394', corner_radius=0)
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
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (75,75))
logo_image_label = customtkinter.CTkLabel(frameRight, text = "", image = logo_image)
logo_image_label.place(relx = 0.15, rely = 0.1, anchor = "center")

# gym name heading
heading_label = customtkinter.CTkLabel(frameRight, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#3d85c6")
heading_label.place(relx = 0.58, rely = 0.1, anchor = "center")

# heading line
heading_line = customtkinter.CTkFrame(frameRight, width = 275, height = 3, fg_color="white")
heading_line.place(relx = 0.58, rely = 0.15, anchor = "center")

# management system label
management_system_label = customtkinter.CTkLabel(frameRight, text = "GYM Management (ADMIN)", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")
management_system_label.place(relx = 0.58, rely = 0.18, anchor = "center")

# sign up label
sign_up_label = customtkinter.CTkLabel(frameRight, text = "Enter User ID to Delete Member", font = customtkinter.CTkFont("Arial", 30, "bold"), bg_color='transparent', text_color="#FFFFFF")
sign_up_label.place(relx = 0.5, rely = 0.27, anchor = "center")

# first name underline
first_name_line = customtkinter.CTkFrame(frameRight, width = 197, height = 3, fg_color="white")
first_name_line.place(relx = 0.75, rely = 0.38, anchor = "e")


# first Name label
first_name_label = customtkinter.CTkLabel(frameRight, text = "User ID ", font =customtkinter.CTkFont("Arial", 20), bg_color= 'transparent', text_color="#FFFFFF")
first_name_label.place(relx = 0.25, rely = 0.36, anchor = "center")


# first name entry field
first_name_entry = customtkinter.CTkEntry(frameRight, placeholder_text="e.g 1", width = 200, height = 28, fg_color="#24272C", border_width=0, text_color="white")
first_name_entry.place(relx= 0.75, rely = 0.36, anchor = "e")


# back button
back_button_user_registration = customtkinter.CTkButton(frameRight, text="Back", corner_radius=35, fg_color="#3d85c6", width=160, height=30, cursor="hand2", command=open_admin_dashboard)
back_button_user_registration.place(relx=0.3, rely=0.5, anchor="center")

# delete button
register_button = customtkinter.CTkButton(frameRight, text="DELETE", corner_radius=35, fg_color="#0b5394",
                                          width=160, height=30, cursor="hand2", command=delete_user)
register_button.place(relx=0.7, rely=0.5, anchor="center")



app.mainloop()