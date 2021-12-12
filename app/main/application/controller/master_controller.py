# -*- encoding: utf-8 -*-

from flask import request
from .._base import BaseResource
from ...repository import *
from ...repository.interface import *
from app.main.application.api_model import *


class StateMasterController(BaseResource):
    """State Master Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("StateID", type = str, required = False)
        self.req_parser.add_argument("StateAbbreviation", type = str, required = False)
        self.req_parser.add_argument("StateName", type = str, required = False)
        self.req_parser.add_argument("AltTag", type = str, required = False)

        # repository controller objects
        self.state_master_repository = StateMasterRepository()


    def get(self):
        try:
            if self.args["StateID"]:
                return self.formatter.get(self.state_master_repository.get_by_id(self.args["StateID"]), None, 200, None)

            elif self.args["StateName"]:
                return self.formatter.get(self.state_master_repository.get_by_name(self.args["StateName"]), None, 200, None)

            elif self.args["StateAbbreviation"]:
                return self.formatter.get(self.state_master_repository.get_by_abbrv(self.args["StateAbbreviation"]), None, 200, None)
                
            else:
                return self.formatter.get(self.state_master_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")



class InstituteMasterController(BaseResource):
    """Institute Master Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("StateID", type = str, required = False)
        self.req_parser.add_argument("InstituteID", type = str, required = False)
        self.req_parser.add_argument("InstituteName", type = str, required = False)
        
        # repository controller objects
        self.institute_master_repository = InstituteMasterRepository()


    def get(self):
        if request.endpoint == "master":
            try:
                if self.args["InstituteID"]:
                    return self.formatter.get(self.institute_master_repository.get_by_id(self.args["InstituteID"]), None, 200, None)
                elif self.args["InstituteName"]:
                    return self.formatter.get(self.institute_master_repository.get_by_name(self.args["InstituteName"]), None, 200, None)

                elif self.args["StateID"]:
                    return self.formatter.get(self.institute_master_repository.get_by_state_id(self.args["StateID"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.institute_master_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint == "api":
            return self.formatter.get(self.institute_master_repository.get_institute_with_state(), None, 200, None)

    def post(self):
        if request.endpoint=="post_institute":
            try:
                if self.args["InstituteName"] and self.args["StateID"]:
                    if validate_institute(self.args["InstituteName"])==True:
                        return self.formatter.post(self.institute_master_repository.create_institute(self.args), err=None, code=200, msg="Successfully Posted Institute")
                    else:
                        raise ValueError
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")


        elif request.endpoint=="update_institute":
            try:
                if self.args["InstituteName"] and self.args["InstituteID"]:
                    if validate_institute_by_id(self.args["InstituteName"],self.args["InstituteID"])==True:
                        return self.formatter.post(self.institute_master_repository.update_institute(self.args), err=None, code=200, msg="Successfully Updated Institute")
                    else:
                        raise ValueError
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

    def delete(self):
        try:
            if self.args["InstituteID"]:
                return self.formatter.post(self.institute_master_repository.delete_institute(self.args), err=None, code=200, msg="Successfully Deleted Institute")
            else:
                raise AttributeError

        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Foreign key constraint")



class QualificationMasterController(BaseResource):
    """Qualification Master Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("InstituteID", type = str, required = False)
        self.req_parser.add_argument("QualificationID", type = str, required = False)
        self.req_parser.add_argument("QualificationName", type = str, required = False)

        # repository controller objects
        self.qualification_master_repository = QualificationMasterRepository()


    def get(self):
        if request.endpoint == "master1":
            try:
                if self.args["QualificationID"]:
                    return self.formatter.get(self.qualification_master_repository.get_by_id(self.args["QualificationID"]), None, 200, None)
                elif self.args["QualificationName"]:
                    return self.formatter.get(self.qualification_master_repository.get_by_name(self.args["QualificationName"]), None, 200, None)

                elif self.args["InstituteID"]:
                    return self.formatter.get(self.qualification_master_repository.get_by_institute_id(self.args["InstituteID"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.qualification_master_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint == "api1":
            return self.formatter.get(self.qualification_master_repository.get_qualification_with_institute(), None, 200, None)


    def post(self):
        if request.endpoint=="post_qualification":
            try:
                if self.args["QualificationName"] and self.args["InstituteID"]:
                    if validate_qualification(self.args["QualificationName"],self.args["InstituteID"])==True:
                        return self.formatter.post(self.qualification_master_repository.create_qualification(self.args) , err=None, code=200, msg="Successfully Posted Qualification")
                    else:
                        raise ValueError
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        
        elif request.endpoint=="update_qualification":
            try:
                if self.args["QualificationName"] and self.args["QualificationID"]:
                    if validate_qualification_by_id(self.args["QualificationName"],self.args["QualificationID"])==True:
                        return self.formatter.post(self.qualification_master_repository.update_qualification(self.args), err=None, code=200, msg="Successfullt Updated Qualification")
                    else:
                        raise ValueError
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

    def delete(self):
        try:
            if self.args["QualificationID"]:
                return self.formatter.post(self.qualification_master_repository.delete_qualification(self.args), err=None, code=200, msg="Successfully Deleted Qualification")
            else:
                raise AttributeError
        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
                return self.formatter.post([], err=err, msg="Foreign key constraint")



class SpecializationMasterController(BaseResource):
    """Specialization Master Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("QualificationID", type = str, required = False)
        self.req_parser.add_argument("SpecializationID", type = str, required = False)
        self.req_parser.add_argument("SpecializationName", type = str, required = False)

        # repository controller objects
        self.specialization_master_repository = SpecializationMasterRepository()


    def get(self):
        if request.endpoint == "master2":
            try:
                if self.args["SpecializationID"]:
                    return self.formatter.get(self.specialization_master_repository.get_by_id(self.args["SpecializationID"]), None, 200, None)
                elif self.args["SpecializationName"]:
                    return self.formatter.get(self.specialization_master_repository.get_by_name(self.args["SpecializationName"]), None, 200, None)

                elif self.args["QualificationID"]:
                    return self.formatter.get(self.specialization_master_repository.get_by_qualification_id(self.args["QualificationID"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.specialization_master_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint == "api2":
            return self.formatter.get(self.specialization_master_repository.get_specialization_with_qualification(), None, 200, None)

    def post(self):
        if request.endpoint=="post_specialization":
            try:
                if self.args["SpecializationName"] and self.args["QualificationID"]:
                    if validate_specialization(self.args["SpecializationName"],self.args["QualificationID"])==True:                    
                        return self.formatter.post(self.specialization_master_repository.create_specialization(self.args), err=None, code=200, msg="Successfully Posted Specialization")
                    else:
                        raise ValueError
                else:
                    raise AttributeError
            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="update_specialization":
            try:
                if self.args["SpecializationName"] and self.args["SpecializationID"]:
                    if validate_specialization_by_id(self.args["SpecializationName"],self.args["SpecializationID"])==True:   
                        return self.formatter.post(self.specialization_master_repository.update_specialization(self.args), err=None, code=200, msg="Successfully Updated Specialization")
                    else:
                        raise ValueError
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

    def delete(self):
        try:
            if self.args["SpecializationID"]:
                return self.formatter.post(self.specialization_master_repository.delete_specialization(self.args), err=None, code=200, msg="Successfully Deleted Specialization")
            else:
                raise AttributeError

        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
                return self.formatter.post([], err=err, msg="Foreign key constraint")



class BoardMasterController(BaseResource):
    """Board Master Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("BoardID", type = str, required = False)
        self.req_parser.add_argument("BoardName", type = str, required = False)
        self.req_parser.add_argument("Class10", type = bool, required = False)

        # repository controller objects
        self.board_master_repository = BoardMasterRepository()



    def get(self):
        try:
            if self.args["BoardID"]:
                return self.formatter.get(self.board_master_repository.get_by_id(self.args["BoardID"]), None, 200, None)

            elif self.args["BoardName"]:
                return self.formatter.get(self.board_master_repository.get_by_name(self.args["BoardName"]), None, 200, None)

            elif self.args["Class10"]:
                return self.formatter.get(self.board_master_repository.get_by_class(self.args["Class10"]), None, 200, None)
                
            else:
                return self.formatter.get(self.board_master_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")

    def post(self):
        if request.endpoint=="post_board":
            try:
                if self.args["BoardName"] :
                    return self.formatter.post(self.board_master_repository.create_boards(self.args), err=None, code=200, msg="Successfully Posted Board")
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="update_board":
            try:
                if self.args["BoardName"] and self.args["BoardID"]:
                    return self.formatter.post(self.board_master_repository.update_board(self.args), err=None, code=200, msg="Successfully Updated Board")
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")
    def delete(self):
        try:
            if self.args["BoardID"]:
                return self.formatter.post(self.board_master_repository.delete_board(self.args), err=None, code=200, msg="Successfully Deleted Board")
            else:
                raise AttributeError

        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
                return self.formatter.post([], err=err, msg="Foreign key constraint")

class SubjectMasterController(BaseResource):
    """Subject Master Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("SubjectID", type = str, required = False)
        self.req_parser.add_argument("SubjectName", type = str, required = False)
        

        # repository controller objects
        self.subject_master_repository = SubjectMasterRepository()


    def get(self):
        try:
            if self.args["SubjectID"]:
                return self.formatter.get(self.subject_master_repository.get_by_id(self.args["SubjectID"]), None, 200, None)

            elif self.args["SubjectName"]:
                return self.formatter.get(self.subject_master_repository.get_by_name(self.args["SubjectName"]), None, 200, None)
                
            else:
                return self.formatter.get(self.subject_master_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")

    def post(self):
        if request.endpoint=="post_subject":
            try:
                if self.args["SubjectName"]:
                    return self.formatter.post(self.subject_master_repository.create_subject(self.args), err=None, code=200, msg="Successfully Posted Subject")
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                    return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="update_subject":
            try:
                if self.args["SubjectName"] and self.args["SubjectID"]:
                    return self.formatter.post(self.subject_master_repository.update_subject(self.args), err=None, code=200, msg="Successfully Updated Subject")
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")
    def delete(self):
        try:
            if self.args["SubjectID"]:
                return self.formatter.post(self.subject_master_repository.delete_subject(self.args), err=None, code=200, msg="Successfully Deleted Subject")
            else:
                raise AttributeError
        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
                return self.formatter.post([], err=err, msg="Foreign key constraint")

