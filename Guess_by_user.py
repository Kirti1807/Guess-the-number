import random
n = random.randint(1,100)
print('you have to guess a number in between 1 to 100 which is selected by computer')
print('You have total 20 moves to guess number')
print('\n')
moves =20
while(moves > 0):
    guess = int (input("Tell your guess"))
    moves = moves-1
    if(guess == n):
        print('Wow!! you guess corect number')
        print(f'You guess this number in {20 - moves} moves \U0001F60D')
        break
    elif guess < n :
        print('Your guess is too low guess another number')
    elif guess > n :
        print('Your guess is too high guess another number')
    
    print(f'Your remaining moves are {moves}','\n')
if moves == 0 :
    print('oppsss , You lose this turn \U0001F92A' )
    print(' no moves remain \U0001F92A')
#print("\U0001F60D")
#print("\U0001F92A")
