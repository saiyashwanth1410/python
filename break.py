a=input(   )
a[-1:len(a):-1] 
i=0
while i<len(a):
    if a[i] not in a[i+1:]:
        print(a[-i])
        break
    i+=1