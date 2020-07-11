def vertical(block):
    for i in range(len(block)):
        result=0
        for j in range(len(block[i])):
            result+=block[j][i]
        if result==3 and block[j][i]!=0:
            print("player 1 wins Vertical")
            return True
        elif result==6:
            print("player 2 wins Vertical")
            return True

def horizontal(block):
    
    for i in range(len(block)):
        result=0
        flag=False
        for j in range(len(block[i])):
            result+=block[i][j]
            if block[i][j]==0:
                flag=True
        if result==3 and flag==False:
            print("player 1 wins Horizontal")
            return True
        elif result==6:
            print("player 2 wins Horizontal")
            return True

def diagonal(block):
    result=0
    flag=False
    for i in range(len(block)):
        for j in range(len(block[i])):
            if i==j:
                result+=block[i][j]
                if block[i][j]==0:
                    flag=True
    if result==3 and flag==False:
        print("player 1 wins Diagonal")
        return True
    elif result==6:
        print("player 2 wins Diagonal")
        return True
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
        if result==3 and flag==False:
            print("player 1 wins Diagonal reverse")
            return True
        elif result==6:
            print("player 2 wins Diagonal reverse")
            return True

if __name__=="__main__":
    block=[
    [2,2,2],
	[0,2,0],
	[2,2,0]]

    if vertical(block) or horizontal(block) or diagonal(block) or diagonalreverse(block):
        exit()


