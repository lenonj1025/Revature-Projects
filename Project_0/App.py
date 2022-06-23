from flask import Flask, request

app = Flask(__name__)

users = {}

@app.route('/test')
def hello():
    print("Hi, the hello() function is being executed")
    return "Hello World"


@app.route('/users')
def get_all_users():
    bank_users = []
    if users:
        for key in users:
            user = {
                "username": key
            }
            bank_users.append(user)
        return {
            "users": bank_users
        }, 200

    else:
        return "There are no users for this bank currently"

@app.route('/users', methods=['POST'])
def create_user():

    data = request.get_json()

    if data["username"] in users:
        return {
                   "message": f"Username {data['username']} already exists"
               }, 400
    else:
        return {
                   "username": data['username']
               }, 201


app.run(port=8080)
