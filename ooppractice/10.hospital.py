class Patient:
    def __init__(self, pid, name, age):
        self.patientID = pid
        self.name = name
        self.age = age

    def getPatientInfo(self):
        return f"patientID: {self.patientID}, name = {self.name}, Age: {self.age}"

class Appointment:
    def __init__(self, aid, pid, dn, appt):
        self.appointmentID = aid
        self.patientID = pid
        self.doctorName = dn
        self.appointmentTime = appt

    def getAppointmentDetails(self):
        return f"AppointmentID: {self.appointmentID}, PatientID: {self.patientID}, Doctor: {self.doctorName}, Time: {self.appointmentTime}"

class PatientManager:
    def __init__(self, patients, appointments):
        self.patients = patients
        self.appointments = appointments

    def scheduleAppointment(self, app):
        self.appointments.append(app)

    def cancelAppointment(self, id):
        for i in self.appointments:
            if i.appointmentID == id:
                self.appointments.remove(i)
                return True
        return False

    def listAppointmentsForPatient(self, pid):
        result = []
        for i in self.appointments:
            if i.patientID == pid:
                result.append(i)
        return result

def main():
# Create a patient and two appointments
    patient = Patient(1, "Emma", 30)
    app1 = Appointment(101, patient.patientID, "Dr. Brown", "2:00 PM")
    app2 = Appointment(102, patient.patientID, "Dr. White", "3:00 PM")
    pm = PatientManager([], [])
    pm.patients.append(patient)
    pm.appointments.extend([app1, app2])
    # List appointments for patient
    print("Appointments for Emma:")
    for app in pm.listAppointmentsForPatient(1):
        print(app.getAppointmentDetails())
    # Cancel an appointment and check again
    cancelled = pm.cancelAppointment(101)
    print("Appointment 101 cancelled:", cancelled)
    print("Remaining appointments for Emma:")
    for app in pm.listAppointmentsForPatient(1):
        print(app.getAppointmentDetails())
if __name__ == '__main__':
    main()
