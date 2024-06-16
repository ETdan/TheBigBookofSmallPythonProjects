print("""
Bagels, a deductive logic game.
I am thinking of a 3-digit number. Try to guess what it is.
*********************************************
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
********************************************
You have 10 guesses to get it.""")

import random

x=list(map(int,str(random.randint(100,1000))))
guessCounter=1
answerFound=False
while guessCounter <11 and not answerFound:
    response=[]
    
    print(f'Guess #{guessCounter}:')
    currGuess= list(map(int,list(input())))
    
    if len(currGuess)!=3:
        print('tryagin. Your guess shoud have length of 3')
        guessCounter-=1
    else:
        for index,num in enumerate(currGuess):
            if num in x and index == x.index(num):
                response.append('Fermi')
            elif num in x:
                response.append('Pico')
                
        if not response:
            print('Bagels')
        elif len(response) == 3 and 'Pico' not in response:
            print('You got it!')
            answerFound=True
        else:
            print(response)
        
    guessCounter+=1
    
if not answerFound:
    print(x)
    print('Better luck Next Time :)')