
#%% its a list with lists in it

#3x2 row column liste gibi düşünebilirsin.
students = [['Joe', 'Kim'], ['Sam', 'Sue'], ['Kelly', 'Chris']]
print(students)

print(students[1])
print(students[2][0]) # 3. satır 1. sütundaki eleman seçiliyor
students[2][0] = "xdddd"
print(students[2][0])
print(students)
# %%
import random

ROWS = 4
COLS = 6

rand_list = [[0]*COLS]*ROWS
# print(rand_list)


for r in range(ROWS):
    for c in range(COLS):
        rand_list[r][c] =  random.randint(1,100)

print(rand_list)
print()
print(rand_list[0]) # whole 0th row
print()
print(rand_list[0][3]) #0th rows 3rd column
# %%
a = [1]*3
print(a)
print()

b = [[1]*3] * 20
print(b)
print()

c = [[[1]*3] * 20]*3
print(c)
print()
# %%
