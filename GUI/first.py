from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

root = Tk()
root.title("GIET ERP Login")
root.geometry("500x500")
root.configure(bg="#1E3D59")  


# image path
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "star.png")

# window icon
icon = PhotoImage(file=image_path)
root.iconphoto(False, icon)

bg_path = os.path.join(current_path,"download.jpg") 
bg_img = Image.open(bg_path)
bg_img = bg_img.resize((1500, 700))
bg_img = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------- LOGIN FUNCTION ----------
def login_function():
    email = email_entry.get()
    password = password_entry.get()

    correct_email = "sidhi@gmail.com"
    correct_password = "12345"

    if email == correct_email and password == correct_password:
        messagebox.showinfo("Login Success", "Welcome to GIET Bucks")
    else:
        messagebox.showerror("Login Failed", "Invalid Email or Password")


# ---------- LOGIN CARD ----------
frame = Frame(root, bg="white", width=360, height=400)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# logo
img = Image.open(image_path)
resize_img = img.resize((90,70))
img = ImageTk.PhotoImage(resize_img)

logo = Label(frame, image=img, bg="white")
logo.pack(pady=15)

# title
title = Label(frame,
              text="GIET ERP",
              font=("Arial",22,"bold"),
              bg="white",
              fg="#1E3D59")
title.pack()

subtitle = Label(frame,
                 text="Student Login",
                 font=("Arial",12),
                 bg="white",
                 fg="grey")
subtitle.pack(pady=(0,10))

# email
email_label = Label(frame,
                    text="Email",
                    font=("Arial",12),
                    bg="white")
email_label.pack(pady=(10,3))

email_entry = Entry(frame,
                    font=("Arial",12),
                    width=28,
                    bd=1,
                    relief="solid")
email_entry.pack(ipady=4)

# password
password_label = Label(frame,
                       text="Password",
                       font=("Arial",12),
                       bg="white")
password_label.pack(pady=(12,3))

password_entry = Entry(frame,
                       font=("Arial",12),
                       width=28,
                       show="*",
                       bd=1,
                       relief="solid")
password_entry.pack(ipady=4)

# login button
login_btn = Button(frame,
                   text="LOGIN",
                   font=("Arial",12,"bold"),
                   bg="#1E3D59",
                   fg="white",
                   width=20,
                   pady=5,
                   command=login_function)

login_btn.pack(pady=20)

# footer
footer = Label(frame,
               text="© GIET University",
               font=("Arial",9),
               bg="white",
               fg="grey")
footer.pack(side="bottom", pady=10)

root.mainloop()