#%%
#q1

x = 2
sum_bottom = 1
sum_top = 7
sum = 0
factorial = 1

for n in range(sum_bottom,sum_top+1,1):
    for k in range(1,n+1,1):
        factorial *= k
    sum_term =   ((-1)**(n+1)) * (x**(n)) / factorial
    sum += sum_term
    factorial = 1 
    print(sum_term)

print("sum ={:.2f}".format(sum))



#%%
#q2

given_base = 2
num_in_given_base = 1001
num_in_given_base_cpy = num_in_given_base
digit_cnt = 1

while (num_in_given_base_cpy // 10) != 0:
    num_in_given_base_cpy //= 10
    digit_cnt += 1
print(digit_cnt)


num_in_given_base_cpy = num_in_given_base
decimal_equivalent = 0
for n in range(0,digit_cnt,1):
    decimal_equivalent += (num_in_given_base_cpy % 10) * given_base**n
    num_in_given_base_cpy //= 10
print(decimal_equivalent)

# %% better q2


given_base = 2
num_in_given_base = 111
num_in_given_base_cpy = num_in_given_base
digit_cnt = 1
n = 0
decimal_equivalent = 0

while ((num_in_given_base_cpy*10) // 10) != 0:
    decimal_equivalent += (num_in_given_base_cpy % 10) * given_base**n
    num_in_given_base_cpy //= 10
    n += 1
print(decimal_equivalent)
    

# %% q3

num1 = 100
num2 = 52
gcd = 1

min_of_them = min(num1,num2)
if(min_of_them%2) == 0:
    max_divisor = min_of_them/2
else:
    max_divisor = min_of_them//3
print(max_divisor)


for n in range(1,min_of_them+1,1):
    if(num1 % n == 0 and num2 % n == 0):
        gcd = n
    else:   
        continue

print("gcd is:{:.2f}".format(gcd))

# %% q4

x = 1.5708
threshold = 0.0000000000000001
cosx = 0
term = threshold + 1 #summed just so term is always greater than threshold at the beginning
the_power = 0
is_positive = True
factorial = 1



while( abs(term) > threshold):
    for k in range(1,the_power+1,1):
        factorial *= k
    if(is_positive):
        term = (x ** the_power) / factorial
        is_positive = not is_positive
    else:
        term = -1 * (x ** the_power) / factorial
        is_positive = not is_positive
    cosx += term    
    the_power += 2
    factorial = 1

print("the result is= {:0.15f}".format(cosx))



# %% q5

number = 76
number_squared = number ** 2
print("squared number is= {:8}".format(number_squared))
number_squared_cpy = number_squared
digit_cnt = 1

while (number_squared_cpy // 10) != 0:
    number_squared_cpy //= 10
    digit_cnt += 1
print("the number contains:{:5} digits".format(digit_cnt))


if(digit_cnt % 2 == 0): 
    right_half = number_squared % (10 ** (digit_cnt / 2))
    print("right half of the number squared is: {}".format(right_half))
else:
    raise Exception("the squared number doesn't have even numbered digits so half of it can't be determined")

if(right_half == number):
    print("number {:5} is Automorphic!!!".format(number))
else:
    print("number {:5} is not Automorphic :((".format(number))


# %% q6 #d0 is msb

bank_acc_num = 4444   #27327
bank_acc_num_cpy = bank_acc_num
digit_cnt = 1

while (bank_acc_num_cpy // 10) != 0:
    bank_acc_num_cpy //= 10
    digit_cnt += 1
print("the bank account contains: {} digits".format(digit_cnt))

bank_acc_num_cpy = bank_acc_num
is_even  = (digit_cnt %2 == 0)
checksum = 0
term = 0
for n in range (digit_cnt):
    if(is_even):
        term = 2 * (bank_acc_num_cpy % 10 )
        is_even = not is_even
    else:
        term = (bank_acc_num_cpy % 10 )
        is_even = not is_even
    checksum += term
    bank_acc_num_cpy //= 10

print("the checksum is= {}".format(checksum))
if(checksum % 10 == 0):
    print("acc num {} is a valid acc num".format(bank_acc_num))
else:
    print("acc num {} isn't a valid acc num".format(bank_acc_num))


# %% q7 

number = 1234 #1634 # 8208  # 9474
sum = 0

number_cpy = number

while ((number_cpy*10) // 10) != 0:
    sum += (number_cpy % 10)**4
    number_cpy //= 10

print("sum is= {}".format(sum))
if(sum == number):
    print("number {} is Narcissistic Number".format(number))
else:
    print("number {} is not a Narcissistic Number".format(number))



# %% q8 

num = int(input("enter integer num"))
n = 0
copy_num = num

while(num != 0): 
    num = num // 10
    n += 1

print("number of digits are: {}".format(n))

if(n%2  == 0):
    i=0
    left_sum = 0
    right_sum=0
    num=copy_num

    while(i < n):
        rem = num % 10
        num = num // 10
        if(i < (n/2)):
            right_sum = right_sum + rem
        if(i >= (n/2) ):
            left_sum=left_sum + rem
        i += 1

    if(left_sum == right_sum):
        print("number {} has EVEN digit number and the sum of digits on the right half and left half of it is equal ".format(copy_num))
    else:
        print("number {} has EVEN digit number but the sum of digits on the right half and left half of it isn't equal ".format(copy_num))
        # print(not X)
        # print(Number)
else:
    print("number {} has ODD digit number so the sum of digits on the right and left half of it doesnt exist ".format(copy_num))



# %% q9 fonskiyonun x ekseninde 0'a değdiği nokta (roots) bul

def func(x):
    return  x**2-4 #(x**3 - 5 * x - 9 )

boundary_start = -10
boundary_end = -5
tolerance = 0.00001
is_start_boundary_changed = True
is_end_boundary_changed = True
f_c = tolerance + 1 #just adding one to tolerance as a start to its always enters below while


while( abs(f_c) > tolerance):

    if(is_start_boundary_changed):
        f_start = func(boundary_start)
        is_start_boundary_changed = False

    if(is_end_boundary_changed):
        f_end = func(boundary_end)
        is_end_boundary_changed = False

    print("f(boundary_start) = {var1}\nf(boundary_end) = {var2}".format(var1 = f_start, var2 = f_end))
    c = boundary_end - (f_end * (boundary_end - boundary_start) / (f_end - f_start) )
    f_c = func(c)
    print("f(c) is= {var2:.4}".format( var2 = f_c))
    

    if(f_start * f_c < 0):
        boundary_end = c
        is_end_boundary_changed = True
    else:
        boundary_start = c
        is_start_boundary_changed = True

    print("boundaries: {var1:} --> {var2}".format(var1 = boundary_start,var2=boundary_end))
    print("***")

print("*************")
print("c(the root) is= {var1:5.4}".format(var1 = c))





# %%
