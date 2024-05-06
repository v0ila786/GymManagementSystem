import customtkinter
from PIL import Image, ImageTk
import GlobalVariables
import pyodbc
from datetime import datetime
import emoji

# Establish connection with the database
server = 'localhost'
database = 'Gym Management 1'
username = 'sa'
password = 'AmalAsim@2002'
connection_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes'
connection = pyodbc.connect(connection_str)
cursor = connection.cursor()

# get name of logged in user
def get_logged_in_person_name():
    sql_query = "SELECT CustomerFirstName FROM Customer WHERE UserID = ?"
    cursor.execute(sql_query, (GlobalVariables.logged_in_person))
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
    sql_query = "SELECT CustomerGender FROM Customer WHERE UserID = ?"
    cursor.execute(sql_query, (GlobalVariables.logged_in_person))
    userGender = cursor.fetchone()[0]
    print(userGender)
    return userGender

# Video Link + Cycle Tracking buttons on dashboard based on gender
def video_link_button():
    gender = get_logged_in_person_gender()
    video_link_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Video Sign.png"), dark_image=Image.open("Pictures/Video Sign.png"), size = (60,60))
    if gender == 'Male':
        video_link_button = customtkinter.CTkButton(customerDashboard, text = "Instructional Video Links", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 560, height = 100, fg_color = "#12A85C", corner_radius=20, image = video_link_image, compound='left', cursor = 'hand')
        video_link_button.place(relx = 0.01, rely = 0.52, anchor = "w")
    else:
        cycle_tracking_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Drop Sign.png"), dark_image=Image.open("Pictures/Drop Sign.png"), size = (40,40))
        video_link_button = customtkinter.CTkButton(customerDashboard, text = "Instructional Video Links", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 360, height = 100, fg_color = "#12A85C", corner_radius=20, image = video_link_image, compound='left', cursor = 'hand')
        video_link_button.place(relx = 0.01, rely = 0.52, anchor = "w")
        cycle_tracking_button = customtkinter.CTkButton(customerDashboard, text = "Cycle\nTracking", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 50, fg_color = "#12A85C", corner_radius=20, image = cycle_tracking_image, compound='top', cursor = 'hand')
        cycle_tracking_button.place(relx = 0.41, rely = 0.52, anchor = "w")

# compute bmi value from height and weight
def compute_bmi():
    # get height in cm
    sql_query_height = "SELECT CustomerHeight FROM Customer WHERE UserID = ?"
    cursor.execute(sql_query_height, (GlobalVariables.logged_in_person))
    userHeight = float(cursor.fetchone()[0])
    sql_query_weight = "SELECT CustomerWeight FROM Customer WHERE UserID = ?"
    cursor.execute(sql_query_weight, (GlobalVariables.logged_in_person))
    userWeight = float(cursor.fetchone()[0])
    bmi = userWeight / ((userHeight / 100) ** 2)
    print(bmi)
    sql_query_store_bmi = "UPDATE Customer SET CustomerBMI = ? WHERE UserID = ?"
    cursor.execute(sql_query_store_bmi, (bmi, GlobalVariables.logged_in_person))
    cursor.commit()
    return bmi

# Change color on progress bar relative to BMI
def update_bmi_progress_bar(bmi):
    value = 0
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


# create frames for todo list  # NOTE TO SELF: UPDATE THIS
def create_todo_list_frame(rely):
    if GlobalVariables.number_of_goals == 6:
        return
    print(GlobalVariables.goal_rely)
    # goal frame
    goal_frame = customtkinter.CTkFrame(todo_frame, width = 360, height = 30, corner_radius=0, bg_color='#24272C', fg_color='#24272C', border_width=1, border_color='white')
    goal_frame.place(relx = 0.5, rely = GlobalVariables.goal_rely, anchor = 'center')
    GlobalVariables.goal_rely = GlobalVariables.goal_rely + 0.1
    GlobalVariables.number_of_goals = GlobalVariables.number_of_goals + 1
    # switch
    goal_switch_var = customtkinter.StringVar(value="on")
    goal_switch = customtkinter.CTkSwitch(goal_frame, text = " ", variable=goal_switch_var, onvalue="on", offvalue="off", progress_color='#12A85C')
    goal_switch.deselect()
    goal_switch.place(relx = 0.15, rely = 0.5, anchor = 'center')
    # goal list
    goal_list = customtkinter.CTkOptionMenu(goal_frame, values=["Weight Loss", "Strength Training", "Cardio Training", "Muscle Toning", "Lower Body Training", "Upper Body Training"], width=150, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color='black')
    goal_list.place(relx = 0.4, rely = 0.5, anchor = 'center')
    #target date
    target_date_list = customtkinter.CTkOptionMenu(goal_frame, values=["1 Week", "1 Month", "3 Months", "6 Months", "1 Year"], width=100, height=20, fg_color="#FFFFFF", button_color="#12A85C", text_color='black')
    target_date_list.place(relx = 0.7, rely = 0.5, anchor = 'w')


    





   
    


   


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
sign_out_button = customtkinter.CTkButton(top_frame, text = "Sign Out", height = 40, corner_radius=0, fg_color="transparent", bg_color="transparent", hover_color="#12A85C", cursor = "hand", width = 120, border_width=0.6, image = sign_out_image)
sign_out_button.place(relx = 0.93, rely = 0.5, anchor = "center")

# WELCOME LABEL -----------------------------------------------------------------------------------------------------------------------------------------------------
time_greeting()

# UPDATE PROFILE -----------------------------------------------------------------------------------------------------------------------------------------------------
update_profile_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Person Sign.png"), dark_image=Image.open("Pictures/Person Sign.png"), size = (60,60))
update_profile_button = customtkinter.CTkButton(customerDashboard, text = "Update\nProfile", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#12A85C", corner_radius=20, image = update_profile_image, compound='top', cursor = 'hand')
update_profile_button.place(relx = 0.09, rely = 0.33, anchor = "center")

# PAYMENT PLAN -----------------------------------------------------------------------------------------------------------------------------------------------------
payment_plan_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Dollar Sign.png"), dark_image=Image.open("Pictures/Dollar Sign.png"), size = (60,60))
payment_plan_button = customtkinter.CTkButton(customerDashboard, text = "Payment\nPlan", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#12A85C", corner_radius=20, image = payment_plan_image, compound='top', cursor = 'hand')
payment_plan_button.place(relx = 0.29, rely = 0.33, anchor = "center")

# HEALTH HISTORY -----------------------------------------------------------------------------------------------------------------------------------------------------
health_history_image = customtkinter.CTkImage(light_image=Image.open("Pictures/Health Sign.png"), dark_image=Image.open("Pictures/Health Sign.png"), size = (60,60))
health_history_button = customtkinter.CTkButton(customerDashboard, text = "Health\nHistory", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 160, height = 100, fg_color = "#12A85C", corner_radius=20, image = health_history_image, compound='top', cursor = 'hand')
health_history_button.place(relx = 0.49, rely = 0.33, anchor = "center")

# VIDEO LINK + CYCLE TRACKING (FEMALE) -----------------------------------------------------------------------------------------------------------------------------------------------------
video_link_button()

# BMI BAR -----------------------------------------------------------------------------------------------------------------------------------------------------

# fat-o-meter label
fat_o_meter_label = customtkinter.CTkLabel(bottom_frame, text = "Fat-O-Meter", font = customtkinter.CTkFont("Arial", 25, "bold"), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
fat_o_meter_label.place(relx = 0.62, rely = 0.2, anchor = 'w')

# bmi progress bar
bmi_category_label = customtkinter.CTkLabel(bottom_frame, text = "", font = customtkinter.CTkFont("Arial", 15), bg_color="transparent", text_color="#FFFFFF", fg_color="transparent")
bmi_progress_bar = customtkinter.CTkProgressBar(customerDashboard, orientation = 'horizontal', width = 350, height = 30, border_width = 3, corner_radius=30, border_color='white')
bmi = compute_bmi()
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
add_goal_button = customtkinter.CTkButton(todo_frame, text = "Add Goals", font = customtkinter.CTkFont("Arial Unicode MS", 20), width = 35, height = 35, fg_color = "#12A85C", corner_radius=20,image=add_goal_image, compound='left', cursor = 'hand', command=lambda: create_todo_list_frame(GlobalVariables.goal_rely))
add_goal_button.place(relx = 0.5, rely = 0.9, anchor = 'center')























customerDashboard.mainloop()



