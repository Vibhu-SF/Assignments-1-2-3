import studentMod as s  

manager = s.Stud() # creating object of stud class from student module

while 1:
    option = int(input("enter '1' for options or '0' to exit application -> \n"))
    if option == 1:
        option2 = int(input( ''' enter '1' to add record or 
 enter '2' to retrive record or 
 enter '3' to delete the record  \n'''))
        if option2 == 1:
            manager.addData()
        elif option2 == 2:
            manager.displayData()
        elif option2 == 3:
            manager.deleteRecord()
            print("### record deleted ###")
        else:
            print("### invalid input ###\n")            
    elif option == 0:
        break
    else:
         print("### invalid input ###\n")             