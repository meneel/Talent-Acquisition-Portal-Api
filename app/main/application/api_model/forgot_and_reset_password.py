# -*- encoding: utf-8 -*-
from werkzeug.security import generate_password_hash, check_password_hash
from ... import *
from app.main.config import *
from app.main.models import *
from .._base import BaseResource
from app.main.repository.interface.user_tbls import PersonalDetailsRepository


class ForgotPasswordController(BaseResource):
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("email", type = str, required = False)
        self.req_parser.add_argument("password", type = str, required = False)
    
    def post(self):
        url = "http://115.124.120.251:5002/" + 'Home/Sendmail?email='
        a = PersonalDetails.query.filter_by(email = self.args["email"]).first()
        if self.args["email"] == a.email:
            # expires = datetime.timedelta(hours=24)
            reset_token = a.get_reset_token()
            print(reset_token)
            try:
                send_email('Reset Your Password',
                                sender='info@inspirigenceworks.com',
                                recipients=[a.email],
                                text_body=(url + a.email + "&token=" + reset_token))

                return self.formatter.post(err=None, code=200, msg="Please Check your inbox")

            except Exception as err:
                return self.formatter.post([], err,401, "Could not send email")


class ForgotPasswordResetPasswordController(BaseResource):
    def __init__(self):
        super().__init__()
        self.req_parser.add_argument("token", type = str, required = False)
        self.req_parser.add_argument("password", type = str, required = False)
        self.req_parser.add_argument("email", type = str, required = False)

        # self.personal_details= 
    
    def post(self):
        reset_token=self.args["token"]
        password = self.args["password"]
        email=self.args["email"]

        if not reset_token or not password:
            return self.formatter.post([], True,412, "Please Pass correct Reset Token and Password")

        user = PersonalDetails.verify_reset_token(reset_token)
        current_user = PersonalDetailsRepository().get_by_id(UUID=user['UUID'])
        print(current_user)
        # if user:
        #     return redirect("post_pass", code=307)
        if current_user[0]["email"]==email:

            hashed_password = generate_password_hash(password)
            # # user.password =hashed_password
            PersonalDetails.query.filter_by(UUID = user['UUID']).update({"password":hashed_password})

            db.session.commit()

            # send_email('Password changed successfully',
            #                 sender='info@inspirigenceworks.com',
            #                 recipients=[row.email for row in user],
            #                 text_body=("Success!!"))

            # return "password has been reset succesfully"
            return self.formatter.post(err=None, code=200, msg="Password changed successfully")
        
        else:
            return self.formatter.post([], True,401, "Email does not match")


class ResetPasswordController(BaseResource):
    def __init__(self):
        super().__init__()
        self.req_parser.add_argument("token", type = str, required = False)
        self.req_parser.add_argument("password", type = str, required = False)
        self.req_parser.add_argument("old_password", type = str, required = False)

        # self.personal_details= 
    
    def post(self):
        reset_token=self.args["token"]
        password = self.args["password"]
        old_password=self.args["old_password"]

        if not reset_token or not password:
            return self.formatter.post([], True,412, "Please Pass correct Reset Token and Password")

        user = PersonalDetails.verify_reset_token(reset_token)
        current_user = PersonalDetailsRepository().get_by_id(UUID=user['UUID'])
        print(current_user)
        # if user:
        #     return redirect("post_pass", code=307)
        if check_password_hash(current_user[0]["password"],old_password ):

            hashed_password = generate_password_hash(password)
            # # user.password =hashed_password
            PersonalDetails.query.filter_by(UUID = user['UUID']).update({"password":hashed_password})

            db.session.commit()

            # send_email('Password changed successfully',
            #                 sender='info@inspirigenceworks.com',
            #                 recipients=[row.email for row in user],
            #                 text_body=("Success!!"))

            # return "password has been reset succesfully"
            return self.formatter.post(err=None, code=200, msg="Password changed successfully")
        
        else:
            return self.formatter.post([], True,401, "Old Password does not match")