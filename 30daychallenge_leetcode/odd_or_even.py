def odd_or_even(number):
    number=int(number)
    if number%2==0:
        if number%4==0:
            print("divisible by 4")
        else:
            print( "even")
    else:
        print("odd")

if __name__=="__main__":
    number="4"
    odd_or_even(number)
