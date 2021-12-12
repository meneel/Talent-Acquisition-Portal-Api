# -*- encoding: utf-8 -*-
from .. import db
from .master_db import *
from .user_db import *


class Level1Quesion(db.Model):
    """Store L1 Questions"""

    __tablename__ = "Level1Quesion"

    L1QuestionID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    SubjectID = db.Column(db.Integer, db.ForeignKey(SubjectMaster.SubjectID), nullable = True)
    Question = db.Column(db.String(512), nullable=True)
    WrongOptions = db.Column(db.String(128), nullable=True)
    CorrectOption = db.Column(db.String(64), nullable=True)
    Marks = db.Column(db.Integer, nullable = False)
    Time = db.Column(db.Float, nullable = False)


class Level2Question(db.Model):
    """Store L2 Questions"""

    __tablename__ = "Level2Question"

    L2QuestionID = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    SubjectID = db.Column(db.Integer, db.ForeignKey(SubjectMaster.SubjectID), nullable = True)
    Marks = db.Column(db.Integer, nullable = False)
    Question = db.Column(db.String(512), nullable=True)
    Instruction = db.Column(db.String(1024), nullable=True)
    FileUpload = db.Column(db.String(512), nullable=True)
    Image = db.Column(db.String(512), nullable=True)
    Time = db.Column(db.Float, nullable = False)

