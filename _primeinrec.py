def prime(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count+=1
        i+=1
    if count==2:
        return
print(prime(4))
