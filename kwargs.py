def func(a,b=0,*args,c=0,**kwargs):
    print(a,args,b,kwargs)
func(1,2,3,4,c=60,d=45)