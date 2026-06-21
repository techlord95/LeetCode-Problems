# Class 

class Dog :
    species = "husky"
    
    #  init is a constructor to initiate 
    
    def __init__(self,name, age): # self refers to current object 
        self.name = name # attribute 
        self.age = age # attribute
        
# Creating an object which is an instance of a class 

dawg = Dog("Bolt",2)
print(dawg.name,'\n',dawg.age )
        
        
        