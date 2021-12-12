# -*- encoding: utf-8 -*-

from ... import db
from ...models import *

class StateMasterRepository:

    get_all      = lambda self : [row.__to_dict__() for row in StateMaster.query.all()]
    get_by_id    = lambda self, StateID : [StateMaster.query.filter_by(StateID = StateID).first().__to_dict__()]
    get_by_name  = lambda self, StateName : [StateMaster.query.filter_by(StateName = StateName).first().__to_dict__()]
    get_by_abbrv = lambda self, StateAbbreviation : [StateMaster.query.filter_by(StateAbbreviation = StateAbbreviation).first().__to_dict__()]


class InstituteMasterRepository:

    get_all     = lambda self : [row.__to_dict__() for row in InstituteMaster.query.all()]
    get_by_id   = lambda self, InstituteID : [InstituteMaster.query.filter_by(InstituteID = InstituteID).first().__to_dict__()]
    get_by_name = lambda self, InstituteName : [InstituteMaster.query.filter_by(InstituteName = InstituteName).first().__to_dict__()]

    # foreign key search(s)
    get_by_state_id = lambda self, StateID : [row.__to_dict__() for row in InstituteMaster.query.filter_by(StateID = StateID).all()]


    def get_institute_with_state(self):
        """Returns the Information of the Institute, alongwith State Information"""

        all_institutes = self.get_all() # get list of all institute information

        institute_with_state = []
        for row in all_institutes:
            try:
                print(StateMasterRepository().get_by_id(StateID = row["StateID"])[0])
                institute_with_state.append({**row, **StateMasterRepository().get_by_id(StateID = row["StateID"])[0]})
            except AttributeError as err:
                # error is raised when a StateID present in InstituteMaster
                # but the StateID is not Present in StateMaster
                # TODO: throw a CRITICAL error for DevOps

                # this function will append `None` value to Each Row
                # when StateID is missing
                institute_with_state.append({**{k : None for k in StateMaster().__get_column_names__()}, **row})

        return institute_with_state


    def create_institute(self, para):

        new_institute = InstituteMaster(InstituteName = para.InstituteName  ,StateID = para.StateID)

        db.session.add(new_institute)
        db.session.commit()
        db.session.close()
        db.engine.dispose()
                 
        
    def update_institute(self,para):

        data = InstituteMaster.query.filter_by(InstituteID = para.InstituteID).update(dict(InstituteName = para.InstituteName,StateID = para.StateID))
        db.session.commit()
        db.session.close()
        db.engine.dispose()


    def delete_institute(self,para):

        data = InstituteMaster.query.filter_by(InstituteID = para.InstituteID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()



class QualificationMasterRepository:
    
    get_all     = lambda self : [row.__to_dict__() for row in QualificationMaster.query.all()]
    get_by_id   = lambda self, QualificationID : [QualificationMaster.query.filter_by(QualificationID = QualificationID).first().__to_dict__()]
    get_by_name = lambda self, QualificationName : [QualificationMaster.query.filter_by(QualificationName = QualificationName).first().__to_dict__()]

    # foreign key search(s)
    get_by_institute_id = lambda self, InstituteID : [row.__to_dict__() for row in QualificationMaster.query.filter_by(InstituteID = InstituteID).all()]


    def get_qualification_with_institute(self):
        """Returns the Information of the Qualification, alongwith Institute Information"""

        all_qualifications = self.get_all() # get list of all institute information

        qualification_with_institute = []
        for row in all_qualifications:
            try:
                qualification_with_institute.append({**row, **InstituteMasterRepository().get_by_id(InstituteID = row["InstituteID"])[0]})
            except AttributeError as err:
                # error is raised when a StateID present in InstituteMaster
                # but the StateID is not Present in StateMaster
                # TODO: throw a CRITICAL error for DevOps

                # this function will append `None` value to Each Row
                # when StateID is missing
                qualification_with_institute.append({**{k : None for k in InstituteMaster().__get_column_names__()}, **row})

        return qualification_with_institute


    def create_qualification(self, para):
        
        new_qua = QualificationMaster(QualificationName = para.QualificationName, InstituteID = para.InstituteID)
        db.session.add(new_qua)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


    def update_qualification(self,para):
       
        data= QualificationMaster.query.filter_by(QualificationID = para.QualificationID).update(dict(QualificationName = para.QualificationName, InstituteID = para.InstituteID))
        db.session.commit()
        db.session.close()
        db.engine.dispose()

    def delete_qualification(self,para):

        data= QualificationMaster.query.filter_by(QualificationID = para.QualificationID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()



class SpecializationMasterRepository:
    
    get_all     = lambda self : [row.__to_dict__() for row in SpecializationMaster.query.all()]
    get_by_id   = lambda self, SpecializationID : [SpecializationMaster.query.filter_by(SpecializationID = SpecializationID).first().__to_dict__()]
    get_by_name = lambda self, SpecializationName : [SpecializationMaster.query.filter_by(SpecializationName = SpecializationName).first().__to_dict__()]

    # foreign key search(s)
    get_by_qualification_id = lambda self, QualificationID : [row.__to_dict__() for row in SpecializationMaster.query.filter_by(QualificationID = QualificationID).all()]


    def get_specialization_with_qualification(self):
        """Returns the Information of the Specialization, alongwith Qualification Information"""

        all_specialization = self.get_all() # get list of all institute information

        specialization_with_qualification = []
        for row in all_specialization:
            try:
                specialization_with_qualification.append({**row, **QualificationMasterRepository().get_by_id(QualificationID = row["QualificationID"])[0]})
            except AttributeError as err:
                # error is raised when a StateID present in InstituteMaster
                # but the StateID is not Present in StateMaster
                # TODO: throw a CRITICAL error for DevOps

                # this function will append `None` value to Each Row
                # when StateID is missing
                specialization_with_qualification.append({**{k : None for k in QualificationMaster().__get_column_names__()}, **row})

        return specialization_with_qualification


    def create_specialization(self, para):

        new_specialization = SpecializationMaster(SpecializationName = para.SpecializationName, QualificationID = para.QualificationID)
        
        db.session.add(new_specialization)
        db.session.commit()
        db.session.close()
        db.engine.dispose()





    def update_specialization(self,para):

        data= SpecializationMaster.query.filter_by(SpecializationID = para.SpecializationID).update(dict(SpecializationName = para.SpecializationName, QualificationID = para.QualificationID))
        db.session.commit()
        db.session.close()
        db.engine.dispose()


    def delete_specialization(self,para):

        data= SpecializationMaster.query.filter_by(SpecializationID = para.SpecializationID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

            


class BoardMasterRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in BoardMaster.query.all()]
    get_by_id    = lambda self, BoardID : [BoardMaster.query.filter_by(BoardID = BoardID).first().__to_dict__()]
    get_by_name  = lambda self, BoardName : [BoardMaster.query.filter_by(BoardName = BoardName).first().__to_dict__()]
    get_by_class = lambda self, Class10 : [row.__to_dict__() for row in BoardMaster.query.filter_by(Class10 = Class10).all()]


    def create_boards(self, para):

        # print(para.Class10)

        new_board = BoardMaster(BoardName = para.BoardName, Class10= para.Class10)
        db.session.add(new_board)
        db.session.commit()
        db.session.close()
        db.engine.dispose()



    def update_board(self,para):

        data= BoardMaster.query.filter_by(BoardID = para.BoardID).update(dict(BoardName = para.BoardName))
        db.session.commit()
        db.session.close()
        db.engine.dispose()


    def delete_board(self,para):

        data= BoardMaster.query.filter_by(BoardID = para.BoardID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()




class SubjectMasterRepository:
    
    get_all      = lambda self : [row.__to_dict__() for row in SubjectMaster.query.all()]
    get_by_id    = lambda self, SubjectID : [SubjectMaster.query.filter_by(SubjectID = SubjectID).first().__to_dict__()]
    get_by_name  = lambda self, SubjectName : [SubjectMaster.query.filter_by(SubjectName = SubjectName).first().__to_dict__()]


    def create_subject(self,para):

        new_subject = SubjectMaster(SubjectName = para.SubjectName)
        db.session.add(new_subject)
        db.session.commit()
        db.session.close()
        db.engine.dispose()

    
    def update_subject(self,para):

        data= SubjectMaster.query.filter_by(SubjectID=para.SubjectID).update(dict(SubjectName = para.SubjectName))
        db.session.commit()
        db.session.close()
        db.engine.dispose()


    def delete_subject(self,para):

        data = SubjectMaster.query.filter_by(SubjectID = para.SubjectID).first()
        db.session.delete(data)
        db.session.commit()
        db.session.close()
        db.engine.dispose()


