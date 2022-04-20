
#%% index method
from numpy import number


wish_a_num = [0,1,2,3,4,5,69,6,7]

print("wish a number! --> {list1}".format(list1 = wish_a_num))


change = int(input("tell me a number to change"))

try:
    item_index = wish_a_num.index(change)

    new_item = int(input("enter the new number that you want to replace the other number with"))
    wish_a_num[item_index] = new_item
    print("the list with the number you wish:",wish_a_num)

except ValueError:
    print("that item isn't found on the list")

print("wish a number now :))")


#%% insert method

numbers = [0,1,2,4,5,6]
numbers.insert(3,3)

print(numbers)

numbers.insert(3,"xd")
print(numbers)


# %% sort


my_list = [1,2,44,53,2,2,2,98]
my_list.sort()
print(my_list)

list2 = ["ayaya","aaron",'beta', 'alpha', 'delta', 'gamma']
list2.sort()
print(list2)


# hata veriyor
# mixed_list = ["text" , 123 , 1.2553 , True]
# mixed_list.sort()
# print(mixed_list)


# %% remove method

my_list = [1,2,2,44,53,98]
my_list.remove(2)
print(my_list)

#%% del method to remove specific item at index

my_list = [1,2,2,44,53,98]
del my_list[5]
print(my_list)

# %% reverse method

my_list = [1,2,2,44,53,98]
my_list.reverse()
print(my_list)

# %%
