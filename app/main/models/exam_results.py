# -*- encoding: utf-8 -*-
from .. import db
from .master_db import *
from .user_db import *
from .questions_db import *

class ExamResult(db.Model):
    """ExamResult"""

    __tablename__ = "ExamResult"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)
    L1Status = db.Column(db.Boolean, nullable = True)
    L1ExamID = db.Column(db.Integer, nullable = True)
    L2Status = db.Column(db.Boolean, nullable = True)
    L1Marks = db.Column(db.Integer, nullable = True)
    L2Marks = db.Column(db.Integer, nullable = True)


class Level1Result(db.Model):
    """Level1Result"""

    __tablename__ = "Level1Result"

    ID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    UUID = db.Column(db.String(64), db.ForeignKey(PersonalDetails.UUID), nullable = False)
    ExamID = db.Column(db.Integer, nullable = True)
    SubjectID = db.Column(db.Integer, db.ForeignKey(SubjectMaster.SubjectID), nullable = True)
    L1QuestionID = db.Column(db.Integer, db.ForeignKey(Level1Quesion.L1QuestionID), nullable = True)
    TotalMarks = db.Column(db.Integer, nullable = True)
    ObtainedMarks = db.Column(db.Integer, nullable = True)
    Attempted = db.Column(db.Boolean,default= False, nullable = True)
    CorrectAnswer = db.Column(db.Boolean, nullable = True)

