from collections  import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # edge case 1 (empty string)
        if not t or not s:
            return ""
        
        # initialize the count
        need = Counter(t)
        window = defaultdict(int) # hashmap / dictionary

        
        have , need_count  = 0 , len(need) # checking total unique chars needed
        
        # result checks the smallest window found [start,end]
        
        result, result_length  = [-1,-1 ] , float("infinity") 
        # infinity is used as it is more readable to say no window has been found yet 
        # a standard way 
        
        left  = 0 #starting the index of current window 
        
        
        # moving the right pointer to exampt the window one character at a time 
        
        for right in range(len(s)):
            character = s[right] 
            window[character] +=1 
            
            # if char is needed and we have exactly enough in window then increase have 
            if character in need and window[character] == need[character]:
                have +=1 
                
            # once we have the characters we shrink the window from left
               
            while have == need_count:
                if (right - left +1) <result_length:
                    result = [left,right]
                    result_length = right - left + 1
                    
                    
                    # before moving left , decreasing the count of the char in window 
                    
                window[s[left]] -= 1

                    # if char removal causes no longer satisfaction of required frequency 
                    # then decrease have 
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -=1
                left +=1 # moving left to the right to continue shrinking 
        l, r  = result 
        return s[l:r+1] if result_length != float("infinity") else ""


        
# Time -> O(n + m) 
# Space -> O(m)

# n is the length  of the string s and m is the total number of unique characters in t ,s 
        
        
        
# idea to be followed 

# s has to contain the string t  

# -> count what we need using Counter 
# -> use pointers left and right to make a sliding window 
# -> expand the right to include characters when valid and move the window left to 
# shrink the window


# Intuition
# We want the smallest window in s that contains all characters of t (with the right counts).
# Instead of checking all substrings, we use a sliding window:

# Expand the window by moving the right pointer r and adding characters into a window map.
# Once the window has all required characters (i.e., it "covers" t), we try to shrink it from the left with pointer l to make it as small as possible while still valid.
# During this process, we keep track of the best (smallest) window seen so far.
# This way, we only scan each character at most two times, making it efficient and still easy to follow.

# Algorithm
# If t is empty, return "".
# Build a frequency map countT for characters in t.
# Initialize:
# window as an empty map for the current window counts.
# have = 0 = how many characters currently meet the required count.
# need = len(countT) = how many distinct characters we need to match.
# res = [-1, -1] and resLen = infinity to store the best window.
# Use a right pointer r to expand the window over s:
# Add s[r] to window.
# If s[r] is in countT and its count in window matches countT, increment have.
# When have == need, the window is valid:
# Update the best result if the current window is smaller.
# Then shrink from the left:
# Decrease the count of s[l] in window.
# If s[l] is in countT and its count in window falls below countT, decrement have.
# Move l right.
# After the loop, return the substring defined by res if found; otherwise, return "".



                    

        
        
        
        
            
        
        

        