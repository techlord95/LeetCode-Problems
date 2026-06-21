# Recursion


# class Solution:
#     def evalRPN(self, tokens: list[str]) -> int:
#         def dfs():
#             token = tokens.pop()
#             if token not in "+-*/":
#                 return int(token)

# Because recursion processes the postfix expression from right to left, the first 
# recursive call corresponds to the right operand, not the left operand. 
#             right = dfs() # this will always be wriiten first 
#             left = dfs()

#             if token == "+":
#                 return left+right
#             elif token == "-":
#                 return left - right  
#             elif token == "*":
#                 return left*right
#             elif token == "/":
#                 return int(left/right)
#         return dfs()


# Stack


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            
            # pop removes the rightmost element and doing this pushes the the last two nums in stack  
            # stack works on lifo (first 2 chars)
            if c == "+":
                stack.append(stack.pop() + stack.pop()) # addistions follow commutative law a+b = b+a 
                
            elif c== "-":
                a , b = stack.pop() , stack.pop() # eg["2","3","-"] a=3(popped first) , b =2 (popped second)
                stack.append(b-a) # same lifo so (b -a = 2-3 = 1 ) 
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c =="/":
                a , b = stack.pop() , stack.pop()
                stack.append(int(float(b)/a)) # // this type of division gives rounds towards negative infinity 
                # question required truncation toward , 5//-2 == -3 and int(5/-2) = -2 . float used to get accurate ans but int used to truncate to 0 
                # / is floating point division and  // is floor division 
            else:
                stack.append(int(c))
        return stack[0]
            
        
                   
        
# Postfix operations to be done here 
# 3,4,+ 
# the above notation gives the ans 3+4 = 7

# Can be solved using Doubly Linked List , Recusrion and Stack

# Recursion and Stack both have Time and Space = O(n)
    