import sys
import random 
import time


responses = ["It is certain", "Not good", "Possible","Not possible", "Not Sure","Better not tell you now","Don't count on it.",
"Most likely.","Without a doubt.", " Yes – definitely.","You may rely on it."]

def ansquery() :
    print(input('Ask and you shall receive : '))
    print('Let me think!!')
    time.sleep(2)
    print(random.choice(responses))
    print("\n")


ansquery()     

restart = input('Do you want to play again (Y/N) ?')

while restart == str('Y') :
    ansquery()
    restart = input('Do you want to play again (Y/N) ?')
else :
    print('Okay Bye')    