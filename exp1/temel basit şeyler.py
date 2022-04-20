




for number in range(5,11):
    square = number ** 2
    print(number, '\t', square )
    
    

#%% 
#Functions


 #call main func

def main():
    print("the sum is:",get_sum(12,45))
    
    
def get_sum(num1, num2):
    sum = num1+num2
    return sum

main()

#%% 



def get_scores():
    test_scores = [] # made a list
    
    again = 'y'
    
    while again == "y":
        value = float(input("enter a test score: "))
        test_scores.append(value)
        
        print("wanna add another score?")
        again = input("type \'y\' for yes, anything else for no ")
        
        
        
    return test_scores
        
scores = get_scores()
print("the student's scores are: ", scores)
        
        


        