n = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
ans=[]
for ele in n:
    if ele%2==0:
        ans.append(ele)
print(ans)