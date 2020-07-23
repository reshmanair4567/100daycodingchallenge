'''Two Sum'''
print("LEETCODE - TWO SUM")

nums=[2,7,9,11,13]
target=9
seen={}
for i,v in enumerate(nums):
    n=target-v
    if n not in seen:
        seen[v]=i
    else:
        print (seen[n],i)

'''reverse integer'''
print("LEETCODE-REVERSE INTEGER")
nums=int(input())
temp=abs(nums)
reverse=0
while temp!=0:
    reverse=reverse*10+temp%10
    temp=temp//10
if nums>1:
    print(reverse)
else:
    print(-1*reverse)


'''Palindrome Number'''
print("LEETCODE - Palindrome Number")
def palindrome(nums):
    if nums<0:
        return False
    else:
        temp=abs(nums)
        reverse=0
        while temp!=0:
            reverse=reverse*10+temp%10
            temp=temp//10
        return(reverse==nums)

if __name__=="__main__":
    nums=int(input())
    print(palindrome(nums))

'''Roman to Integer'''
print("LEETCODE - Roman to Integer")
def roman_to_int(strs):
    values={"I":1,"V":5,"X":10,"C":50,"L":100,"M":1000}
    integer=0
    for i in range(len(strs)):
        if i+1<len(strs) and values[strs[i]]<values[strs[i+1]]:
            integer+=values[strs[i+1]]-strs[s[i]]
            i+=2
        else:
            integer+=values[strs[i]]
            i+=1
    return(integer)


if __name__=="__main__":
    strs=input()
    print(roman_to_int(strs))

'''Longest Common Prefix'''
print("LEETCODE - Longest Common Prefix")
def prefix(strs):
    strs.sort(key=lambda strs:len(strs))
    temp=strs[0]
    for i in range(len(strs)):
        for j in range(len(strs[0])):
            if temp[j]!=strs[i][j]:
                temp=temp[:j]
    return temp

if __name__=="__main__":
    strs=["flow","flowerpot","flower"]
    print(prefix(strs))

''' Valid Paranthesis'''
print("LEETCODE - Valid Paranthesis")
def paranthesis(strs):
    values={"(":")","{":"}","[":"]"}
    seen=[]
    for ele in strs:
        if ele in values:
            seen.append(ele)
        elif seen and values[seen[-1]]==ele:
            seen.pop()
        else:
            return False
    
    return (len(seen)==0)

if __name__=="__main__":
    strs="{}("
    print(paranthesis(strs))




