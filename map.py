a=[2,8,6,4,3,23,2,1,8,9]
def cube(n):
    if n%2==0:
        return n**3
    else:
        return   
print(list(filter(cube,a)))
print(list(filter(lambda n:n**3,a)))
