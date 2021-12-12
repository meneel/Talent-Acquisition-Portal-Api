#!/bin/python
# -*- encoding: utf-8 -*-
# importing the sys module
import os
from flask_restful import Api
from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )

# setting the environment
from dotenv import load_dotenv # Python 3.6+
load_dotenv(verbose = True) # configure .env File or set Environment Variables

app = create_app(os.getenv("PROJECT_ENV_NAME") or "dev") # check config.py
# CORS(app) # enable CORS if needed
api = Api(app)

"""API Management and Server Running Module"""

from app.main.application import *  # import all controllers



### --- List of all Resources --- ###

api.add_resource(LoginApi, '/login')
api.add_resource(ForgotPasswordController, '/forgot_password')
api.add_resource(ForgotPasswordResetPasswordController, '/forgot_reset_password')
api.add_resource(ResetPasswordController, '/reset_password')
api.add_resource(StateMasterController, "/master/states")
api.add_resource(InstituteMasterController, "/master/institutes", endpoint = "master")
api.add_resource(InstituteMasterController, "/post_institute", endpoint = "post_institute")
api.add_resource(InstituteMasterController, "/update_institute", endpoint = "update_institute")
api.add_resource(QualificationMasterController, "/master1/qualification", endpoint = "master1")
api.add_resource(QualificationMasterController, "/post_qualification", endpoint = "post_qualification")
api.add_resource(QualificationMasterController, "/update_qualification", endpoint = "update_qualification")
api.add_resource(SpecializationMasterController, "/master2/specialization", endpoint = "master2")
api.add_resource(SpecializationMasterController, "/post_specialization", endpoint = "post_specialization")
api.add_resource(SpecializationMasterController, "/update_specialization", endpoint = "update_specialization")
api.add_resource(BoardMasterController, "/master/board")
api.add_resource(BoardMasterController, "/post_board",endpoint="post_board")
api.add_resource(BoardMasterController, "/update_board",endpoint="update_board")
api.add_resource(SubjectMasterController, "/master/subject")
api.add_resource(SubjectMasterController, "/post_subject", endpoint="post_subject")
api.add_resource(SubjectMasterController, "/update_subject", endpoint="update_subject")
api.add_resource(PersonalDetailsController, "/user/personal_details", endpoint="user")
api.add_resource(PersonalDetailsController, "/dashboard", endpoint="dashboard")
api.add_resource(PersonalDetailsController, "/post_user",endpoint="post_user")
api.add_resource(PersonalDetailsController, "/update_user",endpoint="update_user")
api.add_resource(AdditionalEducationDetailsController, "/user/additional_education_details")
api.add_resource(AdditionalEducationDetailsController, "/post_additional_education_details",endpoint="post_additional_education_details")
api.add_resource(AdditionalEducationDetailsController, "/update_additional_education_details",endpoint="update_additional_education_details")
api.add_resource(ExperienceDetailsController, "/user/experience_details")
api.add_resource(ExperienceDetailsController, "/post_experience_details",endpoint="post_experience_details")
api.add_resource(ExperienceDetailsController, "/update_experience_details",endpoint="update_experience_details")
api.add_resource(AdditionalInformationController, "/user/additional_information")
api.add_resource(AdditionalInformationController, "/post_additional_information",endpoint="post_additional_information")
api.add_resource(AdditionalInformationController, "/update_additional_information",endpoint="update_additional_information")
api.add_resource(ProjectReviewStatusController, "/user/project_review_status")
api.add_resource(ReviewerProfileController, "/reviewer/reviewer_profile",endpoint="reviewer")
api.add_resource(ReviewerProfileController, "/reviewer_dashboard/reviewer_profile",endpoint="reviewer_dashboard")
api.add_resource(ReviewerProfileController, "/post_reviewer_profile",endpoint="post_reviewer_profile")
api.add_resource(ReviewerProfileController, "/update_reviewer_profile",endpoint="update_reviewer_profile")
api.add_resource(Level1Controller, "/question/level1", endpoint= "question")
api.add_resource(Level1Controller, "/post_question",endpoint="post_question")
api.add_resource(Level1Controller, "/check_answer",endpoint="check_answer")
api.add_resource(Level2Controller, "/question2/level2", endpoint= "question2")
api.add_resource(Level2Controller, "/post_question2",endpoint="post_question2")
api.add_resource(Level2Controller, "/check_answer2",endpoint="check_answer2")
api.add_resource(Level1ResultController, "/result/level1",endpoint="result")
api.add_resource(Level1ResultController, "/percenresult/level1",endpoint="percenresult")
api.add_resource(ExamResultController, "/exam_result")
api.add_resource(ReviewerController, "/post_review")

# specialized controllers
api.add_resource(InstituteMasterController, "/api/institute_details", endpoint = "api")
api.add_resource(QualificationMasterController, "/api1/qualification", endpoint = "api1")
api.add_resource(SpecializationMasterController, "/api2/specialization", endpoint = "api2")
api.add_resource(Level1Controller, "/api4/level1", endpoint= "api4")
api.add_resource(Level2Controller, "/api5/level2", endpoint= "api5")
api.add_resource(Level1ResultController, "/api6/result/level1", endpoint= "api6")

# validate controllers
api.add_resource(ValidateController, "/start_year/validate", endpoint = "start_year")
api.add_resource(ValidateController, "/end_year/validate", endpoint = "end_year")
api.add_resource(ValidateController, "/marks/validate", endpoint = "marks")
api.add_resource(ValidateController, "/percent/validate", endpoint = "percent")
api.add_resource(ValidateController, "/email/validate", endpoint = "email")
api.add_resource(ValidateController, "/mob/validate", endpoint = "mob")
api.add_resource(ValidateController, "/username/validate", endpoint = "username")
api.add_resource(ValidateController, "/institute/validate", endpoint = "institute")
api.add_resource(ValidateController, "/qualification/validate", endpoint = "qualification")
api.add_resource(ValidateController, "/specialization/validate", endpoint = "specialization")


if __name__ == "__main__":
    app.run(
        port = os.getenv("port", 5000), # run the application on default 5000 Port
        # localhost is required to run the code from m/c
        # else, 0.0.0.0 can be used for docker container
        host = os.getenv("host", "0.0.0.0") # define host, as required
    )
