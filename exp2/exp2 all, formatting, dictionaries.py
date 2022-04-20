
#%% q1 print işleri sallandı

#%% q2

a = []

for i in range(3):
    a.append(float(input("enter number: ")))
         
print(len(a))  
is_descending = False
is_ascending = False

for i in range(len(a)-1):
    if(a[i]>a[i+1]):
        is_descending = True
    else:
        is_descending = False
        break
    
for i in range(len(a)-1):    
    if(a[i]<a[i+1]):
        is_ascending = True
    else:
        is_ascending = False
        break
         
if((is_ascending == True) | (is_descending == True) ):
    print("integers are in order")
else:
    print("integers are not in order")

#%% q3 tam düzgün olmuyor

d = (int(input("enter day: ")))
m = (int(input("enter month: ")))
y = (int(input("enter year: ")))


y0 = y - (14 - m) / 12
x = y0 + y0/4 - y0/100 + y0/400
m0 = m + 12 * ((14 - m) / 12) - 2
d0 = (d + x + (31*m0)/ 12) % 7
d0 = int(d0)

days = {
        0: "pazar",
        1: "pazartesi",
        2: "salı",
        3: "çarşamba",
        4: "perşembe",
        5: "cuma",
        6: "cumartesi",
        }

print("day is: {}".format(days[d0]))



#%% q4 rgb to cmyk with formatting numbers

r = (int(input("enter red: " )))
g = (int(input("enter green: ")))
b = (int(input("enter blue: ")))

w = max(r/255, g/255, b/255) 
c = (w - r/255) / w 
m = (w - g/255) / w 
y = (w - b/255) / w 
k = 1 - w

print("c=",format(c,".2f"))
print("m= {var1:10.8f} \ny= {var2}\nk={k}".format(var1=m, var2=y,k=k))

#%% q5

line_length = []

for i in range(3):
    line_length.append(float(input("enter line length: ")))
    
print( (line_length[0]<line_length[1]+line_length[2] and line_length[1]<line_length[0]+line_length[2] and line_length[2]<line_length[1]+line_length[0]) )


#%% q5 # bunu metocum öğretti, hoşmuş

x = float(input("enter x\n"))

y = {
        x < -3 : (x**3 + 4) / (x*x),
        ((x >= -3) and x < 0) : abs(x**2 + 3*x - 10),
        ((x >= 0) and (x < 4) ): x**2 - 4*x,
        x >= 4 : x
        
        }


print(y[True]) # y dictionariy'si içinden hangilerinin keyi doğru sonuç veriyorsa onu yazdırıyor. 