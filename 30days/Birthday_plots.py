from bokeh.plotting import figure, show, output_file
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

m=Counter(months)
x=list(m.keys())
print(x)
y=list(m.values())
print(y)
output_file("plot.html")
x_categories=["January","February","March","April","May","June","July","August","September","October","November","December"]
p=figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)
show(p)


