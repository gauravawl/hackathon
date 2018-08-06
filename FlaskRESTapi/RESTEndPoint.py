from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

SERVER_NAME = "127.0.0.2"
users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occuptaion": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 35,
        "occuptaion": "Doctor"
    }
]


class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        for user in users:
            if name == user["name"]:
                return "User with name {} already exists".format(name), 400
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        for user in users:
            if name == user["name"]:
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted".format(name), 200


api.add_resource(User, "/user/<string:name>")
app.run(host='0.0.0.0', debug=True)
