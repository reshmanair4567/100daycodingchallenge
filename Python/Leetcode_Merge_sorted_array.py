a=[1,2,3,0,0,0]
m=3
b=[2,4,5]
n=3

a=sorted(a[:m]+b)
print(a)

if a[:] is a:
    print("false")
else:
    print("not the same")

#print(a[:])

