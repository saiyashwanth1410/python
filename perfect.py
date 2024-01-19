num=int(input('enter a number :-'))
n1=0
n2=1
i=1
count=0
while i<=num:
    count=n1+n2
    n1=n2
    n2=count
    i+=1
    print(count)   