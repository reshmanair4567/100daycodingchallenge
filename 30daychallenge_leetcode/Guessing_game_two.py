from random import randint 
#my_number=int(input())
#print("my_number is"+str(my_number))
program_number=randint(0,100)
print(program_number)
counter=0
a=0
b=100
while True:
    my_response=input("Is your number Low,High or Same as program number: ")
    if my_response=="Exit" or my_response=="Correct":
        break
    else:
        if my_response=="High":
            a=program_number+1
            program_number=randint(a,b)
            print(program_number)
            counter+=1
        elif my_response=="Low":
            b=program_number-1
            program_number=randint(a,b)
            print(program_number)
            counter+=1
        else:
            print("Invalid input")

print("count is:   "+str(counter))
        



















'''
from random import randint
my_num=int(input("Enter your number"))
n=100
random_guess=randint(0,n)
result=input("please let us know the input")
while True:
    if str(my_num)=="Exit" or result=="Correct":
        break
    else:
        if result=="High":


        elif result=="Low":
        
        else:
            break
            


from random import randint
def guessinggame(my_num):
    result=""
    while True:
        if str(my_num)=="Exit" or result=="Correct":
            break
        else:
            counter=0
            random_guess=randint(0,100)
            if random_guess>my_num:
                result="too high"
                print(result)
                counter+=1
            elif random_guess<my_num:
                result="too low"
                print(result)
                counter+=1
            else:
                print("Correct")

    print(counter)
if __name__=="__main__":
    my_num=int(input("Enter your number"))
    guessinggame(my_num)

'''