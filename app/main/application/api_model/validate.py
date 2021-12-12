# -*- encoding: utf-8 -*-

from datetime import date
from ...repository.interface import *

def validate_start_year(year):
    cur_year = date.today().year

    if year <= cur_year - 5:
        raise ValueError("year should be within 5 year from current")
    elif year > cur_year:
        raise ValueError("year greater than current year")
    else:
        return True

def validate_end_year(start, end):
    validate_start_year(start)
    if end - start > 5:
        raise ValueError("end year too big than start")
    else:
        return True

def validate_marks(marks):
    if marks<0 or marks>100:
        raise ValueError("Marks cannot be less than 0 or more than 100")
    else:
        return True

def validate_percent(percent):
    formatted_string = "{:.2f}".format(percent)
    float_value = float(formatted_string)
    if float_value<0.00 or float_value>100.00:
        raise ValueError("Percentage cannot be less than 0.0 or more than 100.0")
    else:
        return True

def validate_email(email):
    a=PersonalDetailsRepository().get_by_email(email)
    Email=""
    for row in a:
        Email=row["email"]
    if "@" not in email:
        raise ValueError("Please pass valid Email ID")
    elif email == Email:
        raise ValueError("Email already exists")
    else:
        return True

def validate_mob(mob):
    def check(mob):
        a=PersonalDetailsRepository().get_by_mob(mob)
        Mob=0
        for row in a:
            Mob=row["MobileNumber"]
        
        return Mob

    if len(mob)<10 or len(mob)>10:
        raise ValueError("Please pass valid Mobile Number")
    elif mob == check(mob):
        raise ValueError("Mobile Number already exists")
    else:
        return True

def validate_username(username):
    def check(username):
        a=PersonalDetailsRepository().get_by_username(username)
        Username=""
        for row in a:
            Username=row["username"]
        
        return Username

    if username == check(username):
        raise ValueError("Username already exists")
    else:
        return True

def validate_institute(institute):
    institute=institute.upper()
    def check():
        a=InstituteMasterRepository().get_institute_with_state()
        Institute=""
        for row in a:
            Institute=row["InstituteName"]
            Institute=Institute.upper()
        return Institute

    if len(institute)>64:
        raise ValueError("Value Too big")
    elif institute == check():
        raise ValueError("Institute already exists")
    else:
        return True

def validate_institute_by_id(institute,id):
    institute=institute.upper()
    def check(id):
        a=InstituteMasterRepository().get_by_id(id)
        Institute=""
        for row in a:
            Institute=row["InstituteName"]
            Institute=Institute.upper()
        return Institute

    if len(institute)>64:
        raise ValueError("Value Too big")
    elif institute == check(id):
        raise ValueError("Institute already exists")
    else:
        return True

def validate_qualification(qualification,institute):
    qualification=qualification.upper()
    def check(institute):
        a=QualificationMasterRepository().get_by_institute_id(institute)
        Qualification1=[]
        for row in a:
            Qualification=row["QualificationName"]
            Qualification=Qualification.upper()
            Qualification1.append(Qualification)
        return Qualification1

    if len(qualification)>64:
        raise ValueError("Value Too big")
    elif qualification in check(institute):
        raise ValueError("Qualification already exists")
    else:
        return True

def validate_qualification_by_id(qualification,id):
    qualification=qualification.upper()
    def check(id):
        a=QualificationMasterRepository().get_by_id(id)
        Qualification1=[]
        for row in a:
            Qualification=row["QualificationName"]
            Qualification=Qualification.upper()
            Qualification1.append(Qualification)
        return Qualification1

    if len(qualification)>64:
        raise ValueError("Value Too big")
    elif qualification == check(id):
        raise ValueError("Qualification already exists")
    else:
        return True


def validate_specialization(specialization,qualification):
    specialization=specialization.upper()
    def check(qualification):
        a=SpecializationMasterRepository().get_by_qualification_id(qualification)
        Specialization1=[]
        for row in a:
            Specialization=row["SpecializationName"]
            Specialization=Specialization.upper()
            Specialization1.append(Specialization)
        return Specialization1

    if len(specialization)>64:
        raise ValueError("Value Too big")
    elif specialization in check(qualification):
        raise ValueError("Specialization already exists")
    else:
        return True

def validate_specialization_by_id(specialization,id):
    specialization=specialization.upper()
    def check(id):
        a=SpecializationMasterRepository().get_by_id(id)
        Specialization1=[]
        for row in a:
            Specialization=row["SpecializationName"]
            Specialization=Specialization.upper()
            Specialization1.append(Specialization)
        return Specialization1

    if len(specialization)>64:
        raise ValueError("Value Too big")
    elif specialization == check(id):
        raise ValueError("Specialization already exists")
    else:
        return True
