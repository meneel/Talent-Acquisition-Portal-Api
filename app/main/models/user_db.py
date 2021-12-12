# -*- encoding: utf-8 -*-
import jwt
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from .. import db
from app.main.config import *
from .master_db import *
from .questions_db import *
from app.main import *

class PersonalDetails(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "PersonalDetails"

    UUID = db.Column(db.String(64), primary_key = True, nullable = False)
    username = db.Column(db.String(32),unique=True, nullable = False)
    UserRole = db.Column(db.String(16),nullable=False, default='User')
    FirstName = db.Column(db.String(128), nullable=False)
    LastName = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    SubjectID = db.Column(db.Integer, db.ForeignKey(SubjectMaster.SubjectID), nullable = True)

    ImageLocation = db.Column(db.String(50), nullable=False, default='default.jpg')
    
    StateID = db.Column(db.String(64), db.ForeignKey(StateMaster.StateID), nullable=True)
    CityName = db.Column(db.String(50), nullable=True)
    Pincode = db.Column(db.Integer, nullable=True)
    Address = db.Column(db.String(512), nullable=True)

    CountryCode = db.Column(db.String(4), nullable=False)
    MobileNumber = db.Column(db.String(16), unique=True, nullable=False)

    PrimaryCollegeID = db.Column(db.Integer, db.ForeignKey(InstituteMaster.InstituteID), nullable=True)
    PC_StudyLevelID = db.Column(db.Integer,db.ForeignKey(QualificationMaster.QualificationID), nullable=True)
    PC_CourseID = db.Column(db.Integer,db.ForeignKey(SpecializationMaster.SpecializationID), nullable=True)
    PC_Registration = db.Column(db.String(20), nullable=True)
    PC_Percentage = db.Column(db.Float, nullable=True)
    PC_Batch = db.Column(db.String(30), nullable=True)

    Class10Institute = db.Column(db.String(256), nullable=True)
    Class10BoardID = db.Column(db.Integer ,db.ForeignKey(BoardMaster.BoardID), nullable=True)
    Class10Percentage = db.Column(db.Float, nullable=True)
    Class10YOP = db.Column(db.Integer, nullable=True)

    Class12Institute = db.Column(db.String(256), nullable=True)
    Class12BoardID = db.Column(db.Integer ,db.ForeignKey(BoardMaster.BoardID), nullable=True)
    Class12Percentage = db.Column(db.Float, nullable=True)
    Class12YOP = db.Column(db.Integer, nullable=True)


    def hash_password(self):
        self.password = generate_password_hash(self.password)


    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_token(self, expires_sec=1800):
        token = jwt.encode({'UUID': self.UUID},key, algorithm="HS256")
        return token

    @staticmethod
    def verify_reset_token(token):
        # s = Serializer(app.config['SECRET_KEY'])
        # # try:
        # user_id = s.loads(token)['user_id']
        # # except:
        # #     return None

        # return User.query.filter_by(user_id = user_id)
        if token:
                try:
                    data = jwt.decode(token,options={"verify_signature": False},  algorithms="HS256")
                    # print(data)
                    current_user = PersonalDetails.query.filter_by(UUID = data['UUID']).all()
                except jwt.ExpiredSignatureError:
                    msg = 'Signature has expired.'
                    return {'message':msg}
                except jwt.DecodeError:
                    msg = 'Error decoding signature.'
                    return {'message':msg}
                except jwt.InvalidTokenError:
                    msg = 'token is invalid'
                    return {'message':msg}

                return  data
        else:
            return {"remarks" : "pass the token"}



class AdditionalEducationDetails(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "AdditionalEducationDetails"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)

    StudyLevel = db.Column(db.Integer,db.ForeignKey(QualificationMaster.QualificationID), nullable=True)
    InstitueID = db.Column(db.Integer, db.ForeignKey(InstituteMaster.InstituteID), nullable=True)
    CourseID = db.Column(db.Integer,db.ForeignKey(SpecializationMaster.SpecializationID), nullable=True)
    RegistrationNumber = db.Column(db.String(20), nullable=True)
    Percentage = db.Column(db.Float, nullable=True)
    StartYear = db.Column(db.Integer, nullable=True)
    EndYear = db.Column(db.Integer, nullable=True)



class ExperienceDetails(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "ExperienceDetails"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)
    Designation = db.Column(db.String(128), nullable=True) #designation master?
    DepartmentName = db.Column(db.String(64), nullable=True)
    Organization = db.Column(db.String(128), nullable=True)
    StartYear = db.Column(db.Integer, nullable=False)
    EndYear = db.Column(db.Integer, nullable=True)



class AdditionalInformation(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "AdditionalInformation"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)
    ResumeCopyLocation = db.Column(db.String(512), nullable=True)
    Skills = db.Column(db.String(512), nullable=True)
    ECActivities = db.Column(db.String(512), nullable=True)
    ProjectLinks = db.Column(db.String(512), nullable=True)


class ProjectReviewStatus(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "ProjectReviewStatus"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)
    ExamID = db.Column(db.Integer, nullable = True)
    L2QuestionID = db.Column(db.Integer, db.ForeignKey(Level2Question.L2QuestionID), nullable = True)
    L2Answer = db.Column(db.String(200),nullable = True)
    AssignedReviewer = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = True)
    Review = db.Column(db.String(200),nullable = True)
    TotalMarks = db.Column(db.Integer, nullable = True)
    L2Marks = db.Column(db.Integer, nullable = True)
    ReviewStatus = db.Column(db.Boolean,default=False,nullable=True)
    StartTime =db.Column(db.String(64),default=datetime.now, nullable=True)
    EndTime =db.Column(db.String(64), nullable=True)



class ReviewerProfile(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "ReviewerProfile"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)
    AssignedSubject = db.Column(db.Integer, db.ForeignKey(SubjectMaster.SubjectID), nullable = True)
    NoOfReviews = db.Column(db.Integer,default=0, nullable =False)

