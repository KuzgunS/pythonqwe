
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.

def division(x,y):
    
    q=x//y
    r=x%y
    return q,r

def main():
    n1=int(input('Enter n1'))
    n2=int(input('Enter n2'))
    quotient , remainder = division(n1,n2)
    print(n1)
    print(n2)
    print(quotient)
    print(remainder)
    
main()



