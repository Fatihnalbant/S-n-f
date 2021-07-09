"""
Class öznitelikleri
"""

class Sample:
    def __init__(self):
        self.a = 10
        self.b = 20
        
s = Sample()
print(s.a, s.b)

k = Sample()
print(k.a, k.b)


# tarih

class Date: 
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def disp(self):
        print('{}/{}/{}'.format(self.day, self.month, self.year))
        


d=Date(12, 4, 1989)
d.disp()
    
