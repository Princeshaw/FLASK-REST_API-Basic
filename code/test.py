import sqlite3 

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id int,username text,password text)"
cursor.execute(create_table)
user = (1,'jose','asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)
users = [
    (2,'rolf','asdf'),
    (3,'anne','xyz')
]
cursor.executemany(insert_query,users)
select_query = "select * from users"
for row in cursor.execute(select_query):
    print(row)
create_item_table = "CREATE TABLE IF NOT EXISTS items (name text,price real)"
cursor.execute(create_item_table)
item = ('Rice',17)
insert_item_query = "INSERT INTO items VALUES(?,?)"
cursor.execute(insert_item_query,item)

select_item_query = "select * from items"
for row in cursor.execute(select_item_query):
    print(row)
connection.commit()
connection.close()