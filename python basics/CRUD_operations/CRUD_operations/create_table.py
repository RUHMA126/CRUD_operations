
import tkinter as tk
import pyodbc
from tkinter import *
window = tk.Tk()
connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-QUL15MQ;'
                                'Database=master;'
                                'Trusted_Connection=yes;')

Label(window , text='Customer registration form' , font='arial 15 bold').grid(row=0 , column=3)
def submit_form():

    name = namevalue.get()
    email = emailvalue.get()
    phone = phonevalue.get()
    address = addressvalue.get()

    cursor = connection.cursor()

    # SQL query to insert the data into the "customer" table
    sql_query = "INSERT INTO customer (name, email, phone, address , password) VALUES (?, ?, ?, ?)"

    # Execute the query with the form data
    cursor.execute(sql_query, (name, email, phone, address ))

    # Commit the changes to the database
    connection.commit()

    # Close the connection
    connection.close()

    # Clear the form fields after inserting the data
    nameentry.delete(0, tk.END)
    emailentry.delete(0, tk.END)
    phoneentry.delete(0, tk.END)
    addressentry.delete(0, tk.END)

window.geometry('1200x500')

name = Label(window , text='name')
email = Label(window , text='email')
phone = Label(window , text='phone')
address = Label(window , text='address')


name.grid(row=1 , column=2)
email.grid(row=2 , column=2)
phone.grid(row=3 , column=2)
address.grid(row=4 , column=2)

namevalue = StringVar()
emailvalue = StringVar()
phonevalue = StringVar()
addressvalue = StringVar()

nameentry = Entry(window , textvariable=namevalue)
emailentry = Entry(window , textvariable=emailvalue)
phoneentry = Entry(window , textvariable=phonevalue)
addressentry = Entry(window , textvariable=addressvalue)

nameentry.grid(row=1 , column=3)
emailentry.grid(row=2 , column=3)
phoneentry.grid(row=3 , column=3)
addressentry.grid(row=4 , column=3)


btn = tk.Button(window ,text="Submit" , command=submit_form)
btn.grid(row=5,column=3)


window.mainloop()
