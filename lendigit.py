def length():
    a=int(input())
    b=str(int(a))
    i=0
    count=0
    while i <len(b):
        if b[i] in '0123456789':
            count=count+i
        i+=1
    print(count)
length()