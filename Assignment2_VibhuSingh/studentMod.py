import json

student_id = 0  # student id as global
arrayOfFields = []  # empty list


# this is our main student module class 
class Student:

# attributes of stud class -
    std_id: int
    first_name: str 
    last_name: str
    school_name: str
    stud_class: str


    def addData(self):  # (self is a default argument in python)

        # setting student id as global and autoincrement; when a new record is inserted
        globals()['student_id'] = globals()['student_id'] + 1  
        
        # taking user input -
        self.std_id = globals()['student_id'] # autoincrement
        self.first_name = input("enter firstname ->\n")
        self.last_name = input("enter lastname ->\n")
        self.school_name = input("enter school name ->\n")
        self.stud_class = input("enter class ->\n")

         # creating obj with the required variables
        obj_stud = {"firstname": self.first_name, "lastname": self.last_name, "school": self.school_name, "student_id": self.std_id, "student_class": self.stud_class} 

        arrayOfFields.append(obj_stud)  # inserting the values
        file = open('data', 'w')  
        file.write(json.dumps(arrayOfFields))  # .dumps converts python obj to json 
        print("### data-updated ###\n") 

    # function to display data wrt sID
    def displayData(self):
        std_id = int(input("enter Id of student ->\n"))
        file = open('data', 'r')  # opening file in read mode to retrieve the data
        storeData = json.loads(file.read())  # converting json  data into python list

        flag = 0
        for obj in storeData:   # searching data wrt sID
            if obj['student_id'] == std_id:
                print(obj)
                flag = 1
                break
        if flag == 0:
            print("#### record unavailable ####\n")

    # function to delete data from all the user inputs
    def deleteRecord(self):
        std_id = int(input("enter studentId to delete -> \n"))
        file = open('data', 'r')
        storeData = json.loads(file.read())  # loads function converts json to python list

        flag = 0
        for obj in storeData:  # searching the record and any record is present we will remove it
            if obj['student_id'] == std_id:
                storeData.remove(obj)
                file2 = open('data', 'w')
                file2.write(json.dumps(storeData))
                flag = 1
                break
        if flag == 0:
            print("#### record unavailable ####\n")
