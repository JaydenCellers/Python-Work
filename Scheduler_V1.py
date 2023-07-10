import schedule
import time
from datetime import datetime, timedelta

class Patient:
    def __init__(self, name) -> None:
        self.name = name

class Doctor:

    def __init__(self, name) -> None:
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

class DayCounter:
    
    def __init__(self) -> None:
        self.counter = 0

def schedule_appointments(doctor):
    print(f'Doctor {doctor.name} Schedule:')
    total_patients = len(doctor.patients)
    apps_per_day = 16
    num_days = (total_patients - 1) // apps_per_day + 1
    
    appointment_time = datetime.strptime("2023-07-10 09:00", "%Y-%m-%d %H:%M")
    for day in range(num_days):
        start = day * apps_per_day
        end = min(start + apps_per_day, total_patients)
        appointments = doctor.patients[start: end]
        for i, patient in enumerate(appointments, start = 1):
            schedule.every(day + 1).minutes.at(":00").do(appointment, doctor.name, patient.name, i, appointment_time)
            appointment_time += timedelta(minutes=30)
        appointment_time += timedelta(hours=16)

def appointment(doctor_name, patient_name, number, app_time):
    print(f' Appointment {number}: {patient_name} with Dr. {doctor_name} at {app_time}')

dc = DayCounter()
dayendtime = ":30"

doctor1 = Doctor('John Doe')
doctor2 = Doctor('Jane Doe')

patient1 = Patient('Alex')
patient2 = Patient('Bob')
patient3 = Patient('Cameron')
patient4 = Patient('Drake')
patient5 = Patient('Ethan')
patient6 = Patient('Frank')
patient7 = Patient('Gabe')
patient8 = Patient('Hector')
patient9 = Patient('Ignacio')
patient10 = Patient('Jake')
patient11 = Patient('Kevin')
patient12 = Patient('Landon')
patient13 = Patient('Matthew')
patient14 = Patient('Nick')
patient15 = Patient('Oscar')
patient16 = Patient('Patrick')
patient17 = Patient('Quincey')


doctor1.add_patient(patient1)
doctor1.add_patient(patient2)
doctor1.add_patient(patient3)
doctor1.add_patient(patient4)
doctor1.add_patient(patient5)
doctor1.add_patient(patient6)
doctor1.add_patient(patient7)
doctor1.add_patient(patient8)
doctor1.add_patient(patient9)
doctor1.add_patient(patient10)
doctor1.add_patient(patient11)
doctor1.add_patient(patient12)
doctor1.add_patient(patient13)
doctor1.add_patient(patient14)
doctor1.add_patient(patient15)
doctor1.add_patient(patient16)
doctor1.add_patient(patient17)

schedule_appointments(doctor1)

while True:
    schedule.run_pending()
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time >= dayendtime:
        schedule.clear()
    time.sleep(5)