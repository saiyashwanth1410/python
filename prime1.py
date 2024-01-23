class mtca:
    princpal='Prabhakar'
    college='MTCA'
    location='Palamaner'
    def __init__(self,name,mobile,email,sem):
        self.name=name
        self.mobile=mobile
        self.email=email
        self.sem=sem

        def update_mob(self,new):
            self.mobile =new
            print('mobile number updated')
        @classmethod
        def change_principal(cls,new):
            cls.principal=new
        @staticmethod
        def add(a,b):
            return a+b
            
sai=mtca('saiyashwanth','123456789','saiyashwanth1410@gmail.com','1')