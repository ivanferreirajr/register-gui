# Setup
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import database

# Creating window
window = Tk()
window.title("Escola de Bruxaria - Login")
window.geometry("600x300")
window.configure(background="white")
window.resizable(width=False, height=False)
window.iconbitmap(default="icons/wizard.ico")

# Load Image
logo = PhotoImage(file="icons/wizard.png")

# Background Color
bg_color = "#2E454F"

# Widgets
left_frame = Frame(window, width=200, height=300, bg=bg_color, relief="raise")
left_frame.pack(side=LEFT)

right_frame = Frame(window, width=400, height=300, bg=bg_color, relief="raise")
right_frame.pack(side=RIGHT)

logo_label = Label(left_frame, image=logo, bg=bg_color)
logo_label.place(x=50, y=100)

user_label = Label(right_frame, text="Username:", font=("Montserrat", 16), bg=bg_color, fg="white")
user_label.place(x=30, y=100)

user_entry = ttk.Entry(right_frame, width=30)
user_entry.place(x=150, y=110)

pass_label = Label(right_frame, text="Password:", font=("Montserrat", 16), bg=bg_color, fg="white")
pass_label.place(x=40, y=150)

pass_entry = ttk.Entry(right_frame, width=30, show="*")
pass_entry.place(x=150, y=160)

def login():
    user = user_entry.get()
    password = pass_entry.get()

    database.cursor.execute("""
        SELECT * FROM users
        WHERE (username = ? and password = ?)
    """, (user, password))

    verify_login = database.cursor.fetchone()

    try:
        if (user in verify_login and password in verify_login):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem-vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique os dados inseridos.")

# Buttons
login_btn = ttk.Button(right_frame, text="Login", width=20, command=login)
login_btn.place(x=125, y=220)

def register():
    # Removing
    login_btn.place(x=5000)
    register_btn.place(x=5000)

    # Inserting 
    nome_label = Label(right_frame, text="Name:", font=("Montserrat", 16), bg=bg_color, fg="white")
    nome_label.place(x=73, y=15)

    nome_entry = ttk.Entry(right_frame, width=30)
    nome_entry.place(x=150, y=25)

    email_label = Label(right_frame, text="E-mail:", font=("Montserrat", 16), bg=bg_color, fg="white")
    email_label.place(x=73, y=55)

    email_entry =ttk. Entry(right_frame, width=30)
    email_entry.place(x=150, y=66)

    def register_database():
        nome = nome_entry.get()
        email = email_entry.get()
        user = user_entry.get()
        password = pass_entry.get()

        if (nome=="" or email=="" or user=="" or password==""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos!")
        else:
            database.cursor.execute("""
                INSERT INTO users (name, email, username, password) VALUES(?, ?, ?, ?)
            """, (nome, email, user, password))
            database.db.commit()
            messagebox.showinfo(title="Register Info", message="Conta cadastrada com sucesso!")

    register = ttk.Button(right_frame, text="Register", width=20, command=register_database)
    register.place(x=125, y=225)

    def back_login():
        # Removing register
        nome_label.place(x=5000)
        nome_entry.place(x=5000)
        email_label.place(x=5000)
        email_entry.place(x=5000)
        register.place(x=5000)
        back.place(x=5000)

        # Pushing login
        login_btn.place(x=100)
        register_btn.place(x=100)

    back = ttk.Button(right_frame, text="Back", width=20, command=back_login)
    back.place(x=125, y=260)

register_btn = ttk.Button(right_frame, text="Register", width=20, command=register)
register_btn.place(x=125, y=250)

window.mainloop()