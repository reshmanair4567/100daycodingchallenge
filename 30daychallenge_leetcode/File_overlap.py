
one=open("/Users/reshmanair/PycharmProjects/100daycodingchallenge_Leetcode/30daychallenge_leetcode/text1.txt",'r')
text=one.read()
text=text.replace("\n"," ")
text=text.split()

with open("/Users/reshmanair/PycharmProjects/100daycodingchallenge_Leetcode/30daychallenge_leetcode/Other_file.txt",'r') as two:
    twoo=two.read()
    twoo=twoo.replace("\n"," ")
    twoo=twoo.split()

ans=[]
for i in text:
    if i in twoo:
        ans.append(i)

print(ans)
print(len(ans))


one.close()

