s=eval(input('enter a number'))
if s in '0123456789':
    print('digit')
elif s>='A' and s<= 'Z':
    print('uppercase')
elif s>='a' and s<='z':
    print('lowercase')
else:
    print('special character')