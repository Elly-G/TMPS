# prototype
class Location:
    district = ''
    city = ''
    street = ''

    def __init__(self ,district = '', city = '', street = ''):
        self.district = district
        self.city = city
        self.street = street    

class Atm:
    location : Location
    currencyCode = int
    maximumAmount = int

    def __init__(self, location:Location, currencyCode:int, maximumAmount:int):
        self.location = location
        self.currencyCode = currencyCode
        self.maximumAmount = maximumAmount

    def copyWithCurrencyCode(self, currencyCode):
        return Atm(self.location, currencyCode, self.maximumAmount)

    def clone(self):
        return Atm(self.location, self.currencyCode, self.maximumAmount)
    
class Places :
    atm = Atm

atm1 = Atm('Chisinau', 12, 322)
atm2 = atm1.copyWithCurrencyCode(21)
atm3 = atm2.clone()

print(atm1.currencyCode)
print(atm2.currencyCode)
print(atm3.currencyCode)
