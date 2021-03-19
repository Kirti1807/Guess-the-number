import random
print('You have to a choose a number from 1 to 100 and computer guess your choice')
print('if guessed number is low than your choice then give instruction L ,if high then give H , and if equal to your choice then give E ')
print('Computer have total 20 moves to guess your choice','\n')
moves = 20

low =1
high = 100
while moves > 0:
    guess = random.randint(low,high)
    print(f'compurt guess is {guess}')
    user = input("give instruction according to your choice : ")
    moves = moves-1
    if(user == 'E'):
        print('Wow!!  computer guess right number')
        print(f'computer guess your number in {20 - moves} moves \U0001F60D')
        break
    elif user == 'L' :
        low = guess +1
    elif user == 'H' :
        high = guess -1
    else :
        print("Wrong instruction \U0001F92A")
    print(f'compuer have {moves} remaining moves','\n')
if moves == 0 :
    print('oppsss computer have no remaining moves to guess your number \U0001F92A')

