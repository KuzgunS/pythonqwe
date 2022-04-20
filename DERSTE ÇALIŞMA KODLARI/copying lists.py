# %%

list1 = [0,1,2,"end"]
list2 = list1 # with this list1 and list2 shows same place in mem.
list1[1] = "hello"
print(list1)
print(list2) # they're same


# %%
# to copy the elements of the list but have them seperate elements on diff locations of memory.
# solution 1
list3 = []
for n in list1:
    list3.append(n)
print(list3)

# solution 2
list4 = [] + list1
print(list4)
# solution 3
list5 = list1[:]
print(list5)
# solution 4
list6 = list1.copy()
print(list6)
# solution 5
list7 = list(list1)
print(list7)

