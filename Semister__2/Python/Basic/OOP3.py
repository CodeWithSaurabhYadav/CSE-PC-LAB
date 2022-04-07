class sample:
    x = 2
    def get(self,y):
        self.y = y
        
S1 = sample()
S1.get(23)
print(S1.x,S1.y)

S2 = sample()
S2.y = 4
print(S2.x,S2.y)
print(S1.x,S2.y)