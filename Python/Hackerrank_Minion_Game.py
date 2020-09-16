def minion_game(string):
    # your code goes here
    kscore=0
    sscore=0
    vowels=["A","E","I","O","U"]
    for i in range(len(string)):
        if string[i] in vowels:
            kscore+=len(string)-i
        else:
            sscore+=len(string)-i
    
    if kscore>sscore:
        print("Kevin "+str(kscore))
    elif kscore==sscore:
        print("Draw")
    else:
        print("Stuart "+str(sscore))

        
if __name__ == '__main__':
    s = input()
    minion_game(s)