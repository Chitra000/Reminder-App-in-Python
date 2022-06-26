from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time
# GUI
t = Tk()
t.title('Desktop Notifier')
t.geometry("500x340")
# img = Image.open("reminder.jpg")
img = Image.open(r"D:\VS Code\Reminder App/Notifier App.jpg")
tkimage = ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)
    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All the fields are required.")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon=r"D:\VS Code\Reminder App/bell.ico",
                            toast=True,
                            timeout=10)

img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, bg="lightgrey", text="Notification Title", relief="raised", font=("poppins", 10))
t_label.place(x=12, y=120)

# Label - Message
m_label = Label(t, bg="lightgrey", text="Description", relief="raised",  font=("poppins", 10))
m_label.place(x=12, y=175)

# Label - Time
time_label = Label(t, bg="lightgrey", text="Set Timer", relief="raised",  font=("poppins", 10))
time_label.place(x=12, y=230)

# Label - min
time_min_label = Label(t, bg="lightgrey", text="in minutes", relief="raised",  font=("poppins", 10))
time_min_label.place(x=170, y=230)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 10))
title.place(x=123, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 10))
msg.place(x=123, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 10))
time1.place(x=123, y=230)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="grey", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=285)

t.resizable(0,0)
t.mainloop()