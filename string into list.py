s=input('enter a string :-')
i=0
out=[]
start=0
while i<len(s):
    if s[i]=='':
        if start<i:
            out+=[s[start:i]]
            start=i+1
    i+=1
if start<len(s):
    out+=[s[start:]]
print(out)