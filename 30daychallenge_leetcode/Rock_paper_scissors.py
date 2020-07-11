

while True:
    player1=input("Enter your value")
    player2=input("Enter your value")
    if player1=="Quit" or player2=="Quit":
        break
    else:

        if player1=="Rock":
            if player2=="Scissors":
                print("player1 wins!")
            elif player2=="Rock":
                print("play again")
            elif player2=="Paper":
                print("player2 wins!")
        elif player1=="Scissors":
            if player2=="Scissors":
                print("play again")
            elif player2=="Paper":
                print("player1 wins!")
            elif player2=="Rock":
                print("player2 wins!")
        elif player1=="Paper":
            if player2=="Paper":
                print("Play again")
            elif player2=="Rock":
                print("player1 wins!")
            elif player2=="Scissors":
                print("player2 wins!")
        




