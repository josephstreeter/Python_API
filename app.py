import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class user:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.displayname = lastname + ", " + firstname
        self.userid = firstname[0:1] + lastname


@app.route('/api/v1/users', methods=['GET'])
def new_user():
    newuser = user(request.args['firstname'],request.args['lastname'])
    
    results={
        "firstname" : newuser.firstname,
        "lastname" : newuser.lastname,
        "displayname" : newuser.displayname,
        "userid" : newuser.userid
        }

    return jsonify(results)

app.run()
