a=int(input('enter a number:-'))
b=int(input('enter b number'))
op=eval(input('enter a valid operator:- '))
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '//':
        print(a//b)
    case '%':
        print(a%b)
    case _:
        print('enter a valid operator')
