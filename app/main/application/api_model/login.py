# -*- encoding: utf-8 -*-
import jwt
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from ... import db
from app.main.config import *
from .._base import BaseResource
from app.main.repository.interface.user_tbls import PersonalDetailsRepository


class LoginApi(BaseResource,PersonalDetailsRepository):
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("email", type = str, required = False)
        self.req_parser.add_argument("password", type = str, required = False)
        self.req_parser.add_argument("username", type = str, required = False)

    def post(self, **kwargs):
        if self.args["username"]:
            user = self.get_by_email(self.args["username"])
            user1 = self.get_by_username(self.args["username"])
            db.session.close()
            db.engine.dispose()
            if  user:
                password = [row["password"] for row in user]
                user_id = [row["UUID"] for row in user]
                role = [row["UserRole"] for row in user]
                if check_password_hash(password[0], self.args["password"]):
                    token = jwt.encode({
                        'UUID': user_id,
                        'exp' : datetime.utcnow() + timedelta(minutes = 30),
                        'UserRole': role,
                    },key, algorithm="HS256")
            
                    return self.formatter.get(data={"token": token})
        # returns 403 if password is wrong
            elif user1:
                password = [row["password"] for row in user1]
                user_id = [row["UUID"] for row in user1]
                role = [row["UserRole"] for row in user1]
                if check_password_hash(password[0], self.args["password"]):
                    token = jwt.encode({
                        'UUID': user_id,
                        'exp' : datetime.utcnow() + timedelta(minutes = 30),
                        'UserRole': role,
                    },key, algorithm="HS256")
            
                    return self.formatter.get(data={"token": token})
                else:
                    return self.formatter.get(err=True, code=401, msg="Could not verify your password")
            else:
                return self.formatter.get(err=True, code=401, msg="Please pass valid username or email")

        else:
            return self.formatter.get(err=True, code=401, msg="Please pass username or email")   