import json
from collections import Counter

with open("/Users/reshmanair/PycharmProjects/100daycodingchallenge_Leetcode/30daychallenge_leetcode/birthdays.json",'r') as f:
    birthdays=json.load(f)
    number_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}
months=[]
for name,birthday_string in birthdays.items():
    month=int(birthday_string.split("/")[0])
    months.append(number_to_string[month])
print(Counter(months))

'''
inp=input("enter the month")
d={"january":1,"february":3,"august":5}
for i,v in d.items():
    if inp==i:
        print(" we have {} birthdays in {}".format(v,i))
 '''   

