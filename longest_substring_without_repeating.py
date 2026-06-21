class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character_Set = set()             # Stores characters currently in the window
        left_pointer = 0                  # Left boundary of the sliding window
        result_Set = 0                    # Result: length of the longest valid substring

        for right_pointer in range(len(s)):  # Right boundary of the sliding window
            while s[right_pointer] in character_Set:
                character_Set.remove(s[left_pointer])  # Remove leftmost character until duplicate is removed
                left_pointer += 1                      # Shrink window from the left
            character_Set.add(s[right_pointer])        # Add current character to the set
            result_Set = max(result_Set, right_pointer - left_pointer + 1)  # sliding_window size is right - left + 1 Update result if current window is larger

        return result_Set



# | Step | right\_pointer | char | Action                                    | Window (s\[left\:right+1]) | Set     | Length |
# | ---- | -------------- | ---- | ----------------------------------------- | -------------------------- | ------- | ------ |
# | 0    | 0              | a    | Add 'a'                                   | a                          | {a}     | 1      |
# | 1    | 1              | b    | Add 'b'                                   | ab                         | {a,b}   | 2      |
# | 2    | 2              | c    | Add 'c'                                   | abc                        | {a,b,c} | 3 ✅    |
# | 3    | 3              | a    | Duplicate → Remove 'a' → Add new 'a'      | bca                        | {b,c,a} | 3      |
# | 4    | 4              | b    | Duplicate → Remove 'b' → Add new 'b'      | cab                        | {c,a,b} | 3      |
# | 5    | 5              | c    | Duplicate → Remove 'c' → Add new 'c'      | abc                        | {a,b,c} | 3      |
# | 6    | 6              | b    | Duplicate → Remove 'b' → Add new 'b'      | cb                         | {c,b}   | 2      |
# | 7    | 7              | b    | Duplicate → Remove 'c', 'b' → Add new 'b' | b                          | {b}     | 1      |


# Time: O(n), where n = length of s
# Each character is visited at most twice: once by the right_pointer, and once by left_pointer.

# Space: O(k), where k = size of the character set (at most 128 for ASCII)

# substring -> aabbabc output = abc 


                
            
                
#        

                
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




