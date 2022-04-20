
#%%

import numpy as np
# arrays with numpy
import numpy as np

a = np.array([1,2,3,4,5,6]) # 6 satırlık array oluşturdun.
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # 3 satır, 4 sütunluk array oluşturdun

print(a.dtype)
print(a.shape)
print(a[4])

print()

print(b.dtype)
print(b.shape)
print(b[0])
#%% 
#sort arrays with numpy
import numpy as np

c = np.array([[7,1,4,12],[2,9,8,3]])
np.sort(c,axis=0 , kind = 'mergesort')
print(c)
print()

c = np.sort(c,axis=0 , kind = 'heapsort')
print(c)
print()

c = np.sort(c,axis=0 , kind = 'quicksort')[::-1]
print(c)
print()

c = np.sort(c,axis=1 , kind = 'heapsort')[::-1]
print(c)
print()

#%% 
# arrayları logic operasyonlarıyla değiştirme ya da array üzeride işlem yapma

print("array b is:\n", b,"\n")

divisible_by_2 = b[b%2 == 0] # b'dekilerin hangisi 2 ile bölünebiliyorsa onlardan tekrar bir satır arrayı oluşturuyor.
print(divisible_by_2,"\n")

interval = b[( b > 2) & (b<11) ]
print(interval,"\n")

five_and_up = (b > 5) | (b == 5)
print(five_and_up)


#%%
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # 3 satır, 4 sütunluk array oluşturdun
print("array b is:\n", b,"\n")

arr_1 = b.flatten()
arr_1[0] = 1333
print("arr_1 after flatting and changing element 0 is:", arr_1,"\n")
print("array b is:\n", b,"\n")



arr_2 = b.ravel() # bazı metodlar yeni obje yaratıyor bazıları da buradaki gibi yapıyormuş sanırsam o yüzden allta b de değişti.
arr_2[0] = 23434
arr_2[11] = 123213
print(id(arr_2) , id(b))
print("arr_2 after raveling and changing element 0 is:", arr_2,"\n")
print("array b is:\n", b,"\n")
