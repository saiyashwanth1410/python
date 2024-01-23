def fact():
    num=int(input())
    i=1
    res=1
    while i<=num:
        res*=i
        i+=1
    print(res)
fact()