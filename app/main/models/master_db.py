# -*- encoding: utf-8 -*-
from .. import db

class StateMaster(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "StateMaster"

    StateID           = db.Column(db.String(64), primary_key = True, nullable = False)
    StateAbbreviation = db.Column(db.String(4), unique=True, nullable = False)
    StateName         = db.Column(db.String(32), unique=True, nullable = False)
    AltTag            = db.Column(db.String(32), nullable = False)



class InstituteMaster(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "InstituteMaster"

    InstituteID   = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    InstituteName = db.Column(db.String(256),nullable = False)

    # foreign key(s)
    StateID = db.Column(db.String(64), db.ForeignKey(StateMaster.StateID), nullable = False)



class QualificationMaster(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "QualificationMaster"

    QualificationID   = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    QualificationName = db.Column(db.String(128),nullable = False)

    # foreign key(s)
    InstituteID = db.Column(db.Integer, db.ForeignKey(InstituteMaster.InstituteID), nullable = False)

    

class SpecializationMaster(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "SpecializationMaster"

    SpecializationID   = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    SpecializationName = db.Column(db.String(128), nullable = False)

    # foreign key(s)
    QualificationID = db.Column(db.Integer, db.ForeignKey(QualificationMaster.QualificationID), nullable = False)

    

class BoardMaster(db.Model):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "BoardMaster"

    BoardID   = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    BoardName = db.Column(db.String(128), unique=True,nullable = False)
    Class10   = db.Column(db.Boolean, default = True, nullable = False) # if False, then Class12



class SubjectMaster(db.Model,):
    """Use the Model to Establish a Connection to DB"""

    __tablename__ = "SubjectMaster"

    SubjectID   = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    SubjectName = db.Column(db.String(64), unique=True, nullable = False)

