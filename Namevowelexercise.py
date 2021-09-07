def checkforvowels(nameone,nametwo):
    
    totalone = 0
    totaltwo = 0
    
    vowels = ["a","e","i","o","u"]
    
    totalone = totalone + len(nameone)
    totaltwo = totaltwo + len(nametwo)

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
    
totalone,totaltwo = checkforvowels(input("Name one"),input("Name two"))


#print(checkforvowels(input("Name one"),input("Name two")))


