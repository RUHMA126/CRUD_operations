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
    sql_query = "SELECT * FROM customersss"
    cursor.execute(sql_query)
    return cursor.fetchall()

def show_data():
    data = fetch_data()
    print(data)
    
    tree.delete(*tree.get_children())  # Clear previous data from Treeview
    for row in data:
    
        id, name, email, phone, address = row
        tree.insert("", "end", values=(id, name, email, phone, address))


def delete_record():
    record_id = updated_value.get()

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # SQL query to delete the record with the given ID
    sql_query = "DELETE FROM customersss WHERE id = ?"

    # Execute the DELETE query with the record ID as a parameter
    cursor.execute(sql_query, record_id)

    # Commit the changes to the database
    connection.commit()

    # Clear the entry field after deletion
    updated_value.delete(0, tk.END)

    # Show updated data in the Treeview
    show_data()

root = tk.Tk()
root.title("delete record")

# Create a Treeview widget to display the data
tree = ttk.Treeview(root, columns=("ID", "name", "email", "phone" , 'address'))
tree.heading("#0", text="")
tree.heading("ID", text="ID")
tree.heading("name", text="name")
tree.heading("email", text="email")
tree.heading("phone", text="phone")
tree.heading("address", text="address")
tree.pack()


# Button to update data
update_label = tk.Label(root, text="enter id to delete the record:")
update_label.pack()
updated_value = tk.Entry(root)
updated_value.pack()
update_button = tk.Button(root, text="delete", command=delete_record)
update_button.pack()

# Show data in the Treeview
show_data()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when the GUI is closed
connection.close()