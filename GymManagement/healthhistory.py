import tkinter as tk
from PIL import Image, ImageTk
import customtkinter  
import subprocess
import pyodbc
from tkinter import messagebox

# Create the main application window
app = customtkinter.CTk()
app.geometry("1000x700")
app.resizable(True, True)
customtkinter.set_appearance_mode("dark")
app.title("Fat Man Gym Management System")

# Establish connection with the database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# open customer dashboard
def open_customer_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/customerdashboard.py'])

# GET USER INFORMATION -----------------------------------------------------------------------------------------------------------------------------------------------------
    
# get userID of logged in user
def get_user_ID_of_logged_in_person():
    sql_query = "SELECT UserID From LoggedInUser"
    cursor.execute(sql_query)
    userID = cursor.fetchone()[0]
    return str(userID)

# get name of logged in user
def get_logged_in_person_name():
    sql_query = "SELECT CustomerFirstName FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query, (get_user_ID_of_logged_in_person()))
    userName = cursor.fetchone()[0]
    print(userName)
    return str(userName)

# get BMI of logged in user
def get_logged_in_user_BMI():
    sql_query = "SELECT CustomerBMI FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query, (get_user_ID_of_logged_in_person()))
    userBMI = cursor.fetchone()[0]
    if userBMI is None:
        return 'NULL'
    print(userBMI)
    return str(userBMI)

# get weight of logged in user
def get_logged_in_user_weight():
    sql_query = "SELECT CustomerWeight FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query, (get_user_ID_of_logged_in_person()))
    userWeight = cursor.fetchone()[0]
    if userWeight is None:
        return 'NULL'
    print(userWeight)
    return str(userWeight)

# get height of logged in user
def get_logged_in_user_height():
    sql_query = "SELECT CustomerHeight FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query, (get_user_ID_of_logged_in_person()))
    userHeight = cursor.fetchone()[0]
    if userHeight is None:
        return 'NULL'
    print(userHeight)
    return str(userHeight)

# SAVE HEALTH HISTORY -----------------------------------------------------------------------------------------------------------------------------------------------------

def save_health_history():
    medication = medication_entry.get()
    immunization = immunization_entry.get()
    allergies = allergy_entry.get()
    injuries = injuries_entry.get()
    emergency_contact_number = emergency_contact_no_entry.get()
    emergency_contact_name = emergency_contact_name_entry.get()
    try:
        customer_id = get_user_ID_of_logged_in_person()
        sql_query = "INSERT INTO HealthHistory (Medication, Immunization, Allergies, Injuries, EmergencyContactNumber, EmergencyContactName, CustomerID) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql_query, (medication, immunization, allergies, injuries, emergency_contact_number, emergency_contact_name, customer_id))
        connection.commit()

        messagebox.showinfo("Health History Saved", "Health History saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving Health History: {e}")



# Create a frame that occupies the full window
frame = customtkinter.CTkFrame(app, width=1000, height=700, fg_color='#000000', corner_radius=0)
frame.grid(row=0, column=0, sticky="nsew")

# Make the frame resizable
frame.grid_propagate(False)

#Gym Logo
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (65,65))
logo_image_label = customtkinter.CTkLabel(frame, text = "", image = logo_image)
logo_image_label.place(relx = 0.05, rely = 0.08, anchor = "center")

#FATMAN GYM LABEL
heading_label = customtkinter.CTkLabel(frame, text = "USER HEALTH HISTORY", font =customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color= 'transparent', text_color="#3d85c6")
heading_label.place(relx = 0.32, rely = 0.09, anchor = "center")

#immunization picture
immunization_image=customtkinter.CTkImage(light_image=Image.open("Pictures/Immunization.png"),dark_image=Image.open("Pictures/Immunization.png"),size=(85,85))
immunization_image_label=customtkinter.CTkLabel(frame, text="",image=immunization_image)
immunization_image_label.place(relx=0.06,rely=0.25, anchor="center")

#immunization label
immunization_label = customtkinter.CTkLabel(frame, text = "Immunization", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
immunization_label.place(relx = 0.06, rely = 0.32, anchor = "center")

#immunization entry 
immunization_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g Polio", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
immunization_entry.place(relx= 0.35, rely = 0.29, anchor = "e")

#immunization undreline
immunization_line = customtkinter.CTkFrame(frame, width = 225, height = 3, bg_color="white")
immunization_line.place(relx = 0.35, rely = 0.32, anchor = "e")

#medication picture
medication_image=customtkinter.CTkImage(light_image=Image.open("Pictures/Medication.png"),dark_image=Image.open("Pictures/Medication.png"),size=(85,85))
medication_image_label=customtkinter.CTkLabel(frame, text="",image=medication_image)
medication_image_label.place(relx=0.06,rely=0.45, anchor="center")

#medication label
medication_label = customtkinter.CTkLabel(frame, text = "Medication", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
medication_label.place(relx = 0.06, rely = 0.52, anchor = "center")

#medication entry 
medication_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g  Amlodipine", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
medication_entry.place(relx= 0.35, rely = 0.49, anchor = "e")

#medication undreline
medication_line = customtkinter.CTkFrame(frame, width = 225, height = 3, bg_color="white")
medication_line.place(relx = 0.35, rely = 0.52, anchor = "e")

#allergy picture
allergy_image=customtkinter.CTkImage(light_image=Image.open("Pictures/allergy.png"),dark_image=Image.open("Pictures/allergy.png"),size=(85,85))
allergy_image_label=customtkinter.CTkLabel(frame, text="",image=allergy_image)
allergy_image_label.place(relx=0.06,rely=0.65, anchor="center")

#allergy label
medication_label = customtkinter.CTkLabel(frame, text = "Allergies", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
medication_label.place(relx = 0.06, rely = 0.72, anchor = "center")

#allergy entry
allergy_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g  Pollen allergy", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
allergy_entry.place(relx= 0.35, rely = 0.69, anchor = "e")

#allergy underline
allergy_line = customtkinter.CTkFrame(frame, width = 225, height = 3, bg_color="white")
allergy_line.place(relx = 0.35, rely = 0.72, anchor = "e")

#injuries picture
injuries_image=customtkinter.CTkImage(light_image=Image.open("Pictures/injuries.png"),dark_image=Image.open("Pictures/injuries.png"),size=(85,85))
injuries_image_label=customtkinter.CTkLabel(frame, text="",image=injuries_image)
injuries_image_label.place(relx=0.41,rely=0.25, anchor="center")

#injuries label
injuries_label = customtkinter.CTkLabel(frame, text = "Injuries", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
injuries_label.place(relx = 0.41, rely = 0.323, anchor = "center")

#injuries entry 
injuries_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g Concussion", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
injuries_entry.place(relx= 0.7, rely = 0.29, anchor = "e")

#injuries undreline
injuries_line = customtkinter.CTkFrame(frame, width = 225, height = 3, bg_color="white")
injuries_line.place(relx = 0.7, rely = 0.32, anchor = "e")

#emergency contact no picture
emergency_contact_no_image=customtkinter.CTkImage(light_image=Image.open("Pictures/emergencycall.png"),dark_image=Image.open("Pictures/emergencycall.png"),size=(85,85))
emergency_contact_no_image_label=customtkinter.CTkLabel(frame, text="",image=emergency_contact_no_image)
emergency_contact_no_image_label.place(relx=0.41,rely=0.45, anchor="center")

#emergency contact no label
emergency_contact_no_label = customtkinter.CTkLabel(frame, text = "Emergency Info", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
emergency_contact_no_label.place(relx = 0.41, rely = 0.52, anchor = "center")

#emergency contact no entry 
emergency_contact_no_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g 0332-8976543", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
emergency_contact_no_entry.place(relx= 0.7, rely = 0.49, anchor = "e")

#emergency contact no undreline
emergency_contact_no_line = customtkinter.CTkFrame(frame, width = 225, height = 3, bg_color="white")
emergency_contact_no_line.place(relx = 0.7, rely = 0.52, anchor = "e")

#emergency contact name picture
emergency_contact_name_image=customtkinter.CTkImage(light_image=Image.open("Pictures/emergencycontacname.png"),dark_image=Image.open("Pictures/emergencycontacname.png"),size=(85,85))
emergency_contact_name_image_label=customtkinter.CTkLabel(frame, text="",image=emergency_contact_name_image)
emergency_contact_name_image_label.place(relx=0.41,rely=0.65, anchor="center")

#emergency contact name label
emergency_contact_name_label = customtkinter.CTkLabel(frame, text = "Emergency Info", font =customtkinter.CTkFont("Arial", 15), bg_color= 'transparent', text_color="#FFFFFF")
emergency_contact_name_label.place(relx = 0.41, rely = 0.72, anchor = "center")

#emergency contact name entry 
emergency_contact_name_entry = customtkinter.CTkEntry(frame, placeholder_text="e.g Lisa Evans", width = 230, height = 30, fg_color="#24272C", border_width=0, text_color="white")
emergency_contact_name_entry.place(relx= 0.7, rely = 0.69, anchor = "e")

#emergency contact name undreline
emergency_contact_name_line = customtkinter.CTkFrame(frame, width = 225, height = 3, bg_color="white")
emergency_contact_name_line.place(relx = 0.7, rely = 0.72, anchor = "e")
#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------

#user image on the left
user_image=customtkinter.CTkImage(light_image=Image.open("Pictures/gymuserlogo.png"),dark_image=Image.open("Pictures/gymuserlogo.png"),size=(90,90))
user_image_label=customtkinter.CTkLabel(frame, text="",image=user_image)
user_image_label.place(relx=0.85,rely=0.1, anchor="center")

#user info label
user_info_label = customtkinter.CTkLabel(frame, text = "User Information", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_info_label.place(relx = 0.85, rely = 0.2, anchor = "center")

#user ID Label
user_id_label = customtkinter.CTkLabel(frame, text = "User ID", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_id_label.place(relx = 0.8, rely = 0.3, anchor = "center")

#user ID display field
user_id_display=customtkinter.CTkLabel(app, text=str(get_user_ID_of_logged_in_person()),font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_id_display.place(relx=0.9,rely=0.3,anchor="center")

#username Label
username_label = customtkinter.CTkLabel(frame, text = "Name", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
username_label.place(relx = 0.8, rely = 0.4, anchor = "center")

#username display field
username_display=customtkinter.CTkLabel(app, text=str(get_logged_in_person_name()),font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
username_display.place(relx=0.9,rely=0.4,anchor="center")

#user BMI Label
user_BMI_label = customtkinter.CTkLabel(frame, text = "BMI", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_BMI_label.place(relx = 0.8, rely = 0.5, anchor = "center")

#user BMI display field
user_BMI_display=customtkinter.CTkLabel(app, text=str(get_logged_in_user_BMI()),font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_BMI_display.place(relx=0.9,rely=0.5,anchor="center")

#user weight Label
user_weight_label = customtkinter.CTkLabel(frame, text = "Weight", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_weight_label.place(relx = 0.8, rely = 0.6, anchor = "center")

#user weight display field
user_weight_display=customtkinter.CTkLabel(app, text=str(get_logged_in_user_weight()) + " kg",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_weight_display.place(relx=0.9,rely=0.6,anchor="center")

#user height label
user_height_label = customtkinter.CTkLabel(frame, text = "Height", font =customtkinter.CTkFont("Arial", 20,"bold"), bg_color= 'transparent', text_color="#FFFFFF")
user_height_label.place(relx = 0.8, rely = 0.7, anchor = "center")

#user height display field
user_height_display=customtkinter.CTkLabel(app, text=str(get_logged_in_user_height()) + " cm",font =customtkinter.CTkFont("Arial", 20), bg_color= '#000000', text_color="#FFFFFF")
user_height_display.place(relx=0.9,rely=0.7,anchor="center")

#add button
add_button = customtkinter.CTkButton(frame, text="ADD", corner_radius=35, fg_color="#0b5394",width=150,height=30,cursor="hand2", command=save_health_history)
add_button.place(relx=0.3, rely=0.8, anchor="center")

#back button
back_button = customtkinter.CTkButton(frame, text="BACK", corner_radius=35, fg_color="#0b5394",width=150,height=30,cursor="hand2", command=open_customer_dashboard)
back_button.place(relx=0.5, rely=0.8, anchor="center")

app.mainloop()
