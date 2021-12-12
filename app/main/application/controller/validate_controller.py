from flask import request
from flask_restful import reqparse, Resource


from .._base import BaseResource
from ...repository import *
from ...repository.interface import *
from app.main.application.api_model import *


class ValidateController(BaseResource):
    """Validate Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("StartYear", type = int, required = False)
        self.req_parser.add_argument("EndYear", type = int, required = False)
        self.req_parser.add_argument("Marks", type = int, required = False)
        self.req_parser.add_argument("Percentage", type = float, required = False)
        self.req_parser.add_argument("Email", type = str, required = False)
        self.req_parser.add_argument("MobileNumber", type = str, required = False)
        self.req_parser.add_argument("Username", type = str, required = False)
        self.req_parser.add_argument("InstituteName", type = str, required = False)
        self.req_parser.add_argument("InstituteID", type = str, required = False)
        self.req_parser.add_argument("QualificationName", type = str, required = False)
        self.req_parser.add_argument("QualificationID", type = str, required = False)
        self.req_parser.add_argument("SpecializationName", type = str, required = False)
        self.req_parser.add_argument("BoardName", type = str, required = False)
        self.req_parser.add_argument("Class10", type = bool, required = False)




    def get(self):
        if request.endpoint=="start_year":
            try:
                if self.args["StartYear"]:
                    return self.formatter.get(validate_start_year(self.args["StartYear"]), None, 200,"Start Year validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        elif request.endpoint=="end_year":
            try:
                if self.args["StartYear"]and self.args["EndYear"]:
                    return self.formatter.get(validate_end_year(self.args["StartYear"],self.args["EndYear"]), None, 200,"End Year validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        elif request.endpoint=="marks":
            try:
                if self.args["Marks"]:
                    return self.formatter.get(validate_marks(self.args["Marks"]), None, 200,"Marks validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        elif request.endpoint=="percent":
            try:
                if self.args["Percentage"]:
                    return self.formatter.get(validate_percent(self.args["Percentage"]), None, 200,"Percentage validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        
        elif request.endpoint=="email":
            try:
                if self.args["Email"]:
                    return self.formatter.get(validate_email(self.args["Email"]), None, 200,"Email validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        elif request.endpoint=="mob":
            try:
                if self.args["MobileNumber"]:
                    return self.formatter.get(validate_mob(self.args["MobileNumber"]), None, 200,"Mobile Number validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        elif request.endpoint=="username":
            try:
                if self.args["Username"]:
                    return self.formatter.get(validate_username(self.args["Username"]), None, 200,"Username validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        #master validation
        
        elif request.endpoint=="institute":
            try:
                if self.args["InstituteName"]:
                    return self.formatter.get(validate_institute(self.args["InstituteName"]), None, 200,"Institute validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

        
        elif request.endpoint=="qualification":
            try:
                if self.args["QualificationName"] and self.args["InstituteID"]:
                    return self.formatter.get(validate_qualification(self.args["QualificationName"],self.args["InstituteID"]), None, 200,"Qualification validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))


        elif request.endpoint=="specialization":
            try:
                if self.args["SpecializationName"] and self.args["QualificationID"]:
                    return self.formatter.get(validate_specialization(self.args["SpecializationName"],self.args["QualificationID"]), None, 200,"Specialization validated successfully" )
                    
            except ValueError as err:
                return self.formatter.get([], str(ValueError), 403, str(err))

