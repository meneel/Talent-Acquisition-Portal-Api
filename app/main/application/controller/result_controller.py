# -*- encoding: utf-8 -*-

from flask import request
from .._base import BaseResource
from ...repository import *
from ...repository.interface import *


class Level1ResultController(BaseResource):
    """Level 1 Result Controller"""
    
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ExamID", type = int, required = False)
        self.req_parser.add_argument("SubjectID", type = str, required = False)

        self.level1_result_repository= Level1ResultRepository()

    def get(self):
        if request.endpoint=="result":
            print(self.args["ExamID"])
            try:

                if self.args["ExamID"] and self.args["UUID"] :
                    return self.formatter.get(self.level1_result_repository.get_by_ExamID(self.args["ExamID"],self.args["UUID"]), None, 200, None)

                elif self.args["SubjectID"] and self.args["UUID"]:
                    return self.formatter.get(self.level1_result_repository.get_by_SubjectID(self.args["SubjectID"],self.args["UUID"]), None, 200, None)

                elif self.args["UUID"]:
                    return self.formatter.get(self.level1_result_repository.get_by_UUID(self.args["UUID"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.level1_result_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint=='api6':
            try:

                if self.args["ExamID"] and self.args["UUID"] :
                    return self.formatter.get(self.level1_result_repository.get_marks_by_ExamID(self.args), None, 200, None)

            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint=='percenresult':
            try:

                if self.args["UUID"] :
                    return self.formatter.get(self.level1_result_repository.get_percentage_by_UUID(self.args), None, 200, None)

            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")


class ExamResultController(BaseResource):
    """Exam Result Controller"""
    
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)

        self.exam_result_repository= ExamResultRepository()

    def get(self):
        try:
            if self.args["UUID"]:
                return self.formatter.get(self.exam_result_repository.get_by_UUID(self.args["UUID"]), None, 200, None)
                
            else:
                return self.formatter.get(self.exam_result_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")


class ReviewerController(BaseResource):
    """Reviewer Result Controller"""
    
    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ExamID", type = int, required = False)
        self.req_parser.add_argument("Review", type = str, required = False)
        self.req_parser.add_argument("L2Marks", type = str, required = False)

        self.reviewer_post_repository= ReviewerRepository()

    def post(self):
        # try:
            return self.formatter.post(self.reviewer_post_repository.review_post(self.args), err=None, code=200, msg="Successfully Posted Review")

        # except AttributeError as err:
        #     return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        # except ValueError as err:
        #     return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        # except Exception as err:
        #     return self.formatter.post([], err, "Please pass correct values")
