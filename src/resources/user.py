import sqlite3
from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field can not be blank'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field can not be blank'
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400
        
        user = User(**data)
        user.save()

        return {'message': 'usern created successfully.'}, 201
