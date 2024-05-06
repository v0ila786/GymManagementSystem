import customtkinter
from PIL import Image, ImageTk
import pyodbc
from datetime import datetime
import emoji
import subprocess
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Establish connection with the database
server = 'localhost'
database = 'Fat Man Gym'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# function to save trainer to Customers table
def save_trainer():
    try:
        # Get user ID of logged-in person
        customer_userID = get_user_ID_of_logged_in_person()

        # Get the selected trainer from the option menu
        selected_trainer_fullname = trainer_option_menu.get()
        
        # Extract first name from the full name
        selected_trainer_first_name = selected_trainer_fullname.split()[0]

        # Retrieve TrainerID from Staff table based on the selected trainer's first name
        sql_query = "SELECT EmployeeID FROM Staff WHERE EmployeeDesignation = 'Trainer' AND EmployeeFirstName = ?"
        cursor.execute(sql_query, selected_trainer_first_name)
        trainer_id = cursor.fetchone()

        # Update TrainerID in Customers table for the logged-in customer
        update_customer_query = "UPDATE Customers SET TrainerID = ? WHERE CustomerID = ?"
        cursor.execute(update_customer_query, (trainer_id[0], customer_userID))

        # Commit the transaction
        connection.commit()

        messagebox.showinfo("Success", "Trainer updated for the customer successfully.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")





# OPEN PAGES -----------------------------------------------------------------------------------------------------------------------------------------------------

# open cycle tracking page
def open_cycle_tracking_page():
    customerDashboard.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/cycletracking.py'])

# open health history
def open_health_history_page():
    customerDashboard.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/healthhistory.py'])

# open update profile
def open_update_profile_page():
    customerDashboard.destroy()
    subprocess.Popen(['python3', 'GymManagement/updatecustomerprofile.py'])

# open payment plan
def open_payment_plan_page():
    customerDashboard.destroy()
    subprocess.Popen(['python3', 'GymManagement/customerpayment.py'])

# open instructional videos
def open_instructional_videos_page():
    customerDashboard.destroy()
    subprocess.Popen(['python3', 'GymManagement/videolinks.py'])

# open login page
def open_login_page():
    customerDashboard.destroy()
    subprocess.Popen(['python3', 'GymManagement/login.py'])   

# OTHER FUNCTIONS -----------------------------------------------------------------------------------------------------------------------------------------------------
    
# get userID of logged in user
def get_user_ID_of_logged_in_person():
    sql_query = "SELECT UserID From LoggedInUser"
    cursor.execute(sql_query)
    userID = cursor.fetchone()[0]
    return(userID)

# get name of logged in user
def get_logged_in_person_name():
    sql_query = "SELECT CustomerFirstName FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query, (get_user_ID_of_logged_in_person()))
    userName = cursor.fetchone()[0]
    print(userName)
    return userName

# good morning/good evening/good night label
def time_greeting():
    now = datetime.now()
    hour = now.hour
    if hour < 12:
        good_morning_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Sun.png"), dark_image = Image.open("Pictures/Sun.png"), size = (60,60))
        greeting = "Good Morning " + get_logged_in_person_name() + "!"
        welcome_label = customtkinter.CTkLabel(bottom_frame, text = greeting, font = customtkinter.CTkFont("Arial", 40, "bold"), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent", image = good_morning_image, compound = 'left')
        welcome_label.place(relx = 0.01, rely = 0.1, anchor = 'w')
    elif hour < 18:
        good_evening_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Evening.png"), dark_image = Image.open("Pictures/Evening.png"), size = (60,60))
        greeting = "Good Evening " + get_logged_in_person_name() + "!"
        welcome_label = customtkinter.CTkLabel(bottom_frame, text = greeting, font = customtkinter.CTkFont("Arial", 40, "bold"), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent", image = good_evening_image, compound = 'left')
        welcome_label.place(relx = 0.01, rely = 0.1, anchor = 'w')
    else:
        good_night_image = customtkinter.CTkImage(light_image = Image.open("Pictures/Night.png"), dark_image = Image.open("Pictures/Night.png"), size = (60,60))
        greeting = "Good Night " + get_logged_in_person_name() + "!"
        welcome_label = customtkinter.CTkLabel(bottom_frame, text = greeting, font = customtkinter.CTkFont("Arial", 40, "bold"), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent", image = good_night_image, compound = 'left')
        welcome_label.place(relx = 0.01, rely = 0.1, anchor = 'w')

# get gender of logged in person
def get_logged_in_person_gender():
    sql_query = "SELECT CustomerGender FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query, (get_user_ID_of_logged_in_person()))
    userGender = cursor.fetchone()[0]
    print(userGender)
    return userGender

# Video Link + Cycle Tracking buttons on dashboard based on gender
def video_link_button():
    gender = get_logged_in_person_gender()
    video_link_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Video Sign.png"), dark_image=Image.open("Pictures/Video Sign.png"), size = (60,60))
    if gender == 'Male':
        video_link_button = customtkinter.CTkButton(customerDashboard, text = "Instructional Video Links", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 560, height = 100, fg_color = "#12A85C", corner_radius=20, image = video_link_image, compound='left', cursor = 'hand', command=open_instructional_videos_page)
        video_link_button.place(relx = 0.01, rely = 0.52, anchor = "w")
    else:
        cycle_tracking_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Drop Sign.png"), dark_image=Image.open("Pictures/Drop Sign.png"), size = (40,40))
        video_link_button = customtkinter.CTkButton(customerDashboard, text = "Instructional Video Links", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 360, height = 100, fg_color = "#12A85C", corner_radius=20, image = video_link_image, compound='left', cursor = 'hand', command=open_instructional_videos_page)
        video_link_button.place(relx = 0.01, rely = 0.52, anchor = "w")
        cycle_tracking_button = customtkinter.CTkButton(customerDashboard, text = "Cycle\nTracking", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 50, fg_color = "#12A85C", corner_radius=20, image = cycle_tracking_image, compound='top', cursor = 'hand', command=open_cycle_tracking_page)
        cycle_tracking_button.place(relx = 0.41, rely = 0.52, anchor = "w")

def compute_bmi():
    # get height in cm
    sql_query_height = "SELECT CustomerHeight FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query_height, (get_user_ID_of_logged_in_person()))
    height_result = cursor.fetchone()

    if height_result is not None and height_result[0] is not None:
        userHeight = float(height_result[0])
    else:
        print("Error: Could not retrieve valid height.")
        return None

    # get weight in kg
    sql_query_weight = "SELECT CustomerWeight FROM Customers WHERE CustomerID = ?"
    cursor.execute(sql_query_weight, (get_user_ID_of_logged_in_person()))
    weight_result = cursor.fetchone()

    if weight_result is not None and weight_result[0] is not None:
        userWeight = float(weight_result[0])
    else:
        print("Error: Could not retrieve valid weight.")
        return None

    # calculate BMI
    bmi = userWeight / ((userHeight / 100) ** 2)

    # update BMI in the database
    sql_query_store_bmi = "UPDATE Customers SET CustomerBMI = ? WHERE CustomerID = ?"
    cursor.execute(sql_query_store_bmi, (bmi, get_user_ID_of_logged_in_person()))
    cursor.commit()

    return bmi

# Change color on progress bar relative to BMI
def update_bmi_progress_bar(bmi):
    value = 0
    if bmi is None:
        return
    if bmi < 18.5:
        bmi_progress_bar.configure(progress_color='#48cae4')
        bmi_category_label.configure(text=emoji.emojize("Underweight :woman_zombie:"))
    elif bmi < 25:
        bmi_progress_bar.configure(progress_color='#70e000')
        bmi_category_label.configure(text=emoji.emojize("Normal Weight :thumbs_up:"))
    elif bmi < 30:
        bmi_progress_bar.configure(progress_color='#ffd60a')
        bmi_category_label.configure(text=emoji.emojize("Overweight :warning:"))
    else:
        bmi_progress_bar.configure(progress_color='#ef233c')
        bmi_category_label.configure(text=emoji.emojize("Obese :skull:"))
    normalized_bmi = (bmi - 10) / 30
    bmi_progress_bar.set(normalized_bmi)

# get number of goals of logged in user
def get_number_of_goals():
    sql_query = "SELECT COUNT(GoalID)AS NumberOfGoals FROM CustomerGoals WHERE CustomerID = ? AND GoalStatus = 'Not Completed';"
    cursor.execute(sql_query, get_user_ID_of_logged_in_person())
    number_of_goals = cursor.fetchone()[0]
    if number_of_goals is None:
        return 0
    else:
        return number_of_goals



global goal_rely
goal_rely = 0.25

# display uncompleted goals
def display_uncompleted_goals():
    global goal_rely
    sql_query = "SELECT GoalID, GoalType, GoalTargetDate FROM CustomerGoals WHERE CustomerID = ? AND GoalStatus = 'Not Completed';"
    cursor.execute(sql_query, get_user_ID_of_logged_in_person())
    uncompleted_goals = cursor.fetchall()

    for goal_info in uncompleted_goals:
        goal_id, goal_type, target_date = goal_info

        # Create unique variable names using string formatting
        goal_switch_var_unique = f"goal_switch_var_{goal_id}"
        goal_type_var_unique = f"goal_type_var_{goal_id}"
        target_date_var_unique = f"target_date_var_{goal_id}"

        # goal frame
        goal_frame = customtkinter.CTkFrame(todo_frame, width=360, height=30, corner_radius=0, bg_color='#24272C', fg_color='#24272C', border_width=1, border_color='white')
        goal_frame.place(relx=0.5, rely=goal_rely, anchor='center')
        goal_rely = goal_rely + 0.1

        # switch (using unique variable name)
        goal_switch_var_unique = customtkinter.StringVar(value="on")
        goal_switch = customtkinter.CTkSwitch(goal_frame, text=" ", variable=goal_switch_var_unique, onvalue="on", offvalue="off", progress_color='#12A85C')
        goal_switch.deselect()
        goal_switch.place(relx=0.15, rely=0.5, anchor='center')

        # goal list (using unique variable name)
        goal_type_var_unique = customtkinter.StringVar(value=goal_type)
        goal_list = customtkinter.CTkOptionMenu(goal_frame, values=["Weight Loss", "Cardio", "Cardio Training", "Strength Training", "Muscle Toning"], variable=goal_type_var_unique, width=150, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color='black')
        goal_list.place(relx=0.33, rely=0.5, anchor='center')

        # target date (using unique variable name)
        target_date_var_unique = customtkinter.StringVar(value=target_date)
        target_date_list = customtkinter.CTkOptionMenu(goal_frame, values=["1 Week", "1 Month", "3 Months", "6 Months"], variable=target_date_var_unique, width=100, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color='black')
        target_date_list.place(relx=0.57, rely=0.5, anchor='w')

        # save goal (using unique variable names and passing them correctly)
        def save_goal(goal_id, goal_switch_var, goal_type_var, target_date_var):
            try:
                user_id = get_user_ID_of_logged_in_person()
                goal_type = goal_type_var.get()
                target_date = target_date_var.get()

                if goal_switch_var.get() == "on":
                    # Update goal status to "Completed"
                    sql_update_query = "UPDATE CustomerGoals SET GoalStatus = 'Completed' WHERE GoalID = ? AND CustomerID = ? AND GoalType = ? AND GoalTargetDate = ?"
                    cursor.execute(sql_update_query, (goal_id, user_id, goal_type, target_date))
                    connection.commit()
                    messagebox.showinfo("Goal Saved", "Goal saved successfully")
                else:
                    # Debugging print statement to check the value of goal
                    print("Goal switch is not on")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving goal: {e}")

        # save button (using unique variable names and passing them correctly)
        save_goal_button = customtkinter.CTkButton(goal_frame, text="Save", font=customtkinter.CTkFont("Arial Unicode MS", 10), width=40, height=10, fg_color="#12A85C", corner_radius=30, compound='left', cursor='hand', command=lambda goal_id=goal_id, goal_switch_var=goal_switch_var_unique, goal_type_var=goal_type_var_unique, target_date_var=target_date_var_unique: save_goal(goal_id, goal_switch_var, goal_type_var, target_date_var))
        save_goal_button.place(relx=0.93, rely=0.5, anchor='center')

# create frames for todo list 

def create_goals_list_frame():
    global goal_rely
    number_of_goals = get_number_of_goals()
    if (number_of_goals == 6):
        messagebox.showerror("Error", f"Maximum Limit of goals reached!")
        return
    # goal frame
    goal_frame = customtkinter.CTkFrame(todo_frame, width = 360, height = 30, corner_radius=0, bg_color='#24272C', fg_color='#24272C', border_width=1, border_color='white')
    goal_frame.place(relx = 0.5, rely = goal_rely, anchor = 'center')
    goal_rely = goal_rely + 0.1
    # switch
    goal_switch_var = customtkinter.StringVar(value="on")
    goal_switch = customtkinter.CTkSwitch(goal_frame, text = " ", variable=goal_switch_var, onvalue="on", offvalue="off", progress_color='#12A85C')
    goal_switch.deselect()
    goal_switch.place(relx = 0.15, rely = 0.5, anchor = 'center')
    # goal list
    goal_list = customtkinter.CTkOptionMenu(goal_frame, values=["Weight Loss", "Cardio", "Strength Training", "Muscle Toning"], width=150, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color='black')
    goal_list.place(relx = 0.33, rely = 0.5, anchor = 'center')
    # target date
    target_date_list = customtkinter.CTkOptionMenu(goal_frame, values=["1 Week", "1 Month", "3 Months", "6 Months"], width=100, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color='black')
    target_date_list.place(relx = 0.57, rely = 0.5, anchor = 'w')
    # save goal
    def save_goal():
        try:
            # Get user ID
            user_id = get_user_ID_of_logged_in_person()
            # Get selected goal type and target date
            goal_type = goal_list.get()
            target_date = target_date_list.get()

            # Check if the switch is in the "on" state
            if goal_switch_var.get() == "on":
                # Update the goal status to "Completed"
                sql_update_query = "UPDATE CustomerGoals SET GoalStatus = 'Completed' WHERE CustomerID = ? AND GoalType = ? AND GoalTargetDate = ?"
                cursor.execute(sql_update_query, (user_id, goal_type, target_date))
            else:
                # Insert into the database
                sql_query = "INSERT INTO CustomerGoals (CustomerID, GoalType, GoalTargetDate) VALUES (?, ?, ?)"
                cursor.execute(sql_query, (user_id, goal_type, target_date))

            connection.commit()
            # Display success message
            messagebox.showinfo("Goal Saved", "Goal saved successfully")
        except Exception as e:
            # Display error message
            messagebox.showerror("Error", f"Error saving goal: {e}")

            
    # save button
    save_goal_button = customtkinter.CTkButton(goal_frame, text = "Save", font = customtkinter.CTkFont("Arial Unicode MS", 10), width = 40, height = 10, fg_color = "#12A85C", corner_radius=30, compound='left', cursor = 'hand', command=save_goal)
    save_goal_button.place(relx = 0.93, rely = 0.5, anchor = 'center')
    





    
# main app
customerDashboard = customtkinter.CTk()
customerDashboard.geometry("1000x700")
customerDashboard.resizable(True, True)
customtkinter.set_appearance_mode("dark")
customerDashboard.title("Fat Man Gym Management System")

# FRAMES -----------------------------------------------------------------------------------------------------------------------------------------------------

# top frame
top_frame = customtkinter.CTkFrame(customerDashboard, width = 1000, height = 50, fg_color="#34383e", corner_radius=0)
top_frame.grid(row = 0, column = 0, columnspan = 2)

# bottom frame
bottom_frame = customtkinter.CTkFrame(customerDashboard, width = 1000 , height = 650, fg_color = '#24272C', corner_radius=0)
bottom_frame.grid(row = 1, column = 0, sticky = "nsew")

# GYM NAME -----------------------------------------------------------------------------------------------------------------------------------------------------

# Gym logo image
logo_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Gym Logo.png"), dark_image=Image.open("Pictures/Gym Logo.png"), size = (45,45))
logo_image_label = customtkinter.CTkLabel(top_frame, text = "", image = logo_image)
logo_image_label.place(relx = 0.03, rely = 0.5, anchor = "center")

# gym name label
gym_name_label = customtkinter.CTkLabel(top_frame, text = "FAT MAN GYM", font =customtkinter.CTkFont("Doubledecker DEMO", 40, "bold"), bg_color= 'transparent', text_color="#12A85C")
gym_name_label.place(relx = 0.17, rely = 0.5, anchor = "center")

# SIGN OUT BUTTON -----------------------------------------------------------------------------------------------------------------------------------------------------

# sign out image
sign_out_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Turn Off Sign.png"), dark_image=Image.open("Pictures/Turn Off Sign.png"))

# sign out button
sign_out_button = customtkinter.CTkButton(top_frame, text = "Sign Out", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#12A85C", cursor = "hand", width = 120, border_width=0.6, image = sign_out_image, command=open_login_page)
sign_out_button.place(relx = 0.93, rely = 0.5, anchor = "center")

# WELCOME LABEL -----------------------------------------------------------------------------------------------------------------------------------------------------
time_greeting()

# UPDATE PROFILE -----------------------------------------------------------------------------------------------------------------------------------------------------
update_profile_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Person Sign.png"), dark_image=Image.open("Pictures/Person Sign.png"), size = (60,60))
update_profile_button = customtkinter.CTkButton(customerDashboard, text = "Update\nProfile", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#12A85C", corner_radius=20, image = update_profile_image, compound='top', cursor = 'hand', command=open_update_profile_page)
update_profile_button.place(relx = 0.09, rely = 0.33, anchor = "center")

# PAYMENT PLAN -----------------------------------------------------------------------------------------------------------------------------------------------------
payment_plan_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Dollar Sign.png"), dark_image=Image.open("Pictures/Dollar Sign.png"), size = (60,60))
payment_plan_button = customtkinter.CTkButton(customerDashboard, text = "Payment\nPlan", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#12A85C", corner_radius=20, image = payment_plan_image, compound='top', cursor = 'hand', command=open_payment_plan_page)
payment_plan_button.place(relx = 0.29, rely = 0.33, anchor = "center")

# HEALTH HISTORY -----------------------------------------------------------------------------------------------------------------------------------------------------
health_history_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Health Sign.png"), dark_image=Image.open("Pictures/Health Sign.png"), size = (60,60))
health_history_button = customtkinter.CTkButton(customerDashboard, text = "Health\nHistory", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#12A85C", corner_radius=20, image = health_history_image, compound='top', cursor = 'hand', command=open_health_history_page)
health_history_button.place(relx = 0.49, rely = 0.33, anchor = "center")

# VIDEO LINK + CYCLE TRACKING (FEMALE) -----------------------------------------------------------------------------------------------------------------------------------------------------
video_link_button()

# BMI BAR -----------------------------------------------------------------------------------------------------------------------------------------------------

# bmi progress bar
bmi = compute_bmi()
if bmi is None:
    info_label = customtkinter.CTkLabel(bottom_frame, text = " Please add in your height and weight in \nUPDATE PROFILE to display BMI", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
    info_label.place(relx = 0.62, rely = 0.28, anchor = 'w')
else:
    # fat-o-meter label
    fat_o_meter_label = customtkinter.CTkLabel(bottom_frame, text = "Fat-O-Meter", font = customtkinter.CTkFont("Arial", 25, "bold"), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
    fat_o_meter_label.place(relx = 0.62, rely = 0.2, anchor = 'w')
    bmi_category_label = customtkinter.CTkLabel(bottom_frame, text = "", font = customtkinter.CTkFont("Arial", 15), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
    bmi_progress_bar = customtkinter.CTkProgressBar(customerDashboard, orientation = 'horizontal', width = 350, height = 30, border_width = 3, corner_radius=30, border_color='white')
    update_bmi_progress_bar(bmi)
    bmi_progress_bar.place(relx = 0.79, rely= 0.31, anchor = 'center')
    rounded_bmi = round(bmi, 2)
    bmi_value_label = customtkinter.CTkLabel(bottom_frame, text = "Body Mass Index (BMI): " + str(rounded_bmi), font = customtkinter.CTkFont("Arial", 15), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
    bmi_value_label.place(relx = 0.62, rely = 0.32, anchor = 'w')
    bmi_category_label.place(relx = 0.85, rely = 0.32, anchor = 'w')

# GOAL LIST -----------------------------------------------------------------------------------------------------------------------------------------------------

# frame to contain the list
todo_frame = customtkinter.CTkFrame(customerDashboard, width=360, height=350, corner_radius=0, bg_color='#24272C', fg_color='#34383e')
todo_frame.place(relx = 0.61, rely = 0.69, anchor = 'w')

# goals heading
goals_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Goal Sign.png"), dark_image=Image.open("Pictures/Goal Sign.png"), size = (45,45))
my_goals_label = customtkinter.CTkLabel(todo_frame, text = "My Goals", font = customtkinter.CTkFont("Arial", 30, 'bold'), bg_color="#12A85C", text_color="#FFFFFF", fg_color="transparent", height=68, width = 360, image=goals_image, compound='left')
my_goals_label.place(relx = 0.5, rely = 0.1, anchor = 'center')

# add goal button
add_goal_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Plus Sign.png"), dark_image=Image.open("Pictures/Plus Sign.png"), size = (20,20))
add_goal_button = customtkinter.CTkButton(todo_frame, text = "Add Goals", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 35, height = 35, fg_color = "#12A85C", corner_radius=20,image=add_goal_image, compound='left', cursor = 'hand', command=create_goals_list_frame)
add_goal_button.place(relx = 0.5, rely = 0.9, anchor = 'center')

display_uncompleted_goals()

# SELECT TRAINER -----------------------------------------------------------------------------------------------------------------------------------------------------

# trainer frame picture
trainer_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Trainer Frame.png"), dark_image=Image.open("Pictures/Trainer Frame.png"), size = (20,20))

# trainer frame
trainer_frame = customtkinter.CTkFrame(bottom_frame, width = 560, height = 30, corner_radius=0, bg_color='#24272C', fg_color='#24272C', border_width=1, border_color='white')
trainer_frame.place(relx = 0.29, rely = 0.65, anchor = 'center')

#trainer image label
trainer_image_label = customtkinter.CTkLabel(trainer_frame, text = "", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent", image=trainer_image, compound='center')
trainer_image_label.place(relx = 0.02, rely = 0.5, anchor = 'w')

#trainer label
trainer_label = customtkinter.CTkLabel(trainer_frame, text = "Select a Trainer: ", font = customtkinter.CTkFont("Arial", 20), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
trainer_label.place(relx = 0.09, rely = 0.5, anchor = 'w')

#option menu for trainers
def create_option_menu_for_trainers():
        sql_query = "SELECT EmployeeFirstName + ' ' + EmployeeLastName AS FullName FROM Staff WHERE EmployeeDesignation = 'Trainer'"
        cursor.execute(sql_query)
        trainer_names = [row[0] for row in cursor.fetchall()]
        # Create and configure the option menu
        trainer_option_menu = customtkinter.CTkOptionMenu(trainer_frame, width=200, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color="black", values=trainer_names)                
        return trainer_option_menu

trainer_option_menu = create_option_menu_for_trainers()
trainer_option_menu.place(relx = 0.58, rely = 0.5, anchor = 'center')

# save button
save_goal_button = customtkinter.CTkButton(trainer_frame, text="Save", font=customtkinter.CTkFont("Arial Unicode MS", 12), width=80, height=10, fg_color="#12A85C", corner_radius=30, compound='left', cursor='hand', command = save_trainer)
save_goal_button.place(relx=0.9, rely=0.5, anchor='center')










customerDashboard.mainloop()



