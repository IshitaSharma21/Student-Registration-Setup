from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirm_passwordEntry.delete(0, END)


def Signin_page():
    Signup_window.destroy()
    import Signin_page


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirm_passwordEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif passwordEntry.get() != confirm_passwordEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='renu1976')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue')
            return
        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
           messagebox.showerror('Error', 'Username Already Exists')
           
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            Signup_window.destroy()
            import Signin_page

Signup_window = Tk()
Signup_window.title('Signup Page')
Signup_window.resizable(False, False)

# background Image
bgImage = ImageTk.PhotoImage(file='L.jpg')
bgLabel = Label(Signup_window, image=bgImage)
bgLabel.grid(row=0, column=0)

frame = Frame(Signup_window, bg='white')
frame.place(x=580, y=30)

# Heading Section
heading = Label(frame, text='CREATE AN ACCOUNT', font=('Times New Roman', 15, 'bold'),
                bg='White', fg='Royalblue')
heading.grid(row=0, column=0, padx=10, pady=10)

# Email Section
emailLabel = Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='White'
                   , fg='Blue')
emailLabel.grid(row=1, column=0, padx=10, sticky='w', pady=(10, 0))

emailEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 8,), fg='Black', bg='White')
emailEntry.grid(row=2, column=0, sticky='w', padx=10, )

# Username Section
usernameLabel = Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='White'
                      , fg='blue')
usernameLabel.grid(row=3, column=0, padx=10, sticky='w', pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 8,), fg='Black', bg='White')
usernameEntry.grid(row=4, column=0, sticky='w', padx=10, )

# Password Section
passwordLabel = Label(frame, text='Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='White'
                      , fg='blue')
passwordLabel.grid(row=5, column=0, padx=10, sticky='w', pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 8,), fg='Black', bg='White')
passwordEntry.grid(row=6, column=0, sticky='w', padx=10, )

# Confirm Password
confirm_passwordLabel = Label(frame, text='Confirm Password', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='White'
                              , fg='blue')
confirm_passwordLabel.grid(row=7, column=0, padx=10, sticky='w', pady=(10, 0))

confirm_passwordEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 8,), fg='Black', bg='White')
confirm_passwordEntry.grid(row=8, column=0, sticky='w', padx=10, )

# Check Button

check = Checkbutton(frame, text='I agree to the Term & Conditions', font=('Microsoft Yahei UI Light', 8,), bg='White',
                    fg='blue', activebackground='White',
                    activeforeground='Firebrick1', cursor='hand2')
check.grid(row=9, column=0, sticky='w', padx=10, pady=15)

# Sign Up Button
SignUpButton = Button(frame, text='SignUp', bd=0, bg='blue', activebackground='Firebrick1'
                      , cursor='hand2', font=('Open Sans', 15, 'bold')
                      , fg='white', activeforeground='white', width=15, command=connect_database)

SignUpButton.grid(row=10, column=0)

# don't have an account section
signupLabel = Label(frame, text='Dont have an account?', font=('Open Sans', 9, 'bold'), bg='White'
                    , fg='blue')
signupLabel.grid(row=11, column=0, sticky='w', padx=10, pady=15)

# login Button
loginbutton = Button(frame, text='Log In', font=('Open Sans', 9, 'bold '), bd=0, bg='White',
                     activebackground='White', cursor='hand2',
                     activeforeground='blue', fg='blue', command=Signin_page)
loginbutton.place(x=150, y=378)

Signup_window.mainloop()
