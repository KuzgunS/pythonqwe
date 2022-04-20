
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.
EPSILON = 1e-15

def root(a):
    x_n=a
    i=0
    while abs(x_n - a/x_n) > EPSILON:    
        x_n=(a/x_n+x_n)/2.0
        i=i+1

    return x_n,i

def main():
    x=int(input('Enter x'))
    result, iteration = root(x)
    print(x)
    print(result)
    print(iteration)
    
main()



