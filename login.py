#importing tools 
import sqlite3
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk

#defining the things that the app would do after the login process

def login():
    user = username.get()
    code = password.get()

    if user == 'shemsu' and code == '1234':
        root = Toplevel(screen)
        root.title('Inventory system')
        root.geometry('1200x600')

        #app code
        
        #endcode

    #all alerts, when someone try to enter wrong username and password

    elif user == '' and code == "" or  user == ' ' and code == ' ':
        messagebox.showerror('Invaild','Please enter username and password')
    elif user == '' or user==' ':
        messagebox.showerror('Invaild','Please enter username')
    elif code == '' or code == ' ':
        messagebox.showerror('Invaild','Please enter password')
    elif user!='shemsu' and code!='1234':
        messagebox.showerror('Invaild','Please enter correct username and password')
    elif user!='shemsu':
        messagebox.showerror('Invaild','Please enter correct username ')
    elif code!='1234':
        messagebox.showerror('Invaild','Please enter correct password ')





def main_screen():

    global screen
    global username
    global password

#creating login

    screen = Tk()
    screen.geometry('1200x700')
    screen.configure(bg = 'blue')

    #icon 
    image_icon = PhotoImage(file = 'login.png')
    screen.iconphoto(False, image_icon)
    screen.title('Login')

    lblTitle = Label(text='login',font=('arial bold',50),bg='#d7dae2',fg='black')
    lblTitle.pack(pady=50)

    bordercolor = Frame(screen,bg='black',width=800,height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor,bg='#d7dae2',width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text='username',font=('arial',30,'bold'),bg='#d7dae2').place(x=100,y=50)
    Label(mainframe,text='password',font=('arial',30,'bold'),bg='#d7dae2').place(x=100,y=150)


    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe,textvariable=username,width=12,bd=2,font=('arial',30))
    entry_username.place(x=400,y=50)
    entry_password = Entry(mainframe,textvariable=password,width=12,bd=2,font=('arial',30),show='*')
    entry_password.place(x=400,y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe,text='Login',height=2,width=23,bg='#00bd56',fg='white',bd=0, command=login).place(x=100,y=250)
    Button(mainframe,text='Reset',height=2,width=23,bg='#1089ff',fg='white',bd=0, command=reset).place(x=300,y=250)
    Button(mainframe,text='Exit',height=2,width=23,bg='#ed3833',fg='white',bd=0,command=screen.destroy).place(x=500,y=250)

    screen.mainloop()

main_screen()