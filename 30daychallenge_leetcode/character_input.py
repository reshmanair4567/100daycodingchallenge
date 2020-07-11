
def years_later(name,age):
    ans=100-age
    print(("You will be 100 years in "+str(ans)+"years\n")*ans)

if __name__=="__main__":
    name=input()
    age=int(input())
    years_later(name,age)


