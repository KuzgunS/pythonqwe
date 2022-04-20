
#%% string testing methods


the_string = "ayayay23"

if the_string.isalnum():
    print("string is alphanumeric")
if the_string.isdigit():
    print("string is only digits")
if the_string.isalpha():
    print("string is only alphabetic chars")
if the_string.isspace():
    print("string is only whitespace chars")
if the_string.islower():
    print("string is all lowercase")   
if the_string.isupper():
    print("string is all uppercase")   


# %% string modification methods

letters = 'WXyz'
print(letters, letters.lower())
print(letters, letters.upper())



# %%

the_string = "ayay ay23 \n  \t"
the_string2 = "ayay ay23"
str2 = "23"

print("**" + the_string.rstrip() + "**")
print("**" + the_string2.rstrip(str2) + "**")



# %% Searching and Replacing


the_string = "ayay ay23"
substring = "23"

print(the_string.find(substring)) # return lowest index in the string where substring is foound, if not found return -1

print(the_string.replace("aya","xd"))

filename = "file.py"
if filename.endswith('.txt'):
    print('That is the name of a text file.')
elif filename.endswith('.py'):
    print('That is the name of a Python source file.')
elif filename.endswith('.doc'):
    print('That is the name of a word processing document.')
else:
    print('Unknown file type.')


# %% split

word_list = "hey hey".split()
string1 = "kindness of a random stranger"
print(string1.split())
print(word_list)
print(string1.split("s"))
# %%
