def even(value):
    flag=False 
    if value%2==0:
        flag=True 
    return flag 
def sqadd(a,b):
    return a**2+b**2 
def add(a,b): 
    return a+b 
def indexvalue(li):
    out=[] 
    for i in range(len(li)):
        if even(i) and even(li[i]):
            out+=[sqadd(i,li[i])] 
        elif even(i) and even(li[i]):
            out+=[sqadd(i,li[i])] 
        else:
            out+=[add(i,li[i])]
    return out
print(indexvalue([2,4,9,7,11,2,4,3,5,7,6]))