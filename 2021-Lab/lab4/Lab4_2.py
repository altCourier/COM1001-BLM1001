class CharFinder:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def commonWords(self):
        return set(self.s1) & set(self.s2)
         
    def unique_one(self):
        return set(self.s1) - set(self.s2)

    def unique_two(self):
        return set(self.s2) - set(self.s1)
    
finder = CharFinder("Cihan", "Sulh")
print(finder.commonWords())
print(finder.unique_one())
print(finder.unique_two())


