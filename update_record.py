import tkinter as tk
from tkinter import ttk
import pyodbc

connection = pyodbc.connect("DRIVER={SQL Server};"
                            'SERVER=DESKTOP-QUL15MQ;'
                            'DATABASE=master;' 
                            'Trusted_conn=yes;')

# Function to retrieve data from the database
def fetch_data():
    cursor = connection.cursor()
    sql_query = "SELECT * FROM customer"
    cursor.execute(sql_query)
    return cursor.fetchall()

def update_data(id, new_value):
    cursor = connection.cursor()
    sql_query = "UPDATE customer SET email = ? WHERE id = ?"
    print(sql_query)

        # Execute the query with the form data
    cursor.execute(sql_query, (new_value, id))
    connection.commit()
    

# Function to display data in the tkinter Treeview
def show_data():
    data = fetch_data()
    print(data)
    
    tree.delete(*tree.get_children())  # Clear previous data from Treeview
    for row in data:
    
        id, name, email, number , address , phone= row
        tree.insert("", "end", values=(id, name, email, number , address , phone))

# Function to handle the Update button click
def update_button_click():
    selected_item = tree.selection()
    selected = updated_value.get()

    print(selected_item)
    if selected_item:
        selected = tree.item(selected_item, "values")[0]
        new_value = updated_value.get()
        update_data(selected, new_value)
        show_data()

# Create the main Tkinter window
root = tk.Tk()
root.title("update record")

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("ID", "name", "email", "number"))
tree.heading("#0", text="")
tree.heading("ID", text="ID")
tree.heading("name", text="name")
tree.heading("email", text="email")
tree.heading("number", text="number")
tree.pack()


# Button to update data
update_label = tk.Label(root, text="Enter new value:")
update_label.pack()
updated_value = tk.Entry(root)
updated_value.pack()
update_button = tk.Button(root, text="Update", command=update_button_click)
update_button.pack()

# Show data in the Treeview
show_data()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when the GUI is closed
connection.close()
