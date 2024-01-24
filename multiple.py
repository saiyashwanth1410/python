class Add:
    @staticmethod
    def add2(a,b):
        return a+b
    
    @staticmethod
    def add3(a,b,c):
        return a+b+c
class sub:
    @staticmethod
    def  sub2(a,b):
        return a-b
    
class mul:
    @staticmethod
    def mul2(a,b):
        return a*b
    
class cal(Add,sub,mul):
    pass

obj=cal()
print (obj.add2(3,4))
print (obj.add3(1,2,3))
print (obj.sub2(6,2))
print (obj.mul2(2,3))