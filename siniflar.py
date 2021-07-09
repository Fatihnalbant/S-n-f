"""
complex sayılarda class ile koymak

"""
class Complex:
    def set(self, r, i):
        self.r = r
        self.i = i
    
    def disp(self):
        print(f'{self.r}+{self.i}i')

              

z = Complex()
z.set(3, 2)
z.disp()


k = Complex()
k.set(7, 65)
k.disp()
