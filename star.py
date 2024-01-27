rows = int(input('enter number of rows :-'))
out =''
temp=''
for i in range(rows):
    for j in range(rows):
        if i in [0,rows-1,j,rows-j-1,temp] or j in [0,rows-1,temp]:
            out+='* '
        else:
            out+='  '
    out+='\n'
print(out)
    