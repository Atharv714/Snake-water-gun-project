# snake water gun
import random
import string

print('You will get 5 chances | Draw is not counted')


userPoints = 0
computerPoints = 0
range1 = 5

while True:
    for x in range(range1) : 
        userInput = str.lower(input('Choose from Snake, Water, Gun : '))

        listComputer = ['Snake', 'Water', 'Gun']
        computerChoice = str.lower(random.choice(listComputer))

        if (userInput == computerChoice) : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('It is a draw no points to anyone')
            range1 += 1
            print()
            
        if(userInput == 'snake' and computerChoice=='water') : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('You won')
            userPoints = userPoints+1
            print()

        if(userInput == 'snake' and computerChoice == 'gun') : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('Computer won')
            computerPoints = computerPoints+1
            print()
        
        if(userInput == 'water' and computerChoice == 'gun') : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('You won')
            userPoints = userPoints+1
            print()

        if(userInput == 'water' and computerChoice == 'snake') : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('computer won')
            computerPoints = computerPoints+1
            print()
        
        if(userInput == 'gun' and computerChoice == 'snake') : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('You won')
            userPoints = userPoints+1
            print()

        if(userInput == 'gun' and computerChoice == 'water') : 
            print()
            print(f'Computer Played : {computerChoice}')
            print('computer won')
            computerPoints = computerPoints+1
            print()
        
        if(computerPoints+userPoints == 5) : 
            break
    if(computerPoints+userPoints == 5) : 
        break

print()
print()
print(f'Your Score : {userPoints} | Computer Score : {computerPoints}')
print()
print()