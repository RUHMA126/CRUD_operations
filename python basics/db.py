import pyodbc 
conn = pyodbc.connect("Driver={SQL Server};"
                        "Server=DESKTOP-QUL15MQ;"
                        "Database=master;"
                        'Trusted_conn=yes;')

cursor = conn.cursor()

sql_query = '''SELECT orders.order_number ,  product.name , order_detail.quantity ,orders.total_amount , product.price
FROM order_detail 
INNER JOIN orders
ON order_detail.order_detail_id = orders.order_id
join product
on product.id = order_detail.order_detail_id
'''
# Execute a SELECT query
cursor.execute(sql_query)

# Fetch all the data
rows = cursor.fetchall()

# Process the data as needed
for row in rows:
    print(row)

# Close the conn
conn.close()
# cursor = conn.cursor()
# cursor.execute(''' create table category (
#                 id int primary key  identity ,
#                 name varchar(20)
# ) ''') 
# conn.commit()

# cursor = conn.cursor()
# cursor.execute('''create table product(
#                 id int primary key identity, 
#                 name varchar(20) ,
#                 type varchar(20) , 
#                 c_id int foreign key references category(id)
             
#  )  ''') 
# conn.commit()

# cursor = conn.cursor()
# cursor.execute('''
#                 INSERT INTO category ( name )
#                 VALUES
#                   ('clothing') ,
#                 ('cosmetics') , 
#                 ('shoes')
#                 ''')
# conn.commit()



# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE employees (
#                 id INT PRIMARY KEY,
#                 name VARCHAR(50),
#                 department VARCHAR(50)
#           ) ''')
# conn.commit()

# cursor = conn.cursor()
# cursor.execute('''
#               INSERT INTO employees (id, name, department)
#                 VALUES (1, 'John Doe', 'IT'),
#                 (2, 'Jane Smith', 'Sales'),
#                 (3, 'Mike Johnson', 'HR');
#                 ''')
# conn.commit()

# cursor = conn.cursor()
# cursor.execute('''create table departments(
#                 id int primary key identity ,
#                 department_name varchar(20) , 
#                 e_id int foreign key references employees(id)
# )  ''') 
# conn.commit()


# cursor = conn.cursor()
# cursor.execute('''
#               INSERT INTO departments (department_name)
#                 VALUES ( 'IT'  ),
#                 ( 'Sales'  ),
#                 ( 'HR')
#                 ''')
# conn.commit()










