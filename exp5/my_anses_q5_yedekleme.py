#%% q1


from math import remainder
import random


def points(won,draw,lost):
    return (won * 3 + draw + lost * 0)


random.seed(1)
team_A =  {
    "name" : "team A",
    "win" : random.randrange(15,26), #btw 15-25
    "draw" : random.randrange(3,7), # btw 3-6
}
team_A ["lose"] =  30 - (team_A["win"] + team_A["draw"])

team_B =  {
    "name" : "team B",
    "win" : random.randrange(15,26), #btw 15-25
    "draw" : random.randrange(3,7), # btw 3-6
}
team_B ["lose"] =  30 - (team_B["win"] + team_B["draw"])

team_C =  {
    "name" : "team C",
    "win" : random.randrange(15,26), #btw 15-25
    "draw" : random.randrange(3,7), # btw 3-6
}
team_C ["lose"] =  30 - (team_C["win"] + team_C["draw"])

team_A["points"] = points(team_A["win"],team_A["draw"],team_A ["lose"])
team_B["points"] = points(team_B["win"],team_B["draw"],team_B ["lose"])
team_C["points"] = points(team_C["win"],team_C["draw"],team_C ["lose"])

# teams = [team_A , team_B, team_C] # listeyi dict'ten oluşturamıyon

teams = {
        "team A" : team_A,
        "team B" : team_B,
        "team C" : team_C
}

print(teams)
print("***")
print(teams["team A"])
print("***")
print(teams["team A"]["points"]) # oha işe yarıyo
print("devamm**************")
#
# # işe yaramıyor
# for team in teams[:]: 
#     for points in team["points"]:
#         print(points)
# 


# """
# for tms in teams.values():
#     for pts in tms.values():
#         print(pts["points"])
# """

for key in teams:
    print(teams[key]["name"], "'s point is:",teams[key]["points"],)

winner_team = "N/A"
winner_point = -1

for key in teams:
    if(teams[key]["points"] > winner_point):
        winner_team = teams[key]["name"]
        winner_point = teams[key]["points"]

print("champ of leauge is: {var1}\nchamp's point is: {var2}".format(var1 = winner_team, var2 = winner_point))





# %%

#q2 






import random


def points(won,draw,lost):
    return (won * 3 + draw + lost * 0)

def generate():
    return random.randrange(15,26), random.randrange(3,7) #return win and draw games

random.seed(1)
team_A =  {
    "name" : "team A",
}
team_A ["win"], team_A ["draw"] = generate()
team_A ["lose"] =  30 - (team_A["win"] + team_A["draw"])

team_B =  {
    "name" : "team B",
}
team_B ["win"], team_B ["draw"] = generate()
team_B ["lose"] =  30 - (team_B["win"] + team_B["draw"])

team_C =  {
    "name" : "team C",
}
team_C ["win"], team_C ["draw"] = generate()
team_C ["lose"] =  30 - (team_C["win"] + team_C["draw"])

team_A["points"] = points(team_A["win"],team_A["draw"],team_A ["lose"])
team_B["points"] = points(team_B["win"],team_B["draw"],team_B ["lose"])
team_C["points"] = points(team_C["win"],team_C["draw"],team_C ["lose"])

# teams = [team_A , team_B, team_C] # listeyi dict'ten oluşturamıyon

teams = {
        "team A" : team_A,
        "team B" : team_B,
        "team C" : team_C
}


for key in teams:
    print(teams[key]["name"], "'s point is:",teams[key]["points"],)

winner_team = "N/A"
winner_point = -1

for key in teams:
    if(teams[key]["points"] > winner_point):
        winner_team = teams[key]["name"]
        winner_point = teams[key]["points"]

print("champ of leauge is: {var1}\nchamp's point is: {var2}".format(var1 = winner_team, var2 = winner_point))




# %% q3

n1 = 7
n2 = 2


def division (num1,num2):
    quotient = num1 // num2
    remainder = num1%num2
    return quotient,remainder

print("quotient = {var1}\nremainder = {var2}" .format(var1 = division(n1,n2)[0], var2 = division(n1,n2)[1]) )



# %% q4

the_number_to_take_the_root_of = 225
tolerance = 10**(-8)

def root(num):
    x = 999 # x0 #iteration'ı bunla başlatıyoruz, o sonra buluyor.
    print(x)
    iters = 0
    while( abs(x - (num/x)) > tolerance):
        x = 1/2 * (x + num/x)
        iters += 1
        print(x)
    return x, iters # x is the root

(rt,itrs) = root(the_number_to_take_the_root_of)
print("number is:",the_number_to_take_the_root_of)
print("root is: {:.60f}".format(rt))
print("total iterations are:",itrs)

# %% q5 soruda repeat q4 demiş, q4'te verilen bir sayının
# sqrt si bulunurken burada anladığım kadarıyla geçen deneyde
# yapıldığı gibi fonksiyonun köklerini yani x eksenini kestiği 
# noktaları buluyoruz
from sympy import *

the_number_to_take_the_root_of = 0 # ????
tolerance = 10**(-8)

def root(num):
    x = 999 #x0 # iteration'ı bunla başlatıyoruz, o sonra buluyor.
    iters = 1
    print(x)
    while(True): # do while loop yapıldı aslında
        fx = x**2 - 11*x + 28 - num # - num kısmından emin değilim
        
        xx, y, z = symbols('x y z')
        init_printing(use_unicode=True)
        gx = diff( xx**2 - 11*xx + 28 - num, xx)
        gx = lambdify(xx, gx)
        gx = gx(x)

        x = x - (fx/gx)
        iters += 1
        print(x)

        if(abs( fx/gx ) < tolerance):
            break
    return x, iters # x is the root


(rt,itrs) = root(the_number_to_take_the_root_of)
print("number is:",the_number_to_take_the_root_of)
print("root is: {:.60f}".format(rt))
print("total iterations are:",itrs)
# %% q6

check_if_prime = 16335689

def primes(num):
    if ( (num <= 5) and (num != 1)  and  (num !=4) ) :
        return True        
    elif(num > 5):
        for n in range(2,( int(num**(1/2) +1) ),1):
            if(num%n == 0):
                return False
        return True
    else:
        return False

for num in range(1,100,1):
    if(primes(num)):
        print("number {} is prime".format(num))
  
print("****")
if (primes(check_if_prime)):
    print("number is prime")





# %% q7

factorize_this = 163352 #16335689prime # 163351prime #16335689  #3757208

def primes(num):
    if ( (num <= 5) and (num != 1)  and  (num !=4) ) :
        return True        
    elif(num > 5):
        for n in range(2,( int(num**(1/2) +1) ),1):
            if(num%n == 0):
                return False
        return True
    else:
        return False
        
dict = {}

def prime_factor(num):
    n = 2
    count = 0
    num_cpy = num
    while(n <= num_cpy ): # while(n < int(num**(1/2)) ):
        if( primes(n)): # eğer katsayı prime ise True döndürüp if içine giriyor
            # print(n) #!!!!!!!!!!!!!!
            if(num_cpy % n == 0):
                count += 1
                dict[n] = count
                num_cpy //= n
            else:
                n+=1
                count = 0
        else:
            n+=1
            count = 0

prime_factor(factorize_this)

print("factors are:")
for key in dict:
    for n in range(dict[key]):
        if(n == (dict[key] - 1) ):
            print("{}".format(key),end = '')
        
        else:
            print("{}*".format(key),end = '')

    if(key != (list(dict.keys())[-1] )): # if key isnt the last item put *
        print(" *",end = '')

# %% q8

N = 10

def find_gcd(num1,num2):
    gcd = 1

    min_of_them = min(num1,num2)
    if(min_of_them%2) == 0:
        max_divisor = min_of_them/2
    else:
        max_divisor = min_of_them//3


    for n in range(1,min_of_them+1,1):
        if(num1 % n == 0 and num2 % n == 0):
            gcd = n
        else:   
            continue
    
    return gcd

def make_gcd_table(n):
    print("   ",end="")
    for i in range(n):
        print("{:3}".format(i+1),end="")
    print()
    for r in range(n):
        print("{:3}".format(r+1),end="")
        for c in range(n):
            if(find_gcd(r+1,c+1) == 1):
                print("  *",end="")
            else:
                print("   ",end="")
        print()

make_gcd_table(N)



# %%
