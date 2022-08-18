import collegeClass as cc

manager = cc.college()
print("#### WELCOME USER ####")

while 1:
    option = int(input("enter '1' for options or '0' to exit application -> \n"))
    if option == 1:
        option2 = int(input( ''' enter '1' to add record or 
 enter '2' to retrive record or 
 enter '3' to delete the record  
 enter '4' to get clg details\n'''))
        if option2 == 1:
            manager.addData()
        elif option2 == 2:
            manager.displayData()
        elif option2 == 3:
            manager.deleteRecord()
            print("### RECORD DELETED ###")
        elif option2 == 4:
            manager.getCollegeDetails()    
        else:
            print("### INVALID INPUT ###\n")            
    elif option == 0:
        print("#### BYE BYE USER ####")
        break
    else:
         print("### INVALID INPUT ###\n")   