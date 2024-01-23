def toggle():
    a='hello'
    i=0
    out='_'
    while i<len(a):
        if 'a'<=a[i]<'z':
            out+=chr(ord(a[i])-32)
        else:
            out+=a[i]
            