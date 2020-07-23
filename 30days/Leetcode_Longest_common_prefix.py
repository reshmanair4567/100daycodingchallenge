def prefix(strs):
    strs.sort(key=lambda strs:len(strs))
    temp=strs[0]
    flag=True
    for i in range(len(strs)):
        for j in range(len(strs[0])):
            if temp[j]!=strs[i][j]:
                temp= temp[:j]
                flag=False
                break
    return temp


if __name__=="__main__":
    strs=["flow","flowerpot","flower"]
    print(prefix(strs))
