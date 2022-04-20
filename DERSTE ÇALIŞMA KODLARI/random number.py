
#%%

import random

print("random number btw 0-100 is:",random.randint(0,100)) 


# %%

import random


print(random.randrange(10)) 
print(random.randrange(5,10)) # 5,6,7,8,9
random.seed(10) # terminalde, bu satırdan öncekiler random geliyor, interactive modeda yukardakiler de seedli oluyor. 
print(random.randrange(0, 101, 10)) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(random.random()) # 0 ile 1 arasında float sayı, 1 dahil değil.
print(random.uniform(1.0, 29.95)) # 29.95 katılmadan bu aralıkta float döndürüyor

# %%
