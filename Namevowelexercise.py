# name compatibility calculator
# two names as input
# take name length
#loop that counts all vowels
# validate name isnt numbers
# do maths
# write at least two procedures/methods




def getname(name):
    
    while True:
        if name.isdigit() == True:
            print("A name can't be numbers!")
            name = input("Enter valid name Name: ").upper()
        else:
            break
     
    return name   
    


def checkforvowels(name):
 
    vowels = ["A","E","I","O","U"]
    total = 0
    
    for i in name:
        for c in vowels:
            if i == c:
                total = total + 10

    return total


def findlength(name):
    
    l = len(name)

    return l


def calculatetotal(firstsum,secondsum):
    
    total = firstsum[0] + secondsum[0] + firstsum[1] + secondsum[1]
    
    if total >= 100:
        total = 100
                                                          
    return total


firstname = getname(input("Enter your name: ").upper())
secondname = getname(input("Enter lovers name: ").upper())

sumvowels = checkforvowels(firstname), checkforvowels(secondname)
sumlength = findlength(firstname), findlength(secondname)

print(str(calculatetotal(sumvowels,sumlength)) + "%")



