import math 
AB=int(input())
BC=int(input())
x=str(round(math.degrees(math.atan2(AB,BC))))+'°'
print(x)