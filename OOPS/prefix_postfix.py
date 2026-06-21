# Prefix and Postfix operation in C++ / C / Java look like 
# (++x, x++ , --x , x--)

# Python dosen't have (x++ or ++x) operators 

# However, Python does have prefix operators (unary operators), prefix string modifiers, and a 
# rich way of handling prefix/postfix mathematical notations (like Reverse Polish Notation) algorithmically.

## Why ++x does not give syntax error 

# x = 5 
# print(++x , --x)
# -> output = 5 5

# Python interprets + and - as unary prefix operators.

# +x means "positive x" (which mathematically evaluates to x).

# ++x is parsed as +(+(x)). It just applies the unary plus operator twice. It does not increment the value.

# --x is parsed as -(-(x)), which mathematically cancels out the negative signs, leaving you with the original number.


# Dunder Methods 

import math 

class Vector :
    def __init__(self,x,y): #initiate
        self.x = x 
        self.y = y
    def __repr__(self): # representation
        return f"vector({self.x:2f} , {self.y:2f})" #2f is fancy formatting upto 2 decimal places 
    
    def __neg__(self): # Negative 
        return Vector(-self.x , -self.y) # here vector x and y are multiplied by -1 
    
   
        
        
    