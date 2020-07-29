



# #anagram or not
# s="silent"
# l="listen"
# if len(s)!=len(l):
#     print("not an anagram")
# else:
#     if set(s)==set(l):
#         print("anagram")

#anagram or not
# s="silent"
# l="listen"
# if len(s)!=len(l):
#     print("not an anagram")
# else:
#     if sorted(s)==sorted(l):
#         print("anagram")


# #find indices of all substrings in a string 
# import re
# s="GeeksforGeeks forr Geeks"
# t="Geeks"
# l= [(m.start(),m.end()) for m in re.finditer(t,s)]
# print(l)
    
# find frequency of substring in a string
# import re
# s="GeeksforGeeks forr Geeks Geeks"
# t="Geeks"
# # res=s.count(t)
# # print(res)

# print(len(re.findall(t,s)))


# import re
# regex = r"([a-zA-Z]+) (\d+)"
# match = re.search(regex, "I was born on August 13 August 13 August 13  August 13  August 13") 
# print(match.group())
# # print(match.group(1))
# # print(match.group(2))

# regex=r"Error"
# # match=re.search(regex,"here is an Error")
# # print(match.start(),match.end())
# matching=re.findall(regex,"Here is an Error Error Error123")
# print(matching)

# rege = '\d+'
# mat=re.findall(rege,"here is 1 2 3 4 4 112112211")
# print(mat)

# li=['apple','rat']
# #print(sorted(li,key=len))
# li.sort(key=len)
# print(li)

# a=sorted(li,key=len)
# print(a)

# li=['appleeeeeee','mango','banana']
# li.sort(key=len)
# print(li)

# li=["flagssssss", "flower","flowerpot"]
# print(sorted(li,key=len))

# li=['abs','cat','rat']
# li.remove('abs')
# print(li)

#s="TACK"
# print(s[::-1]

# s="TACK"
# # str = "" 
# for i in s: 
#     print("i is:"+i)
#     str = i + str
#     print(str)
# print(str)

#s="TACK"
#l="".join(list(reversed(s)))
#print(l)

# s="TACK"
# s=list(s)
# s.reverse()
# print("".join(s))
