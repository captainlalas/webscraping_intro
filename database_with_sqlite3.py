import sqlite3
import pandas as pd

# This project is about creating a staff db and loading a csv file
my_con = sqlite3.connect("staff.db")
table_name = 'employees'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE', 'DEPT', 'SALARY']
# After creating the db and its attributes, let's load the csv fille
file_path = 'source/employees.csv'
df = pd.read_csv(file_path, names=attribute_list)

# Connect to the db and Create a fresh table
df.to_sql(table_name, my_con, if_exists='replace', index=False)
print('Table is ready')

# Querying the db
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, my_con)
print(query_statement)
print(query_output)

# Let's create a row and append it our employees table
data_dict = { 'ID':[100],
             'FNAME': ['John'],
             'LNAME': ['Doe'],
             'CITY':['Paris'],
             'CCODE': ['FR'],
             'DEPT': ['Accounting'],
             'SALARY': [70000]}
data_to_append = pd.DataFrame(data_dict)

data_to_append.to_sql(table_name, my_con, if_exists='append', index=False)
print('A new row inserted successfully')
my_con.close()
