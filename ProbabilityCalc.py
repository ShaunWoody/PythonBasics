import random


class Ball:

    def __init__(self,number,colour):
        self.number = number
        self.colour = colour

      


def findtotal(allballs):
    total = 0
    for i in allballs:
        total += i.number
    return total    

def pick(allballs):
    
    choice = input("Pick colour: ").lower()
    
    for i in allballs:
        
        if choice == i.colour.lower():
            i.number = i.number - 1

def probability(allballs):
    total = findtotal(allballs)
    
    for i in allballs:
        
       chance = i.number / total
       print(i.colour,i.number,chance)

def create_random(allballs):
    addcat = random.randint(1,4)
    count = 0
    while len(allballs) < addcat:
        number = random.randint(1,10)
        
        colour = ["Yellow","Red","Blue","Green"]
        addvalue = list((Ball(number,colour[count]),))
        allballs = allballs + addvalue
        count += 1
    return allballs




def Main():
    
   
    allballs = []
    allballs = create_random(allballs)
    
    
    while True:
        probability(allballs)
        pick(allballs)

        print(findtotal(allballs))


Main()