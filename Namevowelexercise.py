def getname():
    
    while True:
        firstname = input("Enter first name: ").upper()
        if firstname.isdigit() == True:
            print("Your name can't be numbers!")
        else:
            break

    
    while True:
        secondname = input("Enter second name: ").upper()  
        if secondname.isdigit() == True:
            print("Your name can't be numbers!")
        else:
            break
     
    return firstname,secondname      
    



def checkforvowels(nameone,nametwo):
 
    vowels = ["A","E","I","O","U"]
    totalone = 0
    totaltwo = 0

    for i in nameone:
        for c in vowels:
            if i == c:
                totalone = totalone + 3
    
    for i in nametwo:
        for c in vowels:
            if i == c:
                totaltwo = totaltwo + 3

    return totalone, totaltwo

def findlength(nameone,nametwo):
    
    l1 = len(nameone)
    l2 = len(nametwo)

    return l1,l2

def calculatetotal(firstsum,secondsum):
    
    total1 = firstsum[0] + secondsum[0]
    total2 = firstsum[1] + secondsum[1]

    return total1,total2



 

firstname,secondname = getname()
sumvowels = checkforvowels(firstname,secondname)
sumlength = findlength(firstname,secondname)
print(calculatetotal(sumvowels,sumlength))



