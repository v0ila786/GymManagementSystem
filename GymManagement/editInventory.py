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


# Function to fetch equipment data from the database------------------------------------------------------------------------------------------
def fetch_equipment_data():
    select_query = "SELECT * FROM Equipment2"
    try:
        cursor = connection.cursor()
        cursor.execute(select_query)
        equipment_data = cursor.fetchall()
        connection.commit()
        cursor.close()
        return equipment_data
    except Exception as e:
        print(f"Error fetching equipment data: {e}")
        return None

# window for adding more equipment-------------------------------------------------------------------------------------------------------------
def add_window_pop():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/addInventory.py'])

#deleting equipment from database---------------------------------------------------------------------------------------------------
def delete_equipment_from_database(equipment_id):
    delete_query="DELETE FROM Equipment2 WHERE id=?"
    cursor=connection.cursor()
    cursor.execute(delete_query, (equipment_id,))
    connection.commit()
    cursor.close()

def delete_frame(frame_to_delete, equipment_id):
    # Delete the corresponding equipment record from the database
    delete_equipment_from_database(equipment_id)
    frame_to_delete.destroy()
    
    # Rearrange the frames below the deleted frame
    for child in my_frame.winfo_children():
        child_info = child.place_info()
        if 'y' in child_info and child_info['y'] > frame_to_delete.winfo_y():
            child.place_configure(relx=0, rely=child_info['y'] - 1)



#updating the database values according to the change in description---------------------------------------------------------------------------
def save_changes(equipment_id, name, quantity, supplier, price, type, imagepath,):
    # Update the database with the new values
    update_query = "UPDATE Equipment2 SET name=?, quantity=?, supplier=?, price=?, equipment_type=?, image_path=? WHERE id=?"

    cursor=connection.cursor()
    cursor.execute(update_query, (name, quantity, supplier, price, type, imagepath, equipment_id))

    # Commit the changes
    connection.commit()
    connection.close

#function for displaying the description of the product whose button got clicked----------------------------------------------------------------
def display_equipment_details(equipment_id):
    # Retrieve equipment details from the database based on equipment_id
    select_query="SELECT * FROM Equipment2 WHERE id=?"
    cursor=connection.cursor()
    cursor.execute(select_query, (equipment_id,))
    equipment_details = cursor.fetchone()
    # Create a pop-up window to display equipment details
    details_window = customtkinter.CTk()
    details_window.geometry("700x500+400+100")  # Set the dimensions as needed
    details_window.title("Equipment Details")

    # Example: Displaying Equipment Details---------------------------------------------------------------------------------------------
    details_label = customtkinter.CTkLabel(details_window, text="Equipment Details", font=customtkinter.CTkFont("Arial", 20), bg_color='transparent', text_color="#FFFFFF")
    details_label.pack(pady=10)

    #Displaying Name-----------------------------------------------------------------------------------------------------------------------
    name_label = customtkinter.CTkLabel(details_window, text="Equipment Name:", font=customtkinter.CTkFont("Arial", 16), bg_color='transparent', text_color="#FFFFFF")
    name_label.place(relx=0.25, rely=0.25, anchor="center")

    # name entry field----------------------------------------------------------------------------------------------------------------
    name_entry = customtkinter.CTkEntry(details_window, placeholder_text="e.g Dumbells", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
    name_entry.place(relx=0.75, rely=0.25, anchor="e")
    #entry got set with the value that colum from database------------------------------------------------------------------------------------
    name_entry.insert(0, str(equipment_details[1]) if equipment_details else "")
    # name underline
    name_line = customtkinter.CTkFrame(details_window, width=197, height=3, fg_color="white")
    name_line.place(relx=0.75, rely=0.27, anchor="e")
    name_line.update()

    #Displaying Quantity---------------------------------------------------------------------------------------------------------------------
    quantity_label = customtkinter.CTkLabel(details_window, text="Quantity:", font=customtkinter.CTkFont("Arial", 16), bg_color='transparent', text_color="#FFFFFF")
    quantity_label.place(relx=0.25, rely=0.35, anchor="center")
    # quantity entry field
    quantity_entry = customtkinter.CTkEntry(details_window, placeholder_text="e.g 10", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
    quantity_entry.place(relx=0.75, rely=0.35, anchor="e")
    # Fill data into the quantity entry field
    quantity_entry.insert(0, str(equipment_details[2]) if equipment_details else "")
    # quantity underline
    quantity_line = customtkinter.CTkFrame(details_window, width=197, height=3, fg_color="white")
    quantity_line.place(relx=0.75, rely=0.37, anchor="e")
    quantity_line.update()

    #Displaying Supplier----------------------------------------------------------------------------------------------------------------------
    supplier_label = customtkinter.CTkLabel(details_window, text="Supplier:", font=customtkinter.CTkFont("Arial", 16), bg_color='transparent', text_color="#FFFFFF")
    supplier_label.place(relx=0.25, rely=0.45, anchor="center")
    # supplier entry field
    supplier_entry = customtkinter.CTkEntry(details_window, placeholder_text="e.g ABC Suppliers", width=200, height=28, fg_color="#000000", border_width=0, text_color="white")
    supplier_entry.place(relx=0.75, rely=0.45, anchor="e")
    supplier_entry.insert(0, str(equipment_details[3]) if equipment_details else "")
    # supplier underline
    supplier_line = customtkinter.CTkFrame(details_window, width=197, height=3, fg_color="white")
    supplier_line.place(relx=0.75, rely=0.47, anchor="e")
    supplier_line.update()
    
    #price o product---------------------------------------------------------------------------------------------
    price_label = customtkinter.CTkLabel(
        details_window,
        text="Price :",
        font=customtkinter.CTkFont("Arial", 16),
        bg_color='transparent',
        text_color="#FFFFFF"
    )
    price_label.place(relx=0.25, rely=0.55, anchor="center")

    # price entry field
    price_entry = customtkinter.CTkEntry(
        details_window,
        placeholder_text="e.g $100-$200",
        width=200,
        height=28,
        fg_color="#000000",
        border_width=0,
        text_color="white"
    )
    price_entry.place(relx=0.75, rely=0.55, anchor="e")
    price_entry.insert(0, str(equipment_details[4]) if equipment_details else "")

    # pricerange underline
    price_line = customtkinter.CTkFrame(
        details_window,
        width=197,
        height=3,
        fg_color="white"
    )
    price_line.place(relx=0.75, rely=0.57, anchor="e")
    price_line.update()
   

    #Displaying type----------------------------------------------------------------------------------------------------------------------
    type_label = customtkinter.CTkLabel(
        details_window,
        text="Type:",
        font=customtkinter.CTkFont("Arial", 16),
        bg_color='transparent',
        text_color="#FFFFFF"
    )
    type_label.place(relx=0.25, rely=0.65, anchor="center")

    # type entry field
    type_entry = customtkinter.CTkEntry(
        details_window,
        placeholder_text="e.g Treadmill",
        width=200,
        height=28,
        fg_color="#000000",
        border_width=0,
        text_color="white"
    )
    type_entry.place(relx=0.75, rely=0.65, anchor="e")
    type_entry.insert(0, str(equipment_details[5]) if equipment_details else "")

    # type underline
    type_line = customtkinter.CTkFrame(
        details_window,
        width=197,
        height=3,
        fg_color="white"
    )
    type_line.place(relx=0.75, rely=0.67, anchor="e")
    type_line.update()

    #Displaying Image Path-------------------------------------------------------------------------------------------------------------------
    imagepath_label = customtkinter.CTkLabel(
        details_window,
        text="Image Path:",
        font=customtkinter.CTkFont("Arial", 16),
        bg_color='transparent',
        text_color="#FFFFFF"
    )
    imagepath_label.place(relx=0.25, rely=0.75, anchor="center")
    # imagepath entry field
    imagepath_entry = customtkinter.CTkEntry(
        details_window,
        placeholder_text="e.g path/to/image.jpg",
        width=200,
        height=28,
        fg_color="#000000",
        border_width=0,
        text_color="white"
    )
    imagepath_entry.place(relx=0.75, rely=0.75, anchor="e")
    imagepath_entry.insert(0, str(equipment_details[7]) if equipment_details else "")

    # imagepath underline
    imagepath_line = customtkinter.CTkFrame(
        details_window,
        width=197,
        height=3,
        fg_color="white"
    )
    imagepath_line.place(relx=0.75, rely=0.77, anchor="e")
    imagepath_line.update()

    #fuctiion for saving the changes made in description
    
    def on_save_button_click():
        # Get the updated values from the entry fields
        updated_name = name_entry.get()
        updated_quantity = quantity_entry.get()
        updated_supplier = supplier_entry.get()
        updated_price = price_entry.get()
        updated_type = type_entry.get()
        updated_imagepath = imagepath_entry.get()
        

        # Call the save_changes function to update the database
        save_changes(equipment_id, updated_name, updated_quantity, updated_supplier,
                     updated_price, updated_type, updated_imagepath)

        # Optionally, you can display a message indicating that changes have been saved
        print("Changes saved successfully!")

    # Save button
    save_button = customtkinter.CTkButton(details_window, text="Save", corner_radius=35,
                                          fg_color="#000000", hover_color="#191717",command=on_save_button_click)
    save_button.place(relx = 0.50, rely = 0.91, anchor = "center")

    details_window.mainloop()
#function for setting availability------------------------------------------------------------------------------------------------------
def set_availability(choice, equipment_id):
    availability_value = choice

    # Update availability in the database
    update_query="UPDATE Equipment2 SET availability = ? WHERE id = ?"
    cursor=connection.cursor()
    cursor.execute(update_query, (availability_value, equipment_id))
    connection.commit()
    connection.close

def create_product_frame(image_path, button_name,equipment_id):
    global new_prod
    # Making product frame one tuple in database-------------------------------------------------------------------------------
    new_prod = customtkinter.CTkFrame(my_frame, width=920, height=60, fg_color="#3D3B40")  # Updated color
    new_prod.pack(side="top", pady=10)

    # Retrieve availability from the database-------------------------------------------------------------------------------
    create_query="SELECT availability FROM Equipment2  WHERE id = ?"
    cursor=connection.cursor()
    cursor.execute(create_query, (equipment_id,))
    availability_value = cursor.fetchone()[0]
    cursor.commit()
    cursor.close

    # Availability dropdown menu
    options = ["Available", "Unavailable"]
    menu = customtkinter.CTkOptionMenu(new_prod, values=options,fg_color='#000000',button_color='#000000',button_hover_color='#191717',  
                                       command=lambda choice: set_availability(choice, equipment_id))
    menu.set(availability_value)
    menu.place(relx=0.02, rely=0.5, anchor="w")  # Adjust relx, rely as needed

    # Load an image of equipment----------------------------------------------------------------------------------------------------------
    my_image = customtkinter.CTkImage(
        light_image=Image.open(image_path),
        dark_image=Image.open(image_path),
        size=(100, 50),
    )

    # Adding the button with text and image to the new frame---------------------------------------------------------------------------------
    button = customtkinter.CTkButton(
        new_prod,
        text=f" {button_name} ",
        width=600,
        height=40,
        corner_radius=18,
        anchor="w",
        image=my_image, 
        hover_color="#000000",
        fg_color="#3D3B40",  # Updated color
        compound="left",
        command=lambda: display_equipment_details(equipment_id)
    )
    # Place the button at the desired position on the frame
    button.place(relx=0.2, rely=0)

    # Delete button for deleting the prooduct from datbase-----------------------------------------------------------
    delete_button = customtkinter.CTkButton(
        new_prod,
        text=" Delete ",
        width=40,
        height=20,
        corner_radius=18,
        anchor="w",
        fg_color="#3D3B40",
        hover_color="#000000",  # Updated color
        compound="right",
        command=lambda: delete_frame(new_prod, equipment_id)
    )
    # Place the button at the desired position on the frame
    delete_button.place(relx=0.9, rely=0.3)

#Mainwindow---------------------------------------------------------------------------------------------------------------------------

app = customtkinter.CTk()
app.geometry("1000x700+95+1")
app.resizable(True, True)
customtkinter.set_appearance_mode("Dark")
app.title("Fat Man Gym Management System")
app.configure(fg_color="#3D3B40")

# gym name heading--------------------------------------------------------------------------------------------------------------------------------
heading_label = customtkinter.CTkLabel(app, text="FAT MAN GYM", font=customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color='transparent', text_color="#3d85c6")  # Updated color
heading_label.pack(pady=10)

# management system label-----------------------------------------------------------------------------------------------------------------------------
management_system_label = customtkinter.CTkLabel(app, text="GYM Equipment", font=customtkinter.CTkFont("Doubledecker DEMO", 20, "bold"), bg_color="transparent", text_color="#3d85c6", fg_color="transparent")  # Updated color
management_system_label.pack(pady=12)

#LOG BUTTON that opens the log page----------------------------------------------------------------------------------------------------------------------
def Inventory_Audit_Log():
    app.destroy()
    subprocess.run([sys.executable, 'C:\\Users\\Admin\\Desktop\\gym\\Inventory_Audit_Log.py'])

#inventory log button
log_button = customtkinter.CTkButton(
    app,
    text="Inventory Audit Log",
    width=70,
    height=30,
    corner_radius=20,
    fg_color="#3d85c6",
    hover_color="#191717",  # Updated color
    command=Inventory_Audit_Log
)
# Place the button at the desired position using grid
log_button.place(relx=0.83, rely=0.127)


# Making a scrollable frame-----------------------------------------------------------------------------------------------------
my_frame = customtkinter.CTkScrollableFrame(app, height=200,fg_color="#24272C")
my_frame.pack(expand=True, fill="both")

# Making heading labels---------------------------------------------------------------------------------------------------------------
heading = customtkinter.CTkFrame(my_frame, width=1000, height=200, fg_color="#3D3B40")  # Updated color

# Available label---------------------------------------------------------------------------------------------------------------------
avaiable_label = customtkinter.CTkLabel(heading, text="Availability", font=("Arial", 16, "bold"))
avaiable_label.pack(side="left", pady=10, padx=50)

# Products label----------------------------------------------------------------------------------------------------------------------
products_label = customtkinter.CTkLabel(heading, text="Equipments & Accessories", font=("Arial", 16, "bold"))
products_label.pack(side="left", pady=10, padx=200)  # Add padx for spacing

# Delete label------------------------------------------------------------------------------------------------------------------------
delete_label = customtkinter.CTkLabel(heading, text="Delete", font=("Arial", 16, "bold"))
delete_label.pack(side="left", pady=10, padx=50)

# Place the heading frame within the scrollable frame 
heading.pack()


# Label at the bottom of the page----------------------------------------------------------------------------------------------------------
bottom_label = customtkinter.CTkLabel(app, height=100)
bottom_label.pack(side="bottom", pady=1)

# Add button for adding more equipment inside the label----------------------------------------------------------------------------------
add_button = customtkinter.CTkButton(
    bottom_label,
    text="Add more",
    width=400,
    height=30,
    corner_radius=20,
    fg_color="#3d85c6",
    hover_color="#191717",  # Updated color
    command=add_window_pop
)
# Place the button at the desired position using grid
add_button.grid(row=0, column=0, pady=10)


# Fetch equipment data from the database-----------------------------------------------------------------------------------------
equipment_data = fetch_equipment_data()

# Create frames for each equipment in the scroll bar
for equipment in equipment_data:
    create_product_frame(equipment[7], equipment[1], equipment[0])

# back button
back_button = customtkinter.CTkButton(app, text="Go Back", corner_radius=35, fg_color="#3d85c6", hover_color="#191717", command=open_admin_dashboard)
back_button.place(relx=0.1, rely=0.15, anchor="center")

app.mainloop()
