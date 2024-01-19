user=input('enter username')
password=input('enter password')
bd={'user':'password'}
a=bd['username'] 
b=bd['password']
if (a,b) in bd:
    print('matching')
else:
    print('not matching')