#members = []

#while len(members) != 4:
 #   mem = input("Enter a name, enter 'done' when finished: ")
  #  members.append(mem)
#print(members)



def binarycalculator():

    decimal = 0
    check = False


    while check == False:
        binarynumber = input("Enter binary number: ") 
        for char in binarynumber:
            if char == "0" or char == "1":
                check = True
            else:
                check = False
                break
    
    binarymaxvalue = 1*2 ** (len(binarynumber) - 1)

    for x in binarynumber:
        if x == "1":
            decimal = decimal + binarymaxvalue
    
        binarymaxvalue = binarymaxvalue / 2;    


    return int(decimal)

def markgrade():
    mark = int(input("Enter your marks: "))
    
    if mark >= 85:
        print("Distinction")
    elif mark >= 65:
        print("Pass")
    else:
        print("Fail")

class Student:

    def _init_(student,name,mark):
        student.name = name
        #student.age = age
        #student.sclass = sclass
        student.mark = mark



def score():
    allstudents = []

    while len(allstudents) < 3:

        person = Student()
        person.name = input("Students Name")
        person.mark = int(input("Students Mark"))

        allstudents.append(person)
    
    total = 0
    for i in allstudents:
        total = total + i.mark
    
    total = total / 3
    print(total)
        

    
score()