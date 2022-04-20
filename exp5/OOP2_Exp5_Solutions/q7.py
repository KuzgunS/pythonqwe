
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.


def prime_factor(n):
    factor = 2
    while factor*factor <= n:
        while n % factor == 0:
            # Cast out and write factor.
            n = n//factor
            print(factor, ' ')
        factor = factor+1

    print(n) # en son kalanı yazdurıyor. Mantıklı ama en son 1 yazdırma durumu da var bu da if else ile kolayca halledilebilir

def main():
    x= 8 #  163351 # 163352 works # int(input('Enter number'))
    prime_factor(x)
    
main()