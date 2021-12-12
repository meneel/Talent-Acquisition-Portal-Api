# -*- encoding: utf-8 -*-

from sqlalchemy import func
import random
from datetime import datetime
from datetime import timedelta
from app.main.repository.interface.user_tbls import (PersonalDetailsRepository
                                                    ,ReviewerProfileRepository
                                                    ,ProjectReviewStatusRepository)
from ... import db
from ...models import *

class Level1QuesionRepository:

    get_all      = lambda self : [row.__to_dict__() for row in Level1Quesion.query.all()]
    get_by_L1QuestionID    = lambda self, L1QuestionID : [row.__to_dict__() for row in Level1Quesion.query.filter_by(L1QuestionID = L1QuestionID).all()]
    get_by_SubjectID  = lambda self, SubjectID : [row.__to_dict__() for row in Level1Quesion.query.filter_by(SubjectID = SubjectID).all()]

    def get_question_sub(self,para):

        for i in range(len(para["SubjectID"])):
            if i == 0:    
                data = self.get_by_SubjectID(para["SubjectID"][0])
                h = random.sample((data),6)
                sub_1={}
                for i in range(len(h)):
                    b = random.sample(h[i]["WrongOptions"].split(","), 3 )
                    b+=[h[i]["CorrectOption"]]
                    random.shuffle(b)
                    d = {value: index for index, value in zip(b,["option1","option2","option3","option4"])}
                    sub_1.update({"Options":b})
                    h[i].update(sub_1)
                PersonalDetails.query.filter_by(UUID = para["UUID"][0]).update(dict(SubjectID=para["SubjectID"][0]))
                db.session.commit()
                db.session.close()
                db.engine.dispose()
                
            elif i == 1:
                data = self.get_by_SubjectID(para["SubjectID"][1])
                k = random.sample((data),3)
                sub_2={}
                for i in range(len(k)):
                    b = random.sample(k[i]["WrongOptions"].split(","), 3 )
                    b+=[k[i]["CorrectOption"]]
                    random.shuffle(b)
                    d = {value: index for index, value in zip(b,["option1","option2","option3","option4"])}
                    sub_2.update({"Options":b})
                    k[i].update(sub_2)
                
            elif i ==2:
                data = self.get_by_SubjectID(para["SubjectID"][2])
                z = random.sample((data),1)
                sub_3={}
                for i in range(len(z)):
                    b = random.sample(z[i]["WrongOptions"].split(","), 3 )
                    b+=[z[i]["CorrectOption"]]
                    random.shuffle(b)
                    d = {value: index for index, value in zip(b,["option1","option2","option3","option4"])}
                    sub_3.update({"Options":b})
                    z[i].update(sub_3)

        LIST = h+k+z
        
        return LIST


    def Check_answer(self,para):
        def get_next_id(UUID):
        
                    query1 = db.session.query(func.max(Level1Result.ExamID)).filter(
                        Level1Result.UUID ==UUID
                
                    ).scalar()
                    if query1 is None:
                        return 1
                    else:
                        return query1+1

        def get_id(UUID):
    
                query1 = db.session.query(func.max(ExamResult.L1ExamID)).filter(
                    ExamResult.UUID == UUID
            
                ).scalar()
                if query1 is not  None:
                    return query1

        test = ExamResult(L1ExamID= get_next_id(UUID = para["UUID"][0]),UUID = para["UUID"][0])
        db.session.add(test)
        db.session.commit()
        for i in range(len(para['L1QuestionID'])):
            data = self.get_by_L1QuestionID(para['L1QuestionID'][i])
            selected_ans= para["SelectedAnswer"][i]
            actual_ans= data[0]["CorrectOption"]
            print(para["L1QuestionID"][i])
            if selected_ans==actual_ans:

                new_result = Level1Result(ExamID= get_id(UUID = para["UUID"][0]),UUID = para["UUID"][0],SubjectID=para["SubjectID"][i],L1QuestionID = para["L1QuestionID"][i], TotalMarks = data[0]["Marks"], ObtainedMarks = data[0]["Marks"],  Attempted= True, CorrectAnswer =True)
                db.session.add(new_result)
                db.session.commit()
                db.session.close()
                db.engine.dispose()

            else:

                wrong_result = Level1Result(ExamID= get_id(UUID = para["UUID"][0]),UUID = para["UUID"][0],SubjectID=para["SubjectID"][i],L1QuestionID = para["L1QuestionID"][i], TotalMarks = data[0]["Marks"], ObtainedMarks = 0,  Attempted= True, CorrectAnswer =False)
                db.session.add(wrong_result)
                db.session.commit()
                db.session.close()
                db.engine.dispose()


        total_marks=0
        obtained_marks=0
        data1=[row.__to_dict__() for row in Level1Result.query.filter_by(ExamID= get_id(UUID = para["UUID"][0]), UUID = para["UUID"][0]).all()]

        for i in range(len(data1)):
            total_marks=total_marks+data1[i]["TotalMarks"]
            obtained_marks=obtained_marks+data1[i]["ObtainedMarks"]

        if obtained_marks>=(int(0.4*total_marks)):
            Result = ExamResult.query.filter_by(UUID = para["UUID"][0],L1ExamID=get_id(UUID = para["UUID"][0])).update(dict(L1Status=True, L1Marks= obtained_marks))
            db.session.commit()
            db.session.close()
            db.engine.dispose()
        else:
            Result = ExamResult.query.filter_by(UUID = para["UUID"][0],L1ExamID=get_id(UUID = para["UUID"][0])).update(dict(L1Status=False, L1Marks= obtained_marks))
            db.session.commit()
            db.session.close()
            db.engine.dispose()


    def create_question(self,para):
        
        new_question = Level1Quesion(SubjectID = para.SubjectID, Marks = para.Marks,Question = para.Question, WrongOptions=para.WrongOptions, CorrectOption = para.CorrectOption, Time= para.Time)

        db.session.add(new_question)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

    def delete_questions(self,para):

        data = self.get_by_L1QuestionID(para.L1QuestionID)
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()



class Level2QuesionRepository:

    def __init__(self):

        self.personal_details_repository = PersonalDetailsRepository()
        self.reviewer_profile_repository = ReviewerProfileRepository()
        self.project_review_status_repository = ProjectReviewStatusRepository()
    
    
    
    get_all      = lambda self : [row.__to_dict__() for row in Level2Question.query.all()]
    get_by_L2QuestionID    = lambda self, L2QuestionID : [row.__to_dict__() for row in Level2Question.query.filter_by(L2QuestionID = L2QuestionID).all()]
    get_by_SubjectID  = lambda self, SubjectID : [row.__to_dict__() for row in Level2Question.query.filter_by(SubjectID = SubjectID).all()]

   
   
    def create_question(self,para):
        
        new_question = Level2Question(SubjectID = para.SubjectID, Marks = para.Marks,Question = para.Question, Instruction = para.Instruction,FileUpload=para.FileUpload,Image=para.Image, Time= para.Time)

        db.session.add(new_question)
        db.session.commit()
        db.session.close()
        db.engine.dispose()



    def get_question_sub(self,para):
        def get_next_id(UUID):
    
            query1 = db.session.query(func.max(ProjectReviewStatus.ExamID)).filter(
                ProjectReviewStatus.UUID ==UUID
        
            ).scalar()
            if query1 is None:
                return 1
            else:
                return query1+1

        def get_id(UUID):

            query1 = db.session.query(func.max(ProjectReviewStatus.ExamID)).filter(
                ProjectReviewStatus.UUID ==UUID
        
            ).scalar()
            if query1 is not  None:
                return query1
       
        data2= self.personal_details_repository.get_by_id(para["UUID"])
        data = self.get_by_SubjectID(data2[0]["SubjectID"])
        db.session.close()
        db.engine.dispose()
  
        h = random.sample(data,1)
        v= timedelta(days= h[0]["Time"])
        marks= self.get_by_L2QuestionID(h[0]["L2QuestionID"])

        all_reviewer = ReviewerProfileRepository().get_by_assigned_subject(data2[0]["SubjectID"])

        x={}
        sorted_decending={}
        for row in all_reviewer:
            bn= ProjectReviewStatusRepository().get_by_review_status(row["UUID"])
            if bn is not None:
                x.update({row["UUID"]:len(bn)})
        
        sorted_decending= dict(sorted(x.items(), key = lambda x: x[1], reverse = True))
        
        def getList(dict):
            list = []
            for key in dict.keys():
                list.append(key)
                
            return list
        assigned_reviewer=getList(sorted_decending)[-1]


        data1 = ProjectReviewStatus(ExamID= get_next_id(UUID = para.UUID), UUID = para.UUID,L2QuestionID=h[0]["L2QuestionID"], EndTime= datetime.now()+v, TotalMarks= marks[0]["Marks"],AssignedReviewer = assigned_reviewer )
        db.session.add(data1)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

        return h

   
   
    def check_answer(self,para):
        def get_id(UUID):
    
            query1 = db.session.query(func.max(ProjectReviewStatus.ExamID)).filter(
                ProjectReviewStatus.UUID ==UUID
        
            ).scalar()
            if query1 is not  None:
                return query1


        selected_ans= para.SelectedAnswer

        data = ProjectReviewStatus.query.filter_by(UUID = para.UUID,ExamID= get_id(UUID = para.UUID)).update(dict(L2Answer= selected_ans))
        db.session.commit()
        db.session.close()
        db.engine.dispose()



    def delete_questions(self,para):
        try:
            if para.L2QuestionID:
                data = self.get_by_L2QuestionID(para.L2QuestionID)
                db.session.delete(data)
                db.session.commit()
                db.session.close()
                db.engine.dispose()
                return {"status" : "success","error_message": "none" ,"remarks"  : "successfully deleted question"}
        except:
            return {"status" : "failed","error_message": "Foreigh Key Contraint" ,"remarks"  : "Cannot delete question"}


