
DENEME = "boş"

def assign_data(name,age,is_memer):
    # DENEME = name # DENEME'nin içindeki değeri kullanabilirsin ama değiştirmeye çalıştığında onu değiştiremezsin.
    global DENEME   # bunu yapabilmek için bu şekilde global demek gerekyior. sonra altta değişim yapıyorsun
    DENEME= name

    person_name = name
    person_age = age
    person_is_memer = is_memer
    return person_name,person_age,person_is_memer

def print_data(person_name,person_age,person_is_memer):
    print("name: ",person_name,"\nage: ", person_age, "\nis s/he a memer: ", person_is_memer)



#---------------------------------------------------

person_name,person_age,person_is_memer = assign_data("Bato",24,True)
print_data(person_name,person_age,person_is_memer)

print("\n")

# alttaki gibi, gönderilecek parametre listesine, fonksiyondaki gibi sırayla yazmasan bile parametre isimlerini eşitleyerek karışık şekilde yazabilirsin
person_name,person_age,person_is_memer = assign_data(age = 24, is_memer = True, name = "Meto"  )
print_data(person_name,person_age,person_is_memer)
print(DENEME , "+++++++++++++") # oluşturulan var, direkt func içine gitmedi, paramatre olarak vermen gerekk.


print("\n")

#pozisyon olarak doğru yazıp sonrasında isme göre karışık da yazabilirsin. Ama pozisyona göre yazılacaklar en başta olmalı.
person_name,person_age,person_is_memer = assign_data("Insert a girl name here", 24,  is_memer = True  )
print_data(person_name,person_age,person_is_memer)