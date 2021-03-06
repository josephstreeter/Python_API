import sqlite3
import json

class user:
	'''
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.displayname = lastname + ", " + firstname
		self.userid = firstname[0:1] + lastname
	'''
	@staticmethod
	def create(firstname, lastname):
		conn = sqlite3.connect('./Python_API/idm.db')
		conn.execute("INSERT INTO users (firstname,lastname,displayname,userid) \
		VALUES (?,?,?,?);",(firstname, lastname, lastname + ", " + firstname, firstname[0:1] + lastname))
		conn.commit()

	@staticmethod
	def get(username):
		conn = sqlite3.connect('./Python_API/idm.db')
		cursor = conn.cursor()
		cursor.execute('SELECT * FROM users WHERE userid LIKE ?;',(username,))
		results = cursor.fetchall()
		return results

#x = user("Joseph","Hanson")
#x.create("Joseph","Hanson")
user.create("Joe","Hanson")
i=user.get("j%")
print(json.dumps(i))