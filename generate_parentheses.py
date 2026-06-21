class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN): #no. of opening and closing brackets used till now
            if openN == closedN == n:
                res.append("".join(stack)) # used to convert a list of char into a string and add it to the result string
                return

            if openN < n:
                stack.append("(")
                
                # recursively moving forward with onw extra opening bracket (backtracking)
                backtrack(openN + 1, closedN)
                stack.pop() # when we are done with the backtracking and adding the ( to the stack
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        #  start recursion with 0 opening and 0 closing brackets
        backtrack(0, 0)
        return res
    
    
    
    
    
# Dynamic Programming

# class Solution:
#     def generateParenthesis(self, n):
#         res = [[] for _ in range(n+1)]
#         res[0] = [""]

#         for k in range(n + 1):
#             for i in range(k):
#                 for left in res[i]:
#                     for right in res[k-i-1]:
#                         res[k].append("(" + left + ")" + right)

#         return res[-1]
    
# both solutions have 

# Time = O(4^n/sqrt(n))

# Space = O(n)




# You are an Expert Data Scientist with more than 30 years of experience and you provide your insights and code like a professional who has seen everything in the world of data science / data analysis / data engineering / ML / DL / AI and you have decent industry exposure which includes experience from top tech companies like Netflix Google Amazon Facebook and Microsoft 

# Respond the queries accordingly 


# tell me about yourself in about 10 lines


