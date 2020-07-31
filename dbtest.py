import sqlite3

conn = sqlite3.connect("comment_section.db")
print("DB Connection successful")
results = conn.execute('''SELECT * FROM Comments''')

for result in results:
	print ("column0=",result[0])
	print ("column1=",result[1])
	print ("column2=",result[2])
	print ("column1=",result[3])

conn.close()