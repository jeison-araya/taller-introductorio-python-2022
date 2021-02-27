from tkinter import Tk      # root
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import messagebox

# Root configuration.

root = Tk()
root.title('Inicio de sesión')
root.config(bg='#87CEEB')
root.geometry('350x400') # width x high.

# Frame Configuration.

login_frame = Frame(root, bg='#87CEEB')
login_frame.pack()

# Title Label

title_label = Label(login_frame,
                    text='Iniciar sesión',
                    padx=40,
                    pady=20,
                    bg='#87CEEB')
title_label.grid(row=0, column=0, columnspan=2)

# Username Label

username_label = Label(login_frame, 
                       text='Usuario:', 
                       padx=10, 
                       pady=10,
                       bg='#87CEEB')
username_label.grid(row=1, column=0)

# Username Entry

username_entry = Entry(login_frame, width=30)
username_entry.grid(row=1, column=1)

# Password Label

password_label = Label(login_frame, 
                       text='Contraseña:', 
                       padx=10,
                       pady=10,
                       bg='#87CEEB')
password_label.grid(row=2, column=0)

# Password Entry

password_entry = Entry(login_frame, width=30, show='*')
password_entry.grid(row=2, column=1)

# Submit Button

def submit():
    """This function sends the information of the form."""
    username = username_entry.get()
    password = password_entry.get()
    
    data = {'username':username,
            'password':password}
    
    messagebox.showinfo(title='Formulario enviado', message=data)

submit_button = Button(login_frame,
                       text='Ingresar',
                       command=submit,
                       padx=10,
                       pady=10)
submit_button.config(width=10)
submit_button.grid(row=3, column=0, columnspan=2)

# Run application.

root.mainloop()