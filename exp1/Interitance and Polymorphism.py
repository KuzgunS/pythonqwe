
# class Automobile -------------------- 
class Automobile:
    
    def __init__(self,make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        
        
    # set functions
    def set_make(self,make):
        self.__make = make
        
    def set_model(self,model):
        self.__model = model
        
    def set_mileage(self, mileage):
        self.__mileage = mileage
        
    def set_price(self, price):
        self.__price = price
        
    # get functions

    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price
    
# class Sedan -------------------- 

class Sedan(Automobile):
    
    def __init__(self, make, model, mileage, price, doors):   
        Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors
        
    def set_doors(self, doors):
        self.__doors = doors
        
    def get_doors(self):
        return self.__doors
    
# class Truck -------------------- 
class Truck(Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type
        
    def set_drive_type(self,drive_type):
        self.drive_type = drive_type
                    
    def get_drive_type(self):
        return self.__drive_type
    
    
# main --------------------                      
def main ():
    my_Automobile = Automobile(1, "Tesla", 100000, 1)
    my_Sedan = Sedan(2, "Supra", 123, 15000, 4)
    my_Truck = Truck(3, "Tesla", 23456, 200000, "manual")
    
    print("my Sedan's model is: " + my_Sedan.get_model() + " SUPPRAA")
    my_Sedan.set_model("Mitsu Evo VII")
    print("my Sedan's model is: " + my_Sedan.get_model())

    
    
main()