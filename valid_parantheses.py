class Solution:
    def isValid(self, s: str) -> bool:
        
         # stack is lifo
        
        stack = []
        closing_to_open_dict = {')':'(', ']':'[','}':'{'}
        
        for char in s:
            if char in closing_to_open_dict:
                #first checks for empty stack and then if the last char is not matching the first char
                if not stack or stack.pop() != closing_to_open_dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack
    
# not stack is true as all the char should be matched and stack is empty now

        
        



        


# Time = O(n)
# Space = O(n)