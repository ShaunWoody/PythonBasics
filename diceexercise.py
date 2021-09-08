import dice



def randomthrow():
    
    d = dice.diceroll()
    
    return d

for x in range(0,dice.howmanythrows(),1):
    print(randomthrow())