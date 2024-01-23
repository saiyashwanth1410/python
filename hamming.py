def func(a,b):
    if len(a)==len(b):
        i=0
    c=0
    while i<len(a):
        if not a[i]==b[i]:
            c+=1
        i+=1
    else:
        print('enter valid string')
        print(c)
func('abcde','abcde')
func('strong','string')
func('pil','lip')