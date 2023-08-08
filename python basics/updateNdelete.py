import tkinter as tk
from tkinter import ttk
import pyodbc

# Establish a connection to the database
connection = pyodbc.connect("DRIVER={SQL Server};"
                            'SERVER=DESKTOP-QUL15MQ;'
                            'DATABASE=master;' 
                            'Trusted_conn=yes;')


# Function to retrieve data from the database
def fetch_data():
    cursor = connection.cursor()
    sql_query = "select * from customer"
    result = cursor.execute(sql_query).fetchall()
    cursor.close()
    return result

# Function to update data in the database
def update_data(id, new_value):
    cursor = connection.cursor()
    sql_query ="UPDATE customer SET customer = ? WHERE id = ?"
    cursor.execute(sql_query, (new_value, id))
    connection.commit()
    cursor.close()

# Function to delete data from the database
def delete_data(id):
    cursor = connection.cursor()
    sql_query = "DELETE FROM customer WHERE id = ?"
    cursor.execute(sql_query, (id,))
    connection.commit()
    cursor.close()

# Function to display data in the tkinter Treeview
def show_data():
    data = fetch_data()
    tree.delete(*tree.get_children())  # Clear previous data from Treeview

    for row in data:
        tree.insert("", "end", values=row)

# Function to handle the Update button click
def update_button_click():
    selected_item = tree.selection()
    if selected_item:
        id = tree.item(selected_item, "values")[0]
        new_value = updated_value.get()
        update_data(id, new_value)
        show_data()

# Function to handle the Delete button click
def delete_button_click():
    selected_item = tree.selection()
    if selected_item:
        id = tree.item(selected_item, "values")[0]
        delete_data(id)
        show_data()

# Create the main Tkinter window
root = tk.Tk()
root.title("Data Management")

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("ID", "name", "email", "password"))
tree.heading("#0", text="")
tree.heading("ID", text="ID")
tree.heading("name", text="name")
tree.heading("email", text="email")
tree.heading("password", text="password")
tree.pack()

# Button to update data
update_label = tk.Label(root, text="Enter new value:")
update_label.pack()
updated_value = tk.Entry(root)
updated_value.pack()
update_button = tk.Button(root, text="Update", command=update_button_click)
update_button.pack()

# Button to delete data
delete_button = tk.Button(root, text="Delete", command=delete_button_click)
delete_button.pack()

# Show data in the Treeview
show_data()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when the GUI is closed
connection.close()


