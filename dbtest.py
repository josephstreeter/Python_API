import sqlite3

class user:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.displayname = lastname + ", " + firstname
        self.userid = firstname[0:1] + lastname

    def create(self):
        conn = sqlite3.connect('idm.db')
        conn.execute('INSERT INTO users (firstname,lastname,displayname,userid) \
        VALUES (" + self.firstname + "," + self.lastname + "," + self.displayname + "," + self.userid +");')

    def get(self, userid):
        conn = sqlite3.connect('idm.db')
        results = conn.execute('SELECT * FROM users WHERE userid = "+ userid +";')
        return results
    

x = user("Joseph","Streeter")
#x.create()
cursor=x.get("JStreeter")
for i in cursor:
	print("UserID", i[0])