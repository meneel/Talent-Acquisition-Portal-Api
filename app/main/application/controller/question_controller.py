# -*- encoding: utf-8 -*-

from flask import request
from .._base import BaseResource
from ...repository import *
from ...repository.interface import *


class Level1Controller(BaseResource):
    """Level 1 Controller"""
    
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("SubjectID", type = str, required = False)
        self.req_parser.add_argument("SelectedAnswer", type = str, required = False)
        self.req_parser.add_argument("L1QuestionID", type = str, required = False)
        self.req_parser.add_argument("Marks", type = str, required = False)
        self.req_parser.add_argument("Question", type = str, required = False)
        self.req_parser.add_argument("WrongOptions", type = str, required = False)
        self.req_parser.add_argument("CorrectOption", type = str, required = False)
        self.req_parser.add_argument("Time", type = str, required = False)

        self.level1_question_repository= Level1QuesionRepository()

    def get(self):
        if request.endpoint=="question":
            try:
                if self.args["SubjectID"]:
                    return self.formatter.get(self.level1_question_repository.get_by_SubjectID(self.args["SubjectID"]), None, 200, None)

                elif self.args["L1QuestionID"]:
                    return self.formatter.get(self.level1_question_repository.get_by_L1QuestionID(self.args["L1QuestionID"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.level1_question_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        

    def post(self):
        if request.endpoint=="post_question":
            try:
                if self.args["SubjectID"] :
                    return self.formatter.post(self.level1_question_repository.create_question(self.args), err=None, code=200, msg="Successfully Posted Level 1 Question")
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="check_answer":
            # try:
                args = request.get_json()
                output = {k : [] for k in [ "UUID", "SubjectID" , "L1QuestionID", "SelectedAnswer"]}
                for i in args:
                    for key in output.keys():
                        output[key].append(i.get(key, None))
                return self.formatter.post(self.level1_question_repository.Check_answer(output), err=None, code=200, msg=None)

            # except AttributeError as err:
            #     return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            # except ValueError as err:
            #     return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            # except Exception as err:
            #     return self.formatter.post([], err, "Please pass correct values") 

        elif request.endpoint=="api4":
            args = request.get_json()
            output = {k : [] for k in ["SubjectID","UUID"]}
            
            for i in args:
                for key in output.keys():
                    output[key].append(i.get(key, None))

            return self.formatter.get(self.level1_question_repository.get_question_sub(output), None, 200, None)
 


    def delete(self):
        try:
            if self.args["L1QuestionID"]:
                return self.formatter.post(self.level1_question_repository.delete_questions(self.args), err=None, code=200, msg="Successfully Deleted Question")
            else:
                raise AttributeError

        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")


class Level2Controller(BaseResource):
    """Level 2 Controller"""
    
    def __init__(self, **kwargs):
        super().__init__()

        self.req_parser.add_argument("SubjectID", type = str, required = False)
        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("SelectedAnswer", type = str, required = False)
        self.req_parser.add_argument("L2QuestionID", type = str, required = False)
        self.req_parser.add_argument("Marks", type = str, required = False)
        self.req_parser.add_argument("Question", type = str, required = False)
        self.req_parser.add_argument("Instruction", type = str, required = False)
        self.req_parser.add_argument("FileUpload", type = str, required = False)
        self.req_parser.add_argument("Image", type = str, required = False)
        self.req_parser.add_argument("Time", type = str, required = False)

        self.level2_question_repository= Level2QuesionRepository()

    def get(self):
        if request.endpoint=="question2":
            try:
                if self.args["SubjectID"]:
                    return self.formatter.get(self.level2_question_repository.get_by_SubjectID(self.args["SubjectID"]), None, 200, None)

                elif self.args["L2QuestionID"]:
                    return self.formatter.get(self.level2_question_repository.get_by_L1QuestionID(self.args["L1QuestionID"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.level2_question_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err=err, msg="Please pass correct values")


    def post(self):
        if request.endpoint=="post_question2":
            try:
                if self.args["SubjectID"] :
                    return self.formatter.post(self.level2_question_repository.create_question(self.args), err=None, code=200, msg="Successfully Posted Level 2 Question")
                else:
                    raise AttributeError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="check_answer2":
            try:
                
                return self.formatter.post(self.level2_question_repository.check_answer(self.args), err=None, code=200, msg=None)

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        
        elif request.endpoint=="api5":

            return self.formatter.get(self.level2_question_repository.get_question_sub(self.args), None, 200, None)



    def delete(self):
        try:
            if self.args["L2QuestionID"]:
                return self.formatter.post(self.level2_question_repository.delete_questions(self.args), err=None, code=200, msg="Successfully Deleted Question")
            else:
                raise AttributeError

        except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")
