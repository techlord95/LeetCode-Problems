class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        result = 0
        left_pointer = 0
        maximum_frequency = 0
        
        #expanding the window by moving right_pointer
        for right_pointer in range(len(s)):
            #count.get gets the current character count , for 1st elemet it returns 0 
            # and will throw key error 
            
            # +1 is added to increment as the current character is not in the dict yet 
            count[s[right_pointer]] = 1 + count.get(s[right_pointer] , 0)
            maximum_frequency = max(maximum_frequency, count[s[right_pointer]]) 
           
           #classic sliding window 
            while (right_pointer - left_pointer + 1) - maximum_frequency > k:
                
                #window shrinking 
                count[s[left_pointer]] -= 1
                left_pointer +=1
            result = max(result , right_pointer - left_pointer + 1)
        return result




# case 1 -> "ABAB" REPLACEMENT TO BE DONE BY UPPERCASE CHAR ONLY 
# K =2 
# LEN OF AAAA = 4

# max_frequency is the max occuring element 

# for loop count.get gets the current characters count , for the first element it will return default to 0 
# and throw key error , thats why (,0) is added 

#max_frequency is updated once using max()

# while loop logic 
# right_pointer - left_pointer + 1  is the length of the current window 
# so (window size - max_frequency) = number of characters to be replaced to form a long repeating string
# if this number is > k then shriking of window needs to be done

#in case of invalid window , it is shrinked by moving left_pointer to the right 
# and decrease the character count that has left the window 

# Time: O(n) — each character is added and removed at most once.

# Space: O(26) → only storing frequency of characters (uppercase English letters).






        