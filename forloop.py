a="username@123#admin"
out=''
for chr in a:
    if not '0'<=chr<='9':
        out+=chr
print(out)