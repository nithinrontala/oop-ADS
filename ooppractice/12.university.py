class Applicant:
    def __init__(self,aid,name,score):
        self.applicationID = aid
        self.name = name
        self.score = score

    def getApplicantInfo(self):
        return f"id: {self.name}, name: {self.name}, scor: {self.score}"
    
class Application:
    def __init__(self,aid,appid,papp):
        self.applicationID = aid
        self.applicantID = appid
        self.programApplied = papp

    def getgetApplicationDetails(self):
        return f"applicationid: {self.applicantID}, applicantid: {self.applicantID}, programApplied: {self.programApplied}"
    
class AdmissionOffice:
    def __init__(self,a,app):
        self.applicants = a
        self.applications = app

    def submitApplication(self,app):
        self.applications.append(app)
    
    def reviewApplication(self,appid):
        for i in self.applicants:
            if i.applicationID == appid:
                return f"Sucess"
        return "failed"

def main():
# Create applicants and applications
    applicant1 = Applicant(1, "Sara", 92.5)
    applicant2 = Applicant(2, "Tom", 85.0)
    application1 = Application(101, 1, "Computer Science")
    application2 = Application(102, 2, "Mathematics")
    office = AdmissionOffice([], [])
    office.applicants.extend([applicant1, applicant2])
    office.applications.extend([application1, application2])
    # Submit an application
    office.submitApplication(application1)
    print("Application submitted for", applicant1.name)
    # Review applications
    review1 = office.reviewApplication(1)
    review_invalid = office.reviewApplication(999)
    print("Review outcome for applicant 1:", review1)
    print("Review outcome for non-existent applicant:", review_invalid)
if __name__ == '__main__':
    main()