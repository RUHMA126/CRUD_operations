
import tkinter as tk
import pyodbc
from tkinter import *
window = tk.Tk()
connection = pyodbc.connect('Driver={SQL Server};'
                                'Server=DESKTOP-QUL15MQ;'
                                'Database=master;'
                                'Trusted_Connection=yes;')

Label(window , text='product information' , font='arial 15 bold').grid(row=0 , column=3)
def submit_form():
    name = namevalue.get()
    price = pricevalue.get()


    cursor = connection.cursor()

    # SQL query to insert the data into the "customer" table
    sql_query = "INSERT INTO product (name, price) VALUES (?, ?)"

    # Execute the query with the form data
    cursor.execute(sql_query, (name, price))

    # Commit the changes to the database
    connection.commit()

    # Close the connection
    connection.close()

    # Clear the form fields after inserting the data
    nameentry.delete(0, tk.END)
    priceentry.delete(0, tk.END)
window.geometry('1200x500')
name = Label(window , text='name')
price = Label(window , text='price')


name.grid(row=1 , column=2)
price.grid(row=2 , column=2)


namevalue = StringVar()
pricevalue = StringVar()


nameentry = Entry(window , textvariable=namevalue)
priceentry = Entry(window , textvariable=pricevalue)


nameentry.grid(row=1 , column=3)
priceentry.grid(row=2 , column=3)

btn = tk.Button(window, text="Submit" , command = submit_form)
btn.grid(row=5, column=3)


window.mainloop()