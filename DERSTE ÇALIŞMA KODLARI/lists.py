




#%%


numbers = [5, 10, 15, 20]
print(numbers)

numbers2 = list(range(1, 10, 3))
print(numbers2)



#%% 
empty_list = list()
print(empty_list)

# %%

my_list = [5,3] *3
print(my_list)
print(my_list[3])
print(my_list[-1])
# print(my_list[-89]) list index out of range diyor. 
print(len(my_list))


# %%

numbers = [99, 100, "xd", 102]
for n in numbers:
    print(n)

# %%

a_list = [123]
# a_list[1] = 456 # out of range diyor. bu şekilde yeni list elemanı oluşturamıyorsun

# %%
a = 123
# a.append(123) # olmuyor 
b = [123]
b.append(456)
print(b)
# %%
