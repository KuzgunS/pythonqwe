#%%

listt = []

listt.append([0,12])

print(listt)
listt.append([0,13])
listt.append([0,14])
print(listt)

listt2 = listt.copy()
listt.append(listt2)
print(listt)


# %%

mylist = [0,1,2]
mylist  = [mylist]
mylist = [mylist]
print(mylist)
mylist.append([0,1,2])
print(mylist)


# %%
#bu iyi
mylist = [1,2,3]
mylist.append(mylist.copy())
mylist.append(1)
mylist.append([1,2])
print(mylist)

# %%
