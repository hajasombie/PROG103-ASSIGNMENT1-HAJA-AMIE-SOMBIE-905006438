print("#"*80)
print("\t\t\t STUDENT RECORD MANAGEMENT SYSTEM ")
print("#"*80)


student_information = {
    20060:{"student_name":"George N'GoloMusa Kargbo","email":"ngolomusa@gmail.com","parent_phonenumber":"099999999","phone_number":"090990990","faculty":"FICT","program":"BSEM","class":"1202","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    29094:{"student_name":"Amie Sombie","email":"sombie001@gmail.com","parent_phonenumber":"090999078","phone_number":"080998907","faculty":"FICT","program":"DIT","class":"1202","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    30909:{"student_name":"Chris Effiong","email":"chris@gmail.com","parent_phonenumber":"030343567","phone_number":"033324536","faculty":"FICT","program":"DIT","class":"1201","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    98760:{"student_name":"Ensar Junior","email":"junior@gmail.com","parent_phonenumber":"090999078","phone_number":"088908976","faculty":"FICT","program":"DIT","class":"1203","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    56789:{"student_name":"Amadu Kamara","email":"amakan@gmail.com","parent_phonenumber":"090999034","phone_number":"077789056","faculty":"FICT","program":"DIT","class":"1201","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    90050:{"student_name":"Zaniab Barry","email":"barry@gmail.com","parent_phonenumber":"032456789","phone_number":"080345678","faculty":"FICT","program":"DIT","class":"1205","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    62399:{"student_name":"John Kamara","email":"kamara@gmail.com","parent_phonenumber":"033456789","phone_number":"033909876","faculty":"FICT","program":"DIT","class":"1201","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    11111:{"student_name":"Mohammed Kabie","email":"kabie@gmail.com","parent_phonenumber":"032123456","phone_number":"034567890","faculty":"FICT","program":"DIT","class":"1206","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    32591:{"student_name":"Angie Masalaki","email":"masalki@gmail.com","parent_phonenumber":"030303456","phone_number":"030456789","faculty":"FICT","program":"DIT","class":"1204","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
    64101:{"student_name":"Vandi Mohammed","email":"vandi@gmail.com","parent_phonenumber":"099345670","phone_number":"080998754","faculty":"FICT","program":"DIT","class":"1203","module":"1.PRINCIPLES OF SOFTWARE ENGINEERING.\n2.STRUCTURAL PROGAMMING.\n3.COMPUTERIZE MATHEMATICS.\n4.MULTIMEDIA.\n5.DATA COMMUNICATION.\n6.DATA BASE."},
}
def Admin_access(ID,name):
    admin_list={
        1234:{"name": "Amadu Kamara"},
        5678:{"name": "Elijah Fullah"},
        9012:{"name": "Engineer Kalokoh"},
        3456:{"name": "Osman Bah"},
        7890:{"name": "Santigie Kamara"},
        9876:{"name": "Amadu Kamara"},
    }
    if ID not in admin_list:
        return f" no data found for the name {name} and ID {ID}"
    login_name={}
    ask={}
    login_id=0
    if ID in admin_list:
       information=admin_list[ID]

       for pid, User in admin_list.items():
            if information["name"] == name:
             print (f"Lecturer name: {name} Lecturer ID: {ID}")
             print("do you want to search for a student ?: ")
             
            ask= input("enter yes or no: ").lower().strip()
            try:
              ask=int(ask)
              if ask == "yes":
                     break
              if ask == "no":
                  break
              if isinstance(ask,int):
                   print("not valid")
                   continue
              else:
                  break
            except ValueError:
                    pass
                 
            if ask == "yes":
                try:
                    login_name=input("enter the student name: ").title()
                    login_id=int(input("enter the student id : ") or 0)
                    login_name=int(login_name)
                    if isinstance(login_name,int) or len(login_name) <=0:
                        print("student name should be string")
                        continue

                except ValueError:
                    break
                
            elif ask=="no":
                 print("exiting now.\n good bye")
                 exit()
            else:
                  return "did not understand what you typed"
                 

            try:

                  login_id=int(login_id)
                  if isinstance(login_id,str) or login_id == 0:
                     print("the student id cannot be an integer !.")
                     continue
                  else:
                     break
            except ValueError:
                     break
    else:
        return "The information provided did not match what we have"

    if login_id in student_information:
                      student_info=student_information[login_id]["student_name"]
                      status1=student_information[login_id]["email"]  
                      status2=student_information[login_id]["parent_phonenumber"] 
                      status3=student_information[login_id]["phone_number"] 
                      status4=student_information[login_id]["faculty"] 
                      status5=student_information[login_id]["class"] 
                      status6=student_information[login_id]["module"]

                      for sid, name in student_information.items():
                        if student_info==login_name:
                          return f"student name: {login_name} \nstudent id: {login_id}  \nemail: {status1} \nphone number:{status3} \nfaculty:{status4} \nclass:{status5} \nmodule:{status6} \nparent phonenumber:{status2}"
                          
                        else:
                           return f"student name:{login_name} and \n ID:{login_id} is not in the list"
                     
                      else:
                        return f"no information entered {lecturer_name} and ID {lecturer_id} was not found"
    else:
        return "no input recieved"
                
    



login_name={}

login_id=int(input("enter id: ") or 0)
while True:
    try:
       
        if login_id == 0:
           print("no value input !")
        else:
            break
        
            
    except ValueError:
        print(f"only numerical values allowed !")
        

while True:
    login_name=input("enter your name: ").title().strip()
    try:
        number=int(login_name)
        if isinstance(number ,int):
            print(f"you entered a number {number}")
            continue
        else:
            break
    except ValueError:
             if len(login_name)<=0:
              print("no value entered")
              continue
             else:
                 break
         

if login_id in student_information:
    student_info=student_information[login_id]["student_name"]
    status1=student_information[login_id]["email"] 
    status2=student_information[login_id]["parent_phonenumber"] 
    status3=student_information[login_id]["phone_number"] 
    status4=student_information[login_id]["faculty"] 
    status5=student_information[login_id]["class"] 
    status6=student_information[login_id]["module"]

    for pid, name in student_information.items():
        if student_info==login_name:
            print(f"student name:{student_info} \nstudent id:{pid} \nemail:(status1) \nparentphone number:{status2}\nphone number:{status3} \nfaculty:{status4} \nclass:{status5} \nmodule:{status6}")
            exit()
        else:
            print(f"student name {login_name} is not in the list")
            break
else:
    print("student id is not correct")     


print("#"*80)
print("\t\t\t LOGIN FOR LECTURERS ")
print("#"*80)
lecturer_name={}
lecturer_id=0
next={}
while True:
    print("are you a lecturer?")
    next=input("answer yes or no: ").lower().strip()
    try:
        next=int(next)
        if isinstance(next, int):
         print(f"you entered{next} and its invalid")
         continue
    except ValueError:
        if next == "yes":
            break 
        elif next == "no":
          break
        else:
           continue
while True:
        if next == "yes":
            try:
                lecturer_name=input("enter name: ").title()
                number=int(lecturer_name)
                if isinstance(number,int):
                    print(f"you enter this {number} which is a number")
                    continue
            except ValueError:
                if len(lecturer_name)<=0:
                    print("no data entered")
                    continue
                else:
                    break

        elif next=="no":
               print("you entered no")

               print("exiting now")
               exit()
        else:
            print("data inputed")
            break

while True:
            try:
                lecturer_id=int(input("enter id: ")or 0)

                if isinstance(lecturer_id, int):
                    add=Admin_access(lecturer_id,lecturer_name)
                    print(add)
                    break
                else:
                    print("invalid input")
                    break
      
            except ValueError:
                print("string data type not allowed")





