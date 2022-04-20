
#%%
from numpy import full


name = 'Juliet'
for ch in name:
    print(ch)

for ch in name:
    ch = "x"
print(name) # iterate ederken kopyasının üzerinden ediyor o yüzden ch değişse bile orj. string değişmez


# %% indexing strings

my_string = 'Roses are red'
print(len(my_string))

ch = my_string[6]
print(ch)

print(my_string[-1], my_string[-2], my_string[-1* len(my_string)])



# %% concatenation
message = 'Hello' + " " + 'world'

print(message)

first_name = 'Eren'
last_name = 'Yeager'
full_name = first_name + ' ' + last_name
print(full_name)

full_name += "qwe"
print(full_name)

# %% strings are immutable

friend = 'Jizz'
friend[0] = 'W' # you cant make wizz out of jizz

# %% string slicing

his_name = "Reiner Braun"
first_name = his_name[0:6]
print(first_name)

my_str = his_name[:]
print(my_str)


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(letters[0:len(letters):3]) # every third char is included in slice



# %% in and not in

text = "Four score and seven years ago"
str2 = " s"
if str2 in text:
    print('The string "{}" was found.'.format(str2))
else:
    print('The string "{}" was not found.'.format(str2))

# %%
