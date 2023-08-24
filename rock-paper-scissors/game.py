# So in this game of rock paper scissors what we are gonna do is we gonna take two inputs. i.e one from the user and another from the computer. Then we are gonna compare both the inputs and give the result accorinf to - 
#Rock  >  Scissors - Win
#Scissors  >  paper - Win
#Paper  >  Rock - Win

import random

def play():
    user = input("Hello user! What are you gonna choose - Rock(r) , Paper(p) , Scissors(s) ")
    computer = random.choice(['r','p','s'])

    if(user == computer):
        return f"Its a tie against computer as the computer choose {computer} "

    if(is_win(user,computer)):
        return f"You won against computer as the computer choose {computer} "
    return f"You lost against computer as the computer choose {computer} "

def is_win(player , opponent):
    if((player=='r' and opponent == 's') or (player=='s' and opponent == 'p') or (player=='p' and opponent == 'r')):
        return True
    
print(play())