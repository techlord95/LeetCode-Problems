# # Single Inheritance 

# class Animal : #parent class
#     def __init__(self, name):
#         self.name = name 
        
#     def info(self):
#         print ("Animal Name :" , self.name)
# class Dog (Animal): #child class 
#     def sounds(self):
#         print(self.name, "barks")

# dawg = Dog("good boi")
# dawg.info() # this here is an inherited method 
# dawg.sounds()


# # Multiple Inheritance

# class Mother:
#     mothername = ""
    
#     def mother(self):
#         print(self.mothername)
        
# class Father:
#     fathername = ""
    
#     def father(self):
#         print (self.fathername)

# class Son(Mother,Father):
#     def parents(self):
#         print("Father" , self.fathername)
#         print("Mother" , self.mothername)
        
        
# s1= Son()
# s1.fathername = "Mini Boss"
# s1.mothername = "Ultimate Boss"
# s1.parents()
        
        
# # Multi-Level Inhertance 

class GrandFather: 
    def __init__(self,grandfathername):
        self.grandfathername = grandfathername
        
class Father(GrandFather):
    def __init__(self, fathername, grandfathername):
        super().__init__(grandfathername)
        self.fathername = fathername
class Son(Father):
    def __init__(self, sonname , fathername , grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)
        
        
    def print_name (self):
        print ("Grandfather Name: " , self.grandfathername)
        print ("Father Name: " , self.fathername)
        print ("Son Name: " , self.sonname)
        
s1 = Son("Prince 3rd" , "Prince 2nd" , "Prince Og Gangster")

print(s1.grandfathername)
s1.print_name()
        

        
