# -*- encoding: utf-8 -*-

from flask import request
from flask_restful import reqparse, Resource


from .._base import BaseResource
from ...repository.interface import *
from ...repository import *
from app.main.application.api_model import *


class PersonalDetailsController(BaseResource):
    """Personal Details Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("email", type = str, required = False)
        self.req_parser.add_argument("username", type = str, required = False)
        self.req_parser.add_argument("MobileNumber", type = str, required = False)
        self.req_parser.add_argument("CountryCode", type = str, required = False)
        self.req_parser.add_argument("FirstName", type = str, required = False)
        self.req_parser.add_argument("LastName", type = str, required = False)
        self.req_parser.add_argument("PC_Batch", type = int, required = False)
        self.req_parser.add_argument("PrimaryCollegeID", type = int, required = False)
        self.req_parser.add_argument("PC_Registration", type = int, required = False)
        self.req_parser.add_argument("PC_CourseID", type = int, required = False)
        self.req_parser.add_argument("password", type = str, required = False)
        self.req_parser.add_argument("ImageLocation", type = str, required = False)
        self.req_parser.add_argument("Address", type = str, required = False)
        self.req_parser.add_argument("CityName", type = str, required = False)
        self.req_parser.add_argument("StateID", type = str, required = False)
        self.req_parser.add_argument("Pincode", type = int, required = False)
        self.req_parser.add_argument("token", type = str, required = False)

        # repository controller objects
        self.personal_details_repository = PersonalDetailsRepository()


    def get(self):
        if request.endpoint=="user":
            try:
                if self.args["UUID"]:
                    return self.formatter.get(self.personal_details_repository.get_by_id(self.args["UUID"]), None, 200, None)

                elif self.args["email"]:
                    return self.formatter.get(self.personal_details_repository.get_by_email(self.args["email"]), None, 200, None)

                elif self.args["username"]:
                    return self.formatter.get(self.personal_details_repository.get_by_username(self.args["username"]), None, 200, None)

                elif self.args["MobileNumber"]:
                    return self.formatter.get(self.personal_details_repository.get_by_mob(self.args["MobileNumber"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.personal_details_repository.get_all(), None, 200, None)
                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint=="dashboard":
            if self.args["UUID"]:
                    return self.formatter.get(self.personal_details_repository.get_for_dashboard(self.args["UUID"]), None, 200, None)

    def post(self):
        if request.endpoint=="post_user":
            try:
                if validate_email(self.args["email"])==True:
                    if validate_mob(self.args["MobileNumber"])==True:
                        if validate_username(self.args["username"])==True:
                            return self.formatter.post(self.personal_details_repository.create_user(self.args), err=None, code=200, msg="Successfully Posted User")
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="update_user":
            try:
                return self.formatter.post(self.personal_details_repository.update_user(self.args), err=None, code=200, msg="Successfully Updated User")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

    def delete(self):
        try:
            return self.formatter.post(self.personal_details_repository.delete_user(self.args), err=None, code=200, msg="Successfully Deleted User")

        except AttributeError as err:
            return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")




class AdditionalEducationDetailsController(BaseResource):
    """Additional Education Details Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ID", type = str, required = False)
        self.req_parser.add_argument("StudyLevel", type = str, required = False)
        self.req_parser.add_argument("InstitueID", type = str, required = False)
        self.req_parser.add_argument("CourseID", type = str, required = False)
        self.req_parser.add_argument("RegistrationNumber", type = str, required = False)
        self.req_parser.add_argument("Percentage", type = float, required = False)
        self.req_parser.add_argument("StartYear", type = int, required = False)
        self.req_parser.add_argument("EndYear", type = int, required = False)

        # repository controller objects
        self.additional_education_details_repository = AdditionalEducationDetailsRepository()


    def get(self):
        try:
            if self.args["UUID"]:
                return self.formatter.get(self.additional_education_details_repository.get_by_uuid(self.args["UUID"]), None, 200, None)

            elif self.args["ID"]:
                return self.formatter.get(self.additional_education_details_repository.get_by_id(self.args["ID"]), None, 200, None)
                
            else:
                return self.formatter.get(self.additional_education_details_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")

    
    def post(self):
        if request.endpoint=="post_additional_education_details":
            try:
                return self.formatter.post(self.additional_education_details_repository.create_AEDetails(self.args), err=None, code=200, msg="Successfully Posted Additional Education Details")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")


        elif request.endpoint=="update_additional_education_details":
            try:
                return self.formatter.post(self.additional_education_details_repository.update_AEDetails(self.args), err=None, code=200, msg="Successfully Updated Additional Education Details")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")


    def delete(self):
        try:
            return self.formatter.post(self.additional_education_details_repository.delete_AEDetails(self.args), err=None, code=200, msg="Succssfully Deleted Additional Education Details")

        except AttributeError as err:
            return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")

    


class ExperienceDetailsController(BaseResource):
    """Experience Detailsr Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ID", type = str, required = False)
        self.req_parser.add_argument("Designation", type = str, required = False)
        self.req_parser.add_argument("DepartmentName", type = str, required = False)
        self.req_parser.add_argument("Organization", type = str, required = False)
        self.req_parser.add_argument("StartYear", type = int, required = False)
        self.req_parser.add_argument("EndYear", type = int, required = False)

        # repository controller objects
        self.experience_details_repository = ExperienceDetailsRepository()
        # self.output = {k : [] for k in ["UUID", "Designation","DepartmentName","Organization","StartYear","EndYear"]}
        # for i in self.args:
        #     for key in self.output.keys():
        #         self.output[key].append(i.get(key, None))

    def get(self):
        try:
            if self.args["UUID"]:
                return self.formatter.get(self.experience_details_repository.get_by_uuid(self.args["UUID"]), None, 200, None)

            elif self.args["ID"]:
                return self.formatter.get(self.experience_details_repository.get_by_id(self.args["ID"]), None, 200, None)
                
            else:
                return self.formatter.get(self.experience_details_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")

    def post(self):
        if request.endpoint=="post_experience_details":
            args = request.get_json()
            output = {k : [] for k in ["Designation","UUID","DepartmentName","Organization","StartYear","EndYear"]}
            
            for i in args:
                for key in output.keys():
                    output[key].append(i.get(key, None))
            try:
                return self.formatter.post(self.experience_details_repository.create_ExpDetails(output), err=None, code=200, msg="Successfully Posted Experience Details")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

        elif request.endpoint=="update_experience_details":
            try:
                return self.formatter.post(self.experience_details_repository.update_ExpDetails(self.args), err=None, code=200, msg="Successfully Updated Experience Details")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

    def delete(self):
        try:
            return self.formatter.post(self.experience_details_repository.delete_ExpDetails(self.args), err=None, code=200, msg="Successfully Deleted Experience Details")

        except AttributeError as err:
            return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")


class AdditionalInformationController(BaseResource):
    """Additional Information Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ID", type = str, required = False)
        self.req_parser.add_argument("ResumeCopyLocation", type = str, required = False)
        self.req_parser.add_argument("Skills", type = str, required = False)
        self.req_parser.add_argument("ECActivities", type = str, required = False)
        self.req_parser.add_argument("ProjectLinks", type = str, required = False)

        # repository controller objects
        self.additional_information_repository = AdditionalInformationRepository()

    def get(self):
        try:
            if self.args["UUID"]:
                return self.formatter.get(self.additional_information_repository.get_by_uuid(self.args["UUID"]), None, 200, None)

            elif self.args["ID"]:
                return self.formatter.get(self.additional_information_repository.get_by_id(self.args["ID"]), None, 200, None)
                
            else:
                return self.formatter.get(self.additional_information_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")


    def post(self):
        if request.endpoint=="post_additional_information":
            try:
                return self.formatter.post(self.additional_information_repository.create_AdInfo(self.args), err=None, code=200, msg="Successfully Posted Additional Information")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")


        elif request.endpoint=="update_additional_information":
            try:
                return self.formatter.post(self.additional_information_repository.update_AdInfo(self.args), err=None, code=200, msg="Successfully Updated Additional Information")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")


    def delete(self):
        try:
            return self.formatter.post(self.additional_information_repository.delete_AdInfo(self.args), err=None, code=200, msg="Successfully Deleted Additional Information")

        except AttributeError as err:
            return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")


class ProjectReviewStatusController(BaseResource):
    """Project Review Status Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ExamID", type = int, required = False)
        self.req_parser.add_argument("SubjectID", type = int, required = False)
        self.req_parser.add_argument("ID", type = str, required = False)
        self.req_parser.add_argument("rev_id", type = str, required = False)

        # repository controller objects
        self.project_review_status_repository = ProjectReviewStatusRepository()

    def get(self):
        try:
            if self.args["ExamID"] and self.args["UUID"] :
                return self.formatter.get(self.project_review_status_repository.get_by_ExamID(self.args["ExamID"],self.args["UUID"]), None, 200, None)
            
            elif self.args["UUID"]:
                return self.formatter.get(self.project_review_status_repository.get_with_question(self.args["UUID"]), None, 200, None)

            elif self.args["ID"]:
                return self.formatter.get(self.project_review_status_repository.get_by_id(self.args["ID"]), None, 200, None)

            elif self.args["rev_id"] and self.args["SubjectID"]:
                return self.formatter.get(self.project_review_status_repository.get_with_details(self.args["rev_id"],self.args["SubjectID"]), None, 200, None)
                
            else:
                return self.formatter.get(self.project_review_status_repository.get_all(), None, 200, None)
                
        except AttributeError as err:
            return self.formatter.get([], err, 204, "Value is Not Present")

            


class ReviewerProfileController(BaseResource):
    """Reviewer Profile Controller"""

    def __init__(self):
        super().__init__()

        self.req_parser.add_argument("UUID", type = str, required = False)
        self.req_parser.add_argument("ID", type = str, required = False)
        self.req_parser.add_argument("AssignedSubject", type = str, required = False)

        # repository controller objects
        self.reviewer_profile_repository = ReviewerProfileRepository()

    def get(self):
        if request.endpoint=="reviewer":
            try:
                if self.args["UUID"]:
                    return self.formatter.get(self.reviewer_profile_repository.subject_with_name(self.args["UUID"]), None, 200, None)

                elif self.args["ID"]:
                    return self.formatter.get(self.reviewer_profile_repository.get_by_id(self.args["ID"]), None, 200, None)

                elif self.args["AssignedSubject"]:
                    return self.formatter.get(self.reviewer_profile_repository.get_by_assigned_subject(self.args["AssignedSubject"]), None, 200, None)
                    
                else:
                    return self.formatter.get(self.reviewer_profile_repository.get_all(), None, 200, None)

                    
            except AttributeError as err:
                return self.formatter.get([], err, 204, "Value is Not Present")

        elif request.endpoint=="reviewer_dashboard":
            if self.args["UUID"]:
                    return self.formatter.get(self.reviewer_profile_repository.get_for_dashboard(self.args["UUID"]), None, 200, None)

    def post(self):
        if request.endpoint=="post_reviewer_profile":
            try:
                return self.formatter.post(self.reviewer_profile_repository.create_revprofile(self.args), err=None, code=200, msg="Successfully Posted Reviewer Profile")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")


        elif request.endpoint=="update_reviewer_profile":
            try:
                return self.formatter.post(self.reviewer_profile_repository.update_revprofile(self.args), err=None, code=200, msg="Successfully Updated Reviewer Profile")

            except AttributeError as err:
                return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

            except ValueError as err:
                return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

            except Exception as err:
                return self.formatter.post([], err=err, msg="Please pass correct values")

    def delete(self):
        try:
            return self.formatter.post(self.reviewer_profile_repository.delete_revprofile(self.args), err=None, code=200, msg="Successfully Deleted Reviewer Profile")

        except AttributeError as err:
            return self.formatter.post([], err=repr(err),code=204, msg="Please pass correct values")

        except ValueError as err:
            return self.formatter.post([], err=repr(err),code=409, msg="Duplicate value found")

        except Exception as err:
            return self.formatter.post([], err=err, msg="Please pass correct values")

