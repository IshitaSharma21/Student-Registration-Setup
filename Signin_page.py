from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


# Function Part
def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password Don_t Match', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='renu1976',database='userdata')
            mycursor = con.cursor()
            query='select * from userdata where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='Update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user))


    window=Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='L.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='Reset Password', font=('times new roman','18','bold'), bg='white', fg='royal blue')
    heading_label.place(x=480, y=60)

    userLabel = Label(window, text='Username', font=('arial',12,'bold'), fg='blue')
    userLabel.place(x=470,y=130)

    user_entry= Entry(window, width=25, fg='blue', font=('arial',11,'bold'),bd=0)
    user_entry.place(x=470,y=160)

    Frame(window, width=250, height=2, bg='blue').place(x=470, y=180)

    passwordLabel = Label(window, text='New Password', font=('arial',11,'bold'),fg='blue')
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='royal blue', font=('arial',11,'bold'),bd='0')
    newpass_entry.place(x=470, y=240)

    Frame(window, width=220, height=2, bg='blue').place(x=470,y=260)

    confirmpassLabel= Label(window, text='Confirm Password', font=('arial',11,'bold'),bg='white', fg='blue')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='royal blue',font=('arial', 11,'bold'),bd=0)
    confirmpass_entry.place(x=470,y=320)

    Frame(window,width=220,height=2, bg='blue').place(x=470,y=340)

    submitButton = Button(window, text='Submit',bd=0,bg='blue',fg='white',font=('arial',16,'bold'),width=19,cursor='hand2',command=change_password)
    submitButton.place(x=470, y=390)


    window.mainloop()


def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
           con=pymysql.connect(host='localhost', user='root', password='renu1976')
           mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query='select* from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')

        else:
            messagebox.showerror('Welcome','Login is successful')
def user_enter(event):  # when click on username it will disappear
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def pass_enter(event):  # when click on username it will disappear
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def Signup_page():
    login_window.destroy()
    import Signup_page


# GUI Part
login_window = Tk()
login_window.resizable(0, 0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='Background.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.grid(row=0, column=0)
frame = Frame(login_window, bg='white')
frame.place(x=430, y=19)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 15, 'bold'),
                bg='White', fg='royal blue')
heading.place(x=500, y=40)

# Username Section
usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 10),
                      bg='White', bd=0, fg='blue', )
usernameEntry.place(x=475, y=80)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)  # calling Function

frame1 = Frame(login_window, width=180, height=2, bg='blue'
               ).place(x=475, y=100)

# Password Section
passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 10),
                      bg='White', bd=0, fg='blue', )
passwordEntry.place(x=475, y=120)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', pass_enter)

frame2 = Frame(login_window, width=180, height=2, bg='blue'
               ).place(x=475, y=140)

# eye Button Section
# open eye
openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='White', activebackground='White'
                   , cursor='hand2', command=hide)
eyeButton.place(x=628, y=113)

# Forget Password Section
forgotButton = Button(login_window, text='Forgot Password?', bd=0, bg='White', activebackground='White'
                      , cursor='hand2', font=('Microsoft Yahei UI Light', 8)
                      , fg='blue', activeforeground='blue',command=forget_pass)

forgotButton.place(x=560, y=150)

# login Button Section

LoginButton = Button(login_window, text='Login', bd=0, bg='blue', activebackground='blue'
                     , cursor='hand2', font=('Open Sans', 15, 'bold')
                     , fg='white', activeforeground='white', width=15 , command=login_user)

LoginButton.place(x=470, y=200)

# ---OR--- Section
orLabel = Label(login_window, text='------------OR------------', font=('Open Sans', 16) ,bd='0'
                , fg='blue')
orLabel.place(x=460, y=250)

# logos Section
facebook_logo = PhotoImage(file='facebook.png')
fblabel = Label(login_window, image=facebook_logo, bg='White')
fblabel.place(x=510, y=300, )

google_logo = PhotoImage(file='google.png')
glabel = Label(login_window, image=google_logo, bg='White')
glabel.place(x=550, y=300)

twitter_logo = PhotoImage(file='twitter.png')
tlabel = Label(login_window, image=twitter_logo,
               bg='White')
tlabel.place(x=590, y=300)

# don't have an account section
signupLabel = Label(login_window, text='Dont have an account?', font=('Open Sans', 9, 'bold'), bg='White'
                    , )
signupLabel.place(x=440, y=350)

# create new account button
createButton = Button(login_window, text='Create New Account', bd=0, bg='White', activebackground='White'
                      , cursor='hand2', font=('Open Sans', 9, 'bold underline')
                      , fg='blue', activeforeground='blue', command=Signup_page)

createButton.place(x=560, y=368)

login_window.mainloop()
