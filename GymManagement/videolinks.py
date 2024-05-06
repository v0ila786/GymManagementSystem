import customtkinter
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
import subprocess
import sys
import webbrowser

app = customtkinter.CTk()
app.geometry("1000x700+95+1")
app.resizable(True, True)
customtkinter.set_appearance_mode("Dark")
app.title("Fat Man Gym Management System")
app.configure(fg_color="#000000")

def open_customer_dashboard():
    app.destroy()
    subprocess.Popen(['python3', '/Users/amal/Python Projects/Gym Management/GymManagement/customerdashboard.py'])



def open_url(url):
    
    webbrowser.open(url)

def create_video_frame(my_frame, label, video_link):
    # Making a video frame
    new_video = customtkinter.CTkFrame(my_frame, width=390, height=50, fg_color="#000000")  # Updated color
    new_video.pack(side="top", pady=10)

    # Adding label with video information to the frame
    audit_label = customtkinter.CTkLabel(new_video, width=200, height=100, text=f"{label} - ", font=("Doubledecker DEMO", 14, "bold"), bg_color="#3D3B40",fg_color="#000000", text_color="#FFFFFF")
    audit_label.place(relx=0.1, rely=0.5, anchor="w")

    # Adding clickable link using Label
    video_label = tk.Label(new_video, text="Watch Video", font=("Arial", 12), fg="#12A85C", cursor="hand2")
    video_label.place(relx=0.5, rely=0.5, anchor="w")
    video_label.bind("<Button-1>", lambda event, url=video_link: open_url(url))




# gym name heading
heading_label = customtkinter.CTkLabel(app, text="FAT MAN GYM", font=customtkinter.CTkFont("Doubledecker DEMO", 50, "bold"), bg_color='transparent', text_color="#12A85C")  # Updated color
heading_label.pack(pady=10)
# instructional video links label
video_links_label = customtkinter.CTkLabel(app, text="instructional video links", font=customtkinter.CTkFont("Doubledecker DEMO", 20, "bold"), bg_color="transparent", text_color="#12A85C", fg_color="transparent")  # Updated color
video_links_label.pack(pady=12)
# cardio label
cardio_label = customtkinter.CTkLabel(app, text="Cardio Workouts:",width=200,height=50, font=customtkinter.CTkFont("Doubledecker DEMO", 20, "bold"),corner_radius=50, bg_color="transparent", text_color="#FFFFFF", fg_color="#12A85C")  # Updated color
cardio_label.place(relx=0.01, rely=0.2)
# Making a scrollable frame
my_frame_cardio = customtkinter.CTkScrollableFrame(app,width=400, height=45,fg_color="#12A85C")
my_frame_cardio.place(relx=0.01, rely=0.3 )  # Adjust the vertical offset as needed
# Strength Training label
Strength_Training_label = customtkinter.CTkLabel(app, text="Strength Training:",width=200,height=50, font=customtkinter.CTkFont("Doubledecker DEMO", 20, "bold"),corner_radius=50, bg_color="transparent", text_color="#FFFFFF", fg_color="#12A85C")  # Updated color
Strength_Training_label.place(relx=0.5, rely=0.2)
# Making a scrollable frame
my_frame_st = customtkinter.CTkScrollableFrame(app,width=400, height=45,fg_color="#12A85C")
my_frame_st.place(relx=0.5, rely=0.3 )  # Adjust the vertical offset as needed
# Weightlifting: label
Weightlifting_label = customtkinter.CTkLabel(app, text="Weightlifting:",width=200,height=50, font=customtkinter.CTkFont("Doubledecker DEMO", 20, "bold"),corner_radius=50, bg_color="transparent", text_color="#FFFFFF", fg_color="#12A85C")  # Updated color
Weightlifting_label.place(relx=0.01, rely=0.62)
# Making a scrollable frame
my_frame_WL = customtkinter.CTkScrollableFrame(app,width=400, height=45,fg_color="#12A85C")
my_frame_WL.place(relx=0.01, rely=0.7 )  # Adjust the vertical offset as needed
# Flexibility_and_Mobility: label
Flexibility_and_Mobility_label = customtkinter.CTkLabel(app, text="Flexibility_and_Mobility:",width=200,height=50, font=customtkinter.CTkFont("Doubledecker DEMO", 20, "bold"),corner_radius=50, bg_color="transparent", text_color="#FFFFFF", fg_color="#12A85C")  # Updated color
Flexibility_and_Mobility_label.place(relx=0.5, rely=0.62)
# Making a scrollable frame
my_frame_FM = customtkinter.CTkScrollableFrame(app,width=400, height=45,fg_color="#12A85C")
my_frame_FM.place(relx=0.5, rely=0.7 )  # Adjust the vertical offset as needed
video_links_cardio = { 
            "Running": ["https://youtube.com/shorts/8ibLix2XY2I?si=3kakldDjaFXhyjn4"],
            "Cycling": ["https://youtube.com/shorts/YWb0IxZ_Q6M?si=tTfqflVmGJUSyfn-"],
            "(HIIT)": ["https://youtu.be/yDpCTPOlFMg?si=-7f9_oxRiMOrwpQI"],
            "Jump Rope": ["https://youtube.com/shorts/ZT-Q-Tl8y7I?si=4ioK6pHD-w-fMiwP"]
            

}
for label, links in video_links_cardio.items():
    for link in links:
        create_video_frame(my_frame_cardio, label, link)

video_links_Strength_Training = { 
            "Full-body": ["https://youtu.be/nnpwDoD6fyA?si=rdfdL67XvS62IaBO"],
            "Lower body": ["https://youtu.be/-dTh_L0bJvo?si=GsFK-EvZZgeCpfS8"],
            "Core": ["https://youtu.be/1WIah0t1Bzw?si=5ZJayPBCtLSlJ0Ot"],
            "Upper body": ["https://youtu.be/puLJaNv9m18?si=I0Dlv8HtUxme5NLT"]
            

}
for label, links in video_links_Strength_Training.items():
    for link in links:
        create_video_frame(my_frame_st, label, link)

video_links_Weightlifting = { 
            "Full-body": ["https://youtu.be/nnpwDoD6fyA?si=rdfdL67XvS62IaBO"],
            "Lower body": ["https://youtu.be/-dTh_L0bJvo?si=GsFK-EvZZgeCpfS8"],
            "Core": ["https://youtu.be/1WIah0t1Bzw?si=5ZJayPBCtLSlJ0Ot"],
            "Upper body": ["https://youtu.be/puLJaNv9m18?si=I0Dlv8HtUxme5NLT"]
            

}
for label, links in video_links_Weightlifting.items():
    for link in links:
        create_video_frame(my_frame_WL, label, link)

video_links_Flexibility_and_Mobility = { 
            "Full-body": ["https://youtu.be/nnpwDoD6fyA?si=rdfdL67XvS62IaBO"],
            "Lower body": ["https://youtu.be/-dTh_L0bJvo?si=GsFK-EvZZgeCpfS8"],
            "Core": ["https://youtu.be/1WIah0t1Bzw?si=5ZJayPBCtLSlJ0Ot"],
            "Upper body": ["https://youtu.be/puLJaNv9m18?si=I0Dlv8HtUxme5NLT"]
            

}
for label, links in video_links_Flexibility_and_Mobility.items():
    for link in links:
        create_video_frame(my_frame_FM, label, link)

#back button
back_button = customtkinter.CTkButton(app, text="Back", corner_radius=35, fg_color="#12A85C", width=160, height=30, cursor="hand2", command=open_customer_dashboard)
back_button.place(relx=0.1, rely=0.1, anchor="center")


app.mainloop()

       