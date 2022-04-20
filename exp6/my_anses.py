

#%% q1 patlak
import random
correct_answers = [ [1, "A"],[2, "C"],[3, "A"],[4, "A"],[5, "D"],[6, "B"],[7, "C"],[8, "A"],[9, "C"],[10,"B"],[11,"A"],[12,"D"],[13,"C"],[14,"A"],[15,"D"],[16,"C"],[17,"B"],[18,"B"],[19,"D"],[20,"A"]]

answer_option_dict = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
}

ROWS = 20
COLS = 2
NUMBER_OF_STUDENTS = 3
student_answers = [[[0]*COLS]*ROWS]*NUMBER_OF_STUDENTS # böyle yapınca hepsini aynı referanslıyormuş sanırsam. O yüzden patlıyor.

for s in range(NUMBER_OF_STUDENTS):
    for r in range(ROWS):
        student_answers[s][r][0] = r+1 #random.randint(1,100)  # 
        student_answers[s][r][1] = answer_option_dict[(random.randint(1,4))] # random.randint(1,100)  # 
        print(student_answers[s][r])

print("wtf \n")
print(student_answers) # 
print(student_answers[0][0][0])

#%% q1

import random
from pprint import *
correct_answers = [ [1, "A"],[2, "C"],[3, "A"],[4, "A"],[5, "D"],[6, "B"],[7, "C"],[8, "A"],[9, "C"],[10,"B"],[11,"A"],[12,"D"],[13,"C"],[14,"A"],[15,"D"],[16,"C"],[17,"B"],[18,"B"],[19,"D"],[20,"A"]]

answer_option_dict = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
}

student_dict = {}


ROWS = 20
COLS = 2
NUMBER_OF_STUDENTS = 3

def make_3d_arr(rows, columns, columns2):
    lst = [[ ['#' for col in range(columns)] for row in range(rows)] for col in range(columns2)]
    return lst

def make_2d_arr(rows, columns):
    lst = [ ['#' for col in range(columns)] for row in range(rows)] 
    return lst

student_answers = make_3d_arr(ROWS,COLS,NUMBER_OF_STUDENTS)
students_and_their_wrong_anses = []
temp_list = []
#print(students_and_their_wrong_anses)

#random.seed(1)
for s in range(NUMBER_OF_STUDENTS):
    for r in range(ROWS):
        student_answers[s][r][0] = r+1 #random.randint(1,100)  # 
        student_answers[s][r][1] = answer_option_dict[(random.randint(1,4))] # random.randint(1,100)  # 
        #print(student_answers[s][r])

#print(student_answers) 
#print(student_answers[0][0][0]) #deneme
#pprint(student_answers)

for s in range(NUMBER_OF_STUDENTS):
    student_dict[s+1] = 0
    for r in range(ROWS):
        if(student_answers[s][r][1] == correct_answers[r][1] ):
            student_dict[s+1] += 1
        else:
            temp_list.append(r+1)
    students_and_their_wrong_anses.append(temp_list.copy())
    temp_list.clear()

print(students_and_their_wrong_anses)
#print(student_dict)
for s in range(NUMBER_OF_STUDENTS):
    if(student_dict[s+1] >= 5):
        print("\nstudent{}-------\n -passed the exam\n# of correct answers= {}\n# of wrong answers= {}".format(s+1,student_dict[s+1], ROWS - student_dict[s+1]))
    else:
        print("\nstudent{}-------\n -couldn't pass the exam\n# of correct answers= {}\n# of wrong answers= {}".format(s+1,student_dict[s+1], ROWS - student_dict[s+1]))
    print("# of wrong answers = {}\nwrong answered questions' numbers are:{}".format(len(students_and_their_wrong_anses[s]), students_and_their_wrong_anses[s]))
    
#%% q2
import random

def make_2d_random_arr(rows, columns):
    number_list = [1,2,3,4,5,6,7,8,9]
    lst = [ [random.choice(number_list)  for col in range(columns)] for row in range(rows)] 
    return lst

def is_LoShuMagicSquare(lst):
    is_LoShu = True # altta her kontrol edişte True koymak yerine, False değilse hep True kalıp en son bunun döndürülmesi daha mantıklı
    
    
    #check rows
    i = 0
    the_row_sum = sum(lst[i])
    prev_sum = the_row_sum
    i = 1
    while (True): #check rows
        the_row_sum = sum(lst[i])
        if(the_row_sum != prev_sum):
            return False   #rowların toplamı eşit değil, funcdan çık
        prev_sum = the_row_sum

        i += 1
        if (i > range(len(lst))):
            # is_LoShu = True #rowların toplamı eşit, columna bakmaya devam et
            break
    

    #check columns 
    the_col_sum = 0
    sum_col_list = [0 for col in range(len(lst))] # yukarıdaki gibi en başta şimdiki ve önceki veriyi karşılaştırmak için gereken ilk işlemi yazmamak için burada list kullandım.
    for r in range(len(lst)): 
        for c in range(len(lst[r])):
            sum_col_list[r] += lst[r][c]
    
    
    for i in range(len(sum_col_list)-1):
        if(sum_col_list[i] != sum_col_list[i+1]):
            return False

    the_col_sum = sum_col_list[0]


    #check_diagonal1
    the_diag1_sum = 0
    for d1 in range(len(lst)): 
        the_diag1_sum += lst[d1][d1]
        
    #check_diagonal2
    the_diag2_sum = 0
    for d2 in range(len(lst)): 
        the_diag2_sum += lst[-d2-1][-d2-1]

    if (the_diag1_sum == the_diag2_sum == the_col_sum == the_row_sum):
        print("ewr")

    return is_LoShu;
    

arr = make_2d_random_arr(3,3)
print(arr)
print(is_LoShuMagicSquare(arr))




#%% q4






