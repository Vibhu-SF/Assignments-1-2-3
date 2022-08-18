import studentMod as sm  # importing student file
import json

clgDb = []  # database for this module

clg_id = 0  # global variable for unique id distribution


class college(sm.Student):
    clg_name = str
    clg_stream = str
    clg_location = str

    # this function is similar to previous one its just contain some extra attributes
    def addData(self):
        globals()['clg_id'] = globals()['clg_id'] + 1
        self.sID = globals()['clg_id']
        self.first_name = input("enter first name ->\n")
        self.last_name = input("enter last name ->\n")
        self.school_name = input("enter school name ->\n")
        self.sClass = input("enter class name ->\n")
        self.clg_name = input("enter  college name ->\n")
        self.clg_location = input("enter college location ->\n")
        self.clg_stream = input("enter course stream ->\n")

        obj_stud = {"firstname": self.first_name, "lastname": self.last_name, "school": self.school_name, "student_id": self.sID, "student_class": self.sClass,
                    "college_details": {"college_name": self.clg_name, "college_stream": self.clg_stream,
                                        "clg_location": self.clg_location}}
        clgDb.append(obj_stud)
        file = open('data', 'w')
        file.write(json.dumps(clgDb))
        print("### data-updated ###\n")

# this function will simply print college details

    def getCollegeDetails(self):
        sID = int(input("Enter student Id -> \n"))
        file = open('data', 'r')
        database = json.loads(file.read())
        flag = 0
        for obj in database:
            if obj['student_id'] == sID:
                print(obj['college_details'])
                flag = 1
                break
        if flag == 0:
            print("#### record unavailable ####\n")