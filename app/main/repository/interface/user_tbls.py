# -*- encoding: utf-8 -*-
from flask import request
from sqlalchemy import func
import uuid

from sqlalchemy.sql.expression import null
from ... import db
from ...models import *
from .master_tbls import *

class PersonalDetailsRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in PersonalDetails.query.all()]
    get_by_id    = lambda self, UUID : [row.__to_dict__() for row in PersonalDetails.query.filter_by(UUID = UUID).all()]
    get_by_email    = lambda self, email : [row.__to_dict__() for row in PersonalDetails.query.filter_by(email = email).all()]
    get_by_username    = lambda self, username : [row.__to_dict__() for row in PersonalDetails.query.filter_by(username = username).all()]
    get_by_mob    = lambda self, MobileNumber : [row.__to_dict__() for row in PersonalDetails.query.filter_by(MobileNumber = MobileNumber).all()]

    def get_for_dashboard(self,UUID):
        all_personal_details = self.get_by_id(UUID) # get information for dashboard

        self.profile_comletion=0
        everything = []
        dict={}
        for row in all_personal_details:
            def isnone(result,db):
                if result is not None:
                    self.profile_comletion +=1
                    return result.__to_dict__()
                else:
                    self.profile_comletion +=0
                    return {k : None for k in db().__get_column_names__()}

            def isnone1(result,db):
                if result is not None:
                    self.profile_comletion +=1
                    for row in result:
                        return row.__to_dict__()

                else:
                    self.profile_comletion +=0
                    return {k : None for k in db().__get_column_names__()}


            dict.update({"InstituteMaster": isnone(result=InstituteMaster.query.filter_by(InstituteID = row["PrimaryCollegeID"]).first(),db=InstituteMaster)})
            dict.update({"Clss10Board": isnone(result=BoardMaster.query.filter_by(BoardID = row["Class10BoardID"]).first(),db=BoardMaster)})
            dict.update({"Class12Board": isnone(result=BoardMaster.query.filter_by(BoardID = row["Class12BoardID"]).first(),db=BoardMaster)})
            dict.update({"ProjectReviewStatus": isnone1(result=ProjectReviewStatus.query.filter_by(UUID = row["UUID"]).all(),db=ProjectReviewStatus)})
            dict.update({"QualificationMaster": isnone(result=QualificationMaster.query.filter_by(QualificationID = row["PC_StudyLevelID"]).first(),db=QualificationMaster)})
            dict.update({"SpecializationMaster": isnone(result=SpecializationMaster.query.filter_by(SpecializationID = row["PC_CourseID"]).first(),db=SpecializationMaster)})
            dict.update({"AdditionalEducationDetails": isnone(result=AdditionalEducationDetails.query.filter_by(UUID = row["UUID"]).first(),db=AdditionalEducationDetails)})
            dict.update({"ExperienceDetails": isnone1(result=ExperienceDetails.query.filter_by(UUID = row["UUID"]).all(),db=ExperienceDetails)})
            dict.update({"AdditionalInformation": isnone1(result=AdditionalInformation.query.filter_by(UUID = row["UUID"]).all(),db=AdditionalInformation)})
            dict.update({"ExamResult": isnone1(result=ExamResult.query.filter_by(UUID = row["UUID"]).all(),db=ExamResult)})
            dict.update({"ProfileCompletion": self.profile_comletion-2})
            
            everything.append({**row, **dict})

        return everything


    def create_user(self,para):

        new_user = PersonalDetails(UUID = uuid.uuid4(), FirstName = para.FirstName, LastName = para.LastName,username = para.username, PrimaryCollegeID = para.PrimaryCollegeID, PC_Registration = para.PC_Registration, email = para.email, MobileNumber = para.MobileNumber,CountryCode= para.CountryCode, password = para.password,PC_Batch = para.PC_Batch,Address=para.Address, CityName=para.CityName, StateID=para.StateID, Pincode=para.Pincode, ImageLocation=para.ImageLocation,PC_CourseID=para.PC_CourseID)
        new_user.hash_password()

        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


    def update_user(self,para):
        json_data = request.get_json()
 
        if json_data["UUID"]:
            # del json_data['token']

            data = PersonalDetails.query.filter_by(UUID=json_data["UUID"]).update(dict(json_data))
        
            db.session.commit()
            db.session.close()
            db.engine.dispose()

        
    def delete_user(self,para):

        data = PersonalDetails.query.filter_by(username = para.username).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

        

    
class AdditionalEducationDetailsRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in AdditionalEducationDetails.query.all()]
    get_by_id      = get_by_id    = lambda self, ID : [AdditionalEducationDetails.query.filter_by(ID = ID).first().__to_dict__()]
    get_by_uuid    = lambda self, UUID : [row.__to_dict__() for row in AdditionalEducationDetails.query.filter_by(UUID = UUID).all()]

    def create_AEDetails(self,para):
        new_details = AdditionalEducationDetails(UUID=para.UUID, StudyLevel=para.StudyLevel,InstitueID=para.InstitueID,CourseID=para.CourseID,RegistrationNumber=para.RegistrationNumber,Percentage=para.Percentage,StartYear=para.StartYear,EndYear=para.EndYear)
        db.session.add(new_details)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

    def update_AEDetails(self,para):
        json_data = request.get_json()
 
        if json_data["UUID"]:
            # del json_data['token']

            data = AdditionalEducationDetails.query.filter_by(UUID=json_data["UUID"]).update(dict(json_data))
        
            db.session.commit()
            db.session.close()
            db.engine.dispose()

    def delete_AEDetails(self,para):

        data = AdditionalEducationDetails.query.filter_by(UUID = para.UUID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


class ExperienceDetailsRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in ExperienceDetails.query.all()]
    get_by_id      = get_by_id    = lambda self, ID : [ExperienceDetails.query.filter_by(ID = ID).first().__to_dict__()]
    get_by_uuid    = lambda self, UUID : [row.__to_dict__() for row in ExperienceDetails.query.filter_by(UUID = UUID).all()]


    def create_ExpDetails(self,para):
        for i in range(len(para['UUID'])):
            new_expdetails = ExperienceDetails(UUID=para["UUID"][i], Designation=para["Designation"][i],DepartmentName=para["DepartmentName"][i],Organization=para["Organization"][i],StartYear=para["StartYear"][i],EndYear=para["EndYear"][i])
            db.session.add(new_expdetails)
            db.session.commit()
            db.session.close()
            db.engine.dispose()

    def update_ExpDetails(self,para):
        json_data = request.get_json()
 
        if json_data["UUID"]:
            # del json_data['token']

            data = ExperienceDetails.query.filter_by(UUID=json_data["UUID"]).update(dict(json_data))
        
            db.session.commit()
            db.session.close()
            db.engine.dispose()

    def delete_ExpDetails(self,para):

        data = ExperienceDetails.query.filter_by(UUID = para.UUID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


class AdditionalInformationRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in AdditionalInformation.query.all()]
    get_by_id      = get_by_id    = lambda self, ID : [AdditionalInformation.query.filter_by(ID = ID).first().__to_dict__()]
    get_by_uuid    = lambda self, UUID : [row.__to_dict__() for row in AdditionalInformation.query.filter_by(UUID = UUID).all()]


    def create_AdInfo(self,para):
        new_AdInfo = AdditionalInformation(UUID=para.UUID, ResumeCopyLocation=para.ResumeCopyLocation,Skills=para.Skills,ECActivities=para.ECActivities,ProjectLinks=para.ProjectLinks)
        db.session.add(new_AdInfo)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

    def update_AdInfo(self,para):
        json_data = request.get_json()
 
        if json_data["UUID"]:
            # del json_data['token']

            data = AdditionalInformation.query.filter_by(UUID=json_data["UUID"]).update(dict(json_data))
        
            db.session.commit()
            db.session.close()
            db.engine.dispose()

    def delete_AdInfo(self,para):

        data = AdditionalInformation.query.filter_by(UUID = para.UUID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


class ProjectReviewStatusRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in ProjectReviewStatus.query.all()]
    get_by_id      = lambda self, ID : [ProjectReviewStatus.query.filter_by(ID = ID).first().__to_dict__()]
    get_by_uuid    = lambda self, UUID : [row.__to_dict__() for row in ProjectReviewStatus.query.filter_by(UUID = UUID).all()]
    get_by_ExamID  = lambda self, ExamID,UUID : [row.__to_dict__() for row in ProjectReviewStatus.query.filter_by(ExamID = ExamID, UUID = UUID).all()]
    get_by_assigned_reviewer    = lambda self, rev_id : [row.__to_dict__() for row in ProjectReviewStatus.query.filter_by(AssignedReviewer = rev_id).all()]
    get_by_review_status    = lambda self, rev_id : [row.__to_dict__() for row in ProjectReviewStatus.query.filter_by(AssignedReviewer = rev_id,ReviewStatus=False).all()]
    get_by_review_status1    = lambda self, rev_id : [row.__to_dict__() for row in ProjectReviewStatus.query.filter_by(AssignedReviewer = rev_id,ReviewStatus=True).all()]


    #question_tbls
    get_by_L2QuestionID    = lambda self, L2QuestionID : [row.__to_dict__() for row in Level2Question.query.filter_by(L2QuestionID = L2QuestionID).all()]
    # get_by_SubjectID  = lambda self, SubjectID : [row.__to_dict__() for row in Level2Question.query.filter_by(SubjectID = SubjectID).all()]

  
    def get_with_question(self,UUID):
        all = self.get_by_uuid(UUID) 

        project_review_status_with_question = []
        d={}
        for row in all:
            total_marks=row["TotalMarks"]
            if row["L2Marks"]==None:
                obtained_marks=0
            else:
                obtained_marks=row["L2Marks"]

            percentage=float((obtained_marks/total_marks)*100)
            d.update({"Percentage":percentage})

            project_review_status_with_question.append({**row, **self.get_by_L2QuestionID(L2QuestionID = row["L2QuestionID"])[0],**PersonalDetailsRepository().get_by_id(UUID = row["UUID"])[0], **d})


        return project_review_status_with_question

    
    def get_with_details(self,rev_id,SubjectID):
        
        all = self.get_by_review_status(rev_id) 
        

        project_review_status_with_details = []
        for row in all:

            project_review_status_with_details.append({**row, **self.get_by_L2QuestionID(L2QuestionID = row["L2QuestionID"])[0],**PersonalDetailsRepository().get_by_id(UUID = row["UUID"])[0]})

        
        x=[d for d in project_review_status_with_details if d['SubjectID'] == SubjectID]

        return x

class ReviewerProfileRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in ReviewerProfile.query.all()]
    get_by_id      = get_by_id    = lambda self, ID : [ReviewerProfile.query.filter_by(ID = ID).first().__to_dict__()]
    get_by_uuid    = lambda self, UUID : [row.__to_dict__() for row in ReviewerProfile.query.filter_by(UUID = UUID).all()]
    get_by_assigned_subject    = lambda self, AssignedSubject : [row.__to_dict__() for row in ReviewerProfile.query.filter_by(AssignedSubject = AssignedSubject).all()]

    def subject_with_name(self,UUID):
        """Returns the Information of the Institute, alongwith State Information"""

        all_subjects = self.get_by_uuid(UUID) # get list of all institute information

        subject_name = []
        for row in all_subjects:
            try:
                subject_name.append({**row, **SubjectMasterRepository().get_by_id(SubjectID = row["AssignedSubject"])[0]})
            except AttributeError as err:
                # error is raised when a StateID present in InstituteMaster
                # but the StateID is not Present in StateMaster
                # TODO: throw a CRITICAL error for DevOps

                # this function will append `None` value to Each Row
                # when StateID is missing
                subject_name.append({**{k : None for k in SubjectMaster().__get_column_names__()}, **row})

        return subject_name
    
    def get_for_dashboard(self,UUID):
        all_reviewer_details = self.get_by_uuid(UUID) # get list of all institute information
        pending_reviews= ProjectReviewStatusRepository().get_by_review_status(UUID)
        print(pending_reviews)
        print(len(pending_reviews))

        everything = []
        Total=0
        t={}
        for i in range(len(all_reviewer_details)):
            Total=Total+all_reviewer_details[i]["NoOfReviews"]
            t.update({"Total_reviews": Total})

        t.update({"Pending_Reviews":len(pending_reviews)})
        
        for row in all_reviewer_details:
            
            try:
                everything.append({**row,**PersonalDetailsRepository().get_by_id(UUID=row["UUID"])[0], **t})

            except AttributeError as err:

                everything.append({**{k : None for k in PersonalDetails().__get_column_names__()}, **row})

        return everything
    
    def create_revprofile(self,para):
        new_revprofile = ReviewerProfile(UUID=para.UUID, AssignedSubject=para.AssignedSubject)
        db.session.add(new_revprofile)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

    def update_revprofile(self,para):
        json_data = request.get_json()
 
        if json_data["UUID"]:
            # del json_data['token']

            data = ReviewerProfile.query.filter_by(UUID=json_data["UUID"]).update(dict(json_data))
        
            db.session.commit()
            db.session.close()
            db.engine.dispose()

    def delete_revprofile(self,para):

        data = ReviewerProfile.query.filter_by(ID = para.ID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


class ExamResultRepository:
    get_all      = lambda self : [row.__to_dict__() for row in ExamResult.query.all()]
    get_by_UUID    = lambda self, UUID : [row.__to_dict__() for row in ExamResult.query.filter_by(UUID = UUID).all()]