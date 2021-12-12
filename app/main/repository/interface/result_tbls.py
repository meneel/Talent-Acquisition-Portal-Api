# -*- encoding: utf-8 -*-
from sqlalchemy import func
from ... import db
from ...models import *
from .user_tbls import ProjectReviewStatusRepository 

class Level1ResultRepository:

    get_all      = lambda self : [row.__to_dict__() for row in Level1Result.query.all()]
    get_by_UUID    = lambda self, UUID : [row.__to_dict__() for row in Level1Result.query.filter_by(UUID = UUID).all()]
    get_by_ExamID  = lambda self, ExamID,UUID : [row.__to_dict__() for row in Level1Result.query.filter_by(ExamID = ExamID, UUID = UUID).all()]
    get_by_SubjectID = lambda self, SubjectID,UUID : [row.__to_dict__() for row in Level1Result.query.filter_by(SubjectID = SubjectID,UUID = UUID ).all()]

    def get_marks_by_ExamID(self,para):
        d={}
        total_marks=0
        obtained_marks=0
        data1=self.get_by_ExamID(para["ExamID"],para["UUID"])

        for i in range(len(data1)):
            total_marks=total_marks+data1[i]["TotalMarks"]
            obtained_marks=obtained_marks+data1[i]["ObtainedMarks"]

        d.update({"ExamID": para["ExamID"] })
        d.update({"TotalMarks": total_marks })
        d.update({"ObtainedMarks": obtained_marks })

        return d

    def get_percentage_by_UUID(self,para):
        data1=self.get_by_UUID(para["UUID"])
        total_marks=0
        obtained_marks=0
        d={}
        for i in range(len(data1)):
            total_marks=total_marks+data1[i]["TotalMarks"]
            obtained_marks=obtained_marks+data1[i]["ObtainedMarks"]
            percentage= float((obtained_marks/total_marks)*100)
            d.update({"ExamID": data1[i]["ExamID"] })
            d.update({"TotalMarks": total_marks })
            d.update({"ObtainedMarks": obtained_marks })
            d.update({"Percentage":percentage})


        return d

class ReviewerRepository:

    def review_post(self,para):
        def get_id(UUID):
            
                query1 = db.session.query(func.max(ExamResult.L1ExamID)).filter(
                    ExamResult.UUID == UUID
            
                ).scalar()
                if query1 is not  None:
                    return query1
        if para.Review:
            data = ProjectReviewStatus.query.filter_by(UUID = para.UUID,ExamID= para.ExamID).update(dict(Review=para.Review, L2Marks=para.L2Marks,ReviewStatus=True))
            db.session.commit()
            db.session.close()
            db.engine.dispose()
        

        total_marks=0
        data1=ProjectReviewStatusRepository().get_by_ExamID(UUID=para.UUID,ExamID= para.ExamID)
        print(data1)
        rev_id=data1[-1]["AssignedReviewer"]
        if data1[-1]["ReviewStatus"]==True:
            data2= ReviewerProfile.query.filter_by(UUID=rev_id).update(dict(NoOfReviews=ReviewerProfile.NoOfReviews+1))
        
            db.session.commit()
            db.session.close()
            db.engine.dispose()

        total_marks=total_marks+data1[-1]["TotalMarks"]
        obtained_marks=para.L2Marks

        if int(obtained_marks)>=(int(0.4*total_marks)):
            Result = ExamResult.query.filter_by(UUID = para["UUID"],L1ExamID=get_id(UUID = para["UUID"])).update(dict(L2Status=True, L2Marks= obtained_marks))
            db.session.commit()
            db.session.close()
            db.engine.dispose()
        else:
            Result = ExamResult.query.filter_by(UUID = para["UUID"],L1ExamID=get_id(UUID = para["UUID"])).update(dict(L2Status=False, L2Marks= obtained_marks))
            db.session.commit()
            db.session.close()
            db.engine.dispose()
        



