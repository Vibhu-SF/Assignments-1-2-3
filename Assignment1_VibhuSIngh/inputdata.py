import json

arrOfFields = ["firstName", "lastName", "schoolName", "className", "marks"]
list = []
totalNumberOfStudents = int(input("Enter total number of students  "))

# add data to array
def addStudent(n):
    for i in range(n):
        dict = {}
        print('Enter details of student ', i+1)
        for fields in arrOfFields:
            dict[fields] = input("Enter " + fields + " ->")
        list.append(dict)
# write to file
def writeToFile(list):
    with open('inputdata.json', 'w') as f:
            json.dump(list, f)
            f.write('\n')

# read from file
def readFromFile(id):
    with open('inputdata.json', 'r') as f:
        data = json.load(f)
        if id == 0 or id > len(data):
            print("Invalid user id")
        else:
            print(data[id-1])
       
addStudent(totalNumberOfStudents)
writeToFile(list)
idInput = int(input("enter id to retrive -> "))
readFromFile(idInput)


