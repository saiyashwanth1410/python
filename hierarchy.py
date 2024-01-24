class MTCA:
    chairman='saiyashwanth'
    location='palamaner'
    college='MTCA'

    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile

class MCA(MTCA):
    principal='sandhya suresh '
    strength =500
    staff    =10

class Btech(MTCA):
    principal='sudharshan '
    strength =1000
    staff    =100

sushma=MCA('sushma',6305658968)
chintu=Btech('chintu',9505413199)
