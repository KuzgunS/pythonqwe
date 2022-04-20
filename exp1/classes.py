

import random


class Coin: # simulates a coin that can be flipped
    

    def __init__(self): # the __init__ method initializes the __sideup data attribute with 'heads'
        self.__sideup = 'Head'

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            
    
    def get_sideup(self):
        return self.__sideup
    

def main(): # defined a main func
    my_coin = Coin() # create an object from the Coin class
    
    print('The init side up is:', my_coin.get_sideup())
    
    #toss coin
    print("I'm gonna toss the coin 10 times and print their side ups:\n")
    for count in range(10):
        my_coin.toss()
        print(count,"-",my_coin.get_sideup())

main()        
    







