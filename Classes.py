class Vowels:
    
    def __init__(self,word,allvowels):
        self.allvowels = allvowels
        self.word = word
        
    
    def checkforvowels(self):
        for i in self.word:
            for c in self.allvowels:
                if c == i:
                    return True
        
word1 = Vowels(input("Input string: ").upper(),"AOEUI")


print(word1.checkforvowels())

