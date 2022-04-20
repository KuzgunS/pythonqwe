
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.

import math


def main():                              #10 pts
    number=int(input('Enter number '))   #5 pts
    print(number)                        #5 pts
    primes(number)                       #10 pts
    
def primes(n):                          #10 pts
    for i in range(1, n+1):
        print(i,"",end='')              #5 pts
    print()
    for i in range(1, n+1):             #10 pts
        for j in range(1, n+1):         #10 pts
            if math.gcd(i,j)==1:        #5 pts
                print("* ",end='')      #5 pts
            else:                       #5 pts
                print("  ",end='')      #5 pts
        print(i)                        #5 pts
            
main()                                  #10 pts
