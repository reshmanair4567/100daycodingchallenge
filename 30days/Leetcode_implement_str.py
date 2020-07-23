haystack=""
needle = ""
h=len(haystack)
n=len(needle)

for i in range(h-n):
    if haystack[i:i+n]==needle:
        ans=i
    else:
        ans=-1
print(ans)


# if needle in haystack:
#     ans=haystack.index(needle)
# else:
#     ans=-1
# print(ans)
