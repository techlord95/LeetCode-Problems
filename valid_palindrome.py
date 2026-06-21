
# String Reveral Approach

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s=="":
            return True # empty str will always be true palindrome
        
        
        new_string = ""

        for character in s:
            if character.isalnum():
                new_string += character.lower()
        return new_string == new_string[::-1]

# Time - O(n)
# Space = O(n)


# how string operates
# s="3111"
# print(s[len(s)-1]) -> this will give the element at the end of the str

# More Optimized Two Pointer Approach

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left_ptr , right_ptr = 0 , len(s) -1
        
        #continue till the pointers meet 
        while left_ptr < right_ptr:
            
            # skipping non alpha numeric characters from the left 
            while left_ptr < right_ptr and not self.alphaNum(s[left_ptr]):
                left_ptr +=1 
            #skipping non alphanum chars from right 
            while left_ptr < right_ptr and not self.alphaNum(s[right_ptr]):
                right_ptr -= 1
                
            # compare chars ingnoring the case 
            if s[left_ptr].lower() != s[right_ptr].lower():
                return False
            
            # moving both pointers to the centre 
            left_ptr , right_ptr = left_ptr + 1 , right_ptr -1 
        return True
            

            
            
            
    def alphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or 
                ord("0") <= ord(c) <= ord("9")) 
    
# Time = O(n)
# Space = O(1)
             
        
        
       
            
                

       