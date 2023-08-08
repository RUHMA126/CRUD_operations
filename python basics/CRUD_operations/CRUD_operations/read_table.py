import tkinter as tk
from tkinter import ttk
import pyodbc

# Establish a connection to the database
connection = pyodbc.connect("DRIVER={SQL Server};"
                            'SERVER=DESKTOP-QUL15MQ;'
                            'DATABASE=master;'
                            'Trusted_conn=yes;')

# Function to retrieve data from the joined table
def fetch_data():
    cursor = connection.cursor()
    sql_query = """
    SELECT orders.order_number , customer.name , product.name , order_detail.quantity , orders.total_amount , product.price 
    FROM order_detail 
    INNER JOIN orders ON order_detail.order_id = orders.order_id
    JOIN product ON product.id = order_detail.product_id
    JOIN customer ON customer.id = orders.customer_id
    """
    result=  cursor.execute(sql_query).fetchall()
    print(result)
    ##data = result.fetchall()
    cursor.close()
    return result

# Function to create a new window and display the data
def show_join_table():
    data = fetch_data()
    print(data)

   
  

    # Create a new Tkinter Toplevel window
    window = tk.Toplevel(root)
    window.title("Joined Table Data")

    # Create a Treeview widget to display the data in the new window
    tree = ttk.Treeview(window)
    tree["columns"] = ( "order_number", "Customer", "product", "quantity", "total_amount", "price" )

    # Add column headings
    tree.heading( "#0", text="", anchor="center" )
    tree.heading( "order_number", text="Order number" )
    tree.heading ( "Customer", text="Customer" )
    tree.heading( "product", text="Product" )
    tree.heading( "quantity", text="Quantity" )
    tree.heading("total_amount", text="Total Amount")
    tree.heading("price", text="Price")

    # Add data to the Treeview
    for i, row in enumerate(data):
        print(i,row)
        data1 = str(row)[1:-1]
        tree.insert( "",i, values=data1)
 
    # Pack the Treeview in the new window
    tree.pack(expand=True, fill="both")

# Create the main Tkinter window
root = tk.Tk()
root.title("Main Window")

# Button to show the join table data in a new window
show_button = tk.Button(root, text="Show Join Table Data", command=show_join_table)
show_button.pack()

# Run the Tkinter main loop
root.mainloop()

# Close the database connection when the GUI is closed
connection.close()
