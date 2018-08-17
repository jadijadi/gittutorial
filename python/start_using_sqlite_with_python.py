import sqlite3

conn = sqlite3.connect('database_name.db') # connect to the database or create it if it doesn't exist before

c = conn.cursor() # use this cursor object to run sql commands
c.execute('''create table table_name (col_1_name int, col_2_name int)''') # create a table with two columns

c.execute('''insert into table_name values (1, 1)''') # insert two records to that table
c.execute('''insert into table_name values (2, 2)''')

conn.commit() # commit changes

conn.close()
