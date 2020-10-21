import random
from hangmanParts import parts
from time import sleep
#Creating series of word to guessed
words = ['python', 'programming', 'hello', 'welcome', 'name', 'gender', 'knowledge' ]
#Picking word at random [python]
picked = random.choice(words)
print('The word has', len(picked), 'letter')#Displays the length of the word
right = ['_'] * len(picked)#Displays an underscore times the lenght of the picked word
wrong = []
def update():
    for i in right:
        print(i, end = ' ')
    print()
print('Let me think of a word....')

'''Function that will wait in number of seconds for the console to think of the word selected
 by by the console at random.
'''
def wait():
    for i in range(5):
        print('.', end = '') 
        sleep(.5)       
    print()
#calling of functions
wait()
update()
parts(len(wrong))
while True:
    print('')
    print('===============================================================================')
    guess = input("Guess a letter: ")
    print('Let me check....')
    wait()
    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index += 1
        update()
    else:  
        if guess not in wrong:
            wrong.append(guess)
            parts(len(wrong))
        else:
            print('You already guessed that') 
        print(wrong)
    if len(wrong) > 7:
        print('You are hanged!!!')
        sleep(.9)
        print('You loose!')
        sleep(1.0)
        print('I picked', picked)
        break
    if '_' not in right:
        sleep(1.5)
        print('You win!')
        break