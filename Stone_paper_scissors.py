import random

def game(player1,player2):
    if player1==player2:
        return None
    elif player1=='S':
        if player2=='P':
            return True
        elif player2=='SS':
            return False
    elif player1=='P':
        if player2=='SS':
            return True
        elif player2=='S':
            return False
    elif player1=='SS':
        if player2=='P':
            return False
        elif player2=='S':
            return True

randNum=random.randint(1,3)
if randNum==1:
    player1="S"
elif randNum==2:
    player1="SS"
elif randNum==3:
    player1="P"

    
    

name=input("Enter Your Name:")

print(" Computer has taken Stone (S),  Paper(P) , Scissors(SS)   ?:")
player2=input("You Turn---->Stone (S),  Paper(P) , Scissors(SS)   ?:")
winner= game(player1,player2)

print(f"Computer choosed {player1}")
print(f"{name} choosed {player2}")

if winner == None:
    print("Opppss!!! Its a Tie")
elif winner:
    print(f"Congratulation You Win {name}")
else:
    print("Opppssssss! Sorry You Loss the match Better Luck Next Time")

