import csv
import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)
# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)


# query = "INSERT INTO sys_command VALUES (null,'obs', 'C:\\Program Files\\obs-studio\\bin\\obs64.exe')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT IN TO web_command VALUES (null,'whatsapp', 'https://web.whatsapp.com/')"
# cursor.execute(query)
# conn.commit()


# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name VARCHAR(200), Phone VARCHAR(255), email VARCHAR(255) NULL)''') 

# query = "DELETE FROM sys_command WHERE name='obs'"
# cursor.execute(query)
# conn.commit()



desired_columns_indices = [0, 18]
 
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
     csvreader = csv.reader(csvfile)
     for row in csvreader:
         selected_data = [row[i] for i in desired_columns_indices]
         cursor.execute(''' INSERT INTO contacts (id, 'name', 'Phone') VALUES (null, ?,? );''', tuple(selected_data))

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully")

