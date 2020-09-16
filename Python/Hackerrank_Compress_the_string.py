# from itertools import groupby
# input=input()
# for k, g in groupby(input):
#     print("({}, {})".format(len(list(g)), k), end=" ")


from itertools import groupby
input=input()
for k,g in groupby(input):
    print("{}{}".format(k,len(list(g))),sep="",end="")
print("\n")