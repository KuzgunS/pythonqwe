
# Accept integer n as a command-line argument. Write to standard
# output the prime factors of n.
import random

def points(x,y,z):
    return 3*x+y

def generate():
    w=random.randint(15,25)
    d=random.randint(3,6)
    l=30-(w+d)
    return w,d,l

def main():
    w,d,l=generate()
    pa = points(w,d,l)
    w,d,l=generate()
    pb = points(w,d,l)
    w,d,l=generate()
    pc = points(w,d,l)

    print(pa)
    print(pb)
    print(pc)
    
    if pa>pb and pa>pc:
        print("Champ A")
    if pb>pa and pb>pc:
        print("Champ B")
    if pc>pa and pc>pb:
        print("Champ C")
    
main()



