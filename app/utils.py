# -*- encoding: utf-8 -*-

import jwt
import time

from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash
from app.main.config import *
from app.main.models.master_db import *
from app.main.models.user_db import PersonalDetails


def token_required(f):
        @wraps(f)
        def decorated(self, para, *args):
            # args = self.req_parser.parse_args()
            # token = None
            # jwt is passed in the request header
            if para.token:
                try:
                    data = jwt.decode(para.token, key, algorithms="HS256")
                    current_user = PersonalDetails.query.filter_by(UUID = data['user_id']).first()
                except jwt.ExpiredSignatureError:
                    msg = 'Signature has expired.'
                    return {"status" : "failed","error_message": msg ,"remarks" : msg}
                except jwt.DecodeError:
                    msg = 'Error decoding signature.'
                    return {"status" : "failed","error_message": msg ,"remarks" : msg}
                except jwt.InvalidTokenError:
                    msg = 'token is invalid'
                    return {"status" : "failed","error_message": msg ,"remarks" : msg}

                return  f(self, para)
            else:
                return {"status" : "failed","error_message": "Token is invalid" ,"remarks" : "pass the token"}

        return decorated


def admin_required(f):
    @wraps(f)
    def decorated(self, para, *args):
        if para.user_id:
            data= PersonalDetails.query.filter_by(UUID=para.user_id).first()
            if data.role!="Admin":
                return {"status" : "Unauthorized","error_message": "Unauthorized","remarks" : "Unauthorized"}
            return f(self,para)
        else:
            return {"status" : "failed","error_message": "user_id invalid","remarks" : "pass the user_id"}

    return decorated


def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')


def check_password(self, password):
    return check_password_hash(self.password, password)


class ResponseFormatter(object):
    """Format any CRUD Operation to a Standard API Response"""

    def get_small_message(self, code : str) -> int:
        """Define Status Codes for API Response"""

        return {
            200 : "OK",
            201 : "Created",
            204 : "No Content",
            400 : "Bad Request",
            401 : "Unauthorized",
            403 : "Forbidden",
            404 : "Not Found",
            409 : "Conflict Found",
            500 : "Internal Server Error",
            502 : "Bad Gateway"
        }.get(code, 502) # 502 > Bad Gateway


    def get(self, data : list=None, err : str = None, code : int=502, msg : str=None) -> dict:
        """Format O/P of all GET Response"""

        return {
            "status" : {
                "code"    : code, # https://www.restapitutorial.com/httpstatuscodes.html
                "refer"   : self.get_small_message(code), # reference TAG (derived from code)
                "error"   : str(err) if err else err, # this error to be logged, for DevOps
                "message" : msg # Long Message Description - for UI/UX
            },

            "data" : data,
            "time" : time.ctime()
        }

    def post(self, data : list=None, err : str = None, code : int=502, msg : str=None) -> dict:
        """Format O/P of all POST Response"""

        return {
            "status" : {
                "code"    : code, # https://www.restapitutorial.com/httpstatuscodes.html
                "refer"   : self.get_small_message(code), # reference TAG (derived from code)
                "error"   : str(err) if err else err, # this error to be logged, for DevOps
                "message" : msg # Long Message Description - for UI/UX
            },
            "time" : time.ctime()
        }
