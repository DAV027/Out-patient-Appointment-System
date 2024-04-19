from flask_pymongo import PyMongo

mongo = PyMongo()

class Doctor:
    def __init__(self, name, specialty, schedule):
        self.name = name
        self.specialty = specialty
        self.schedule = schedule

class Appointment:
    def __init__(self, doctor_id, date, patient_name):
        self.doctor_id = doctor_id
        self.date = date
        self.patient_name = patient_name
