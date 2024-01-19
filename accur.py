s=input('enter a string :-')
out={}
for chr in s :
    if not (chr in out):
        out[chr]=1
    else:
        out[chr]+=1
print(out)
