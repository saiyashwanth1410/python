def prime(a,i=2):
    if a==i:
        return 'prime'
    elif a%i==0:
        return 'not a prime'
    return prime(a,i+1)
print (prime(5))
def fib(a,b=0,c=1,out=[]):
    if c>=a:
        return out
    elif b==0:
        out+=(b,c)
    else:
        out+=(c,)
    return fib(a,c,b+c,out)
print(fib(100))