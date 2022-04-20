
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.




def main():     #10 pts
    number=int(input('Enter number '))   #5 pts
    print(number)                        #5 pts
    result=primes(number)   #10 pts
    
    if result:
        print(number," is prime")       #10 pts
    else:
        print(number," is not prime")   #10 pts
    
def primes(n):              #10 pts
    for j in range (2,n):   #10 pts
        if n%j==0:          #10 pts
            break
    if n==j+1:              #10 pts
        return 1
    else:
        return 0
main()          #10 pts



