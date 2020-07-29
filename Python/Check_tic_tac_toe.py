def vertical(block):
    for i in range(len(block)):
        result=0
        flag=False
        for j in range(len(block[i])):
            result+=block[j][i]
            if block[j][i]==0:
                flag=True
        print(result)
        pc=winner(result,flag)
        if pc==True:
            return pc

def horizontal(block):
    
    for i in range(len(block)):
        result=0
        flag=False
        for j in range(len(block[i])):
            result+=block[i][j]
            if block[i][j]==0:
                flag=True
        print(result)
        pc=winner(result,flag)
        if pc==True:
            return pc


def diagonal(block):
    result=0
    flag=False
    for i in range(len(block)):
        for j in range(len(block[i])):
            if i==j:
                result+=block[i][j]
                if block[i][j]==0:
                    flag=True
    pc=winner(result,flag)
    if pc==True:
        return pc
def diagonalreverse(block):
        result=0
        flag=False 
        i=0
        j=len(block)-1
        result=0
        for x in range(len(block)):
            result+=block[i][j]
            if block[i][j]==0:
                flag=False
            i=i+1
            j=j-1 
        pc=winner(result,flag)
        if pc==True:     # telling the code that iterate through the loop if pc (flag) is False
            return pc

def winner(result,flag):
    if result==3 and flag==False:
        print("player 1 wins")
        return True
    elif result==6:
        print("player 2 wins")
        return True
    

if __name__=="__main__":
    block=[
    [1,2,0],
	[1,2,0],
	[2,2,0]]


    if vertical(block) or horizontal(block) or diagonal(block) or diagonalreverse(block):
        exit()
    else:
        print("No one wins")


