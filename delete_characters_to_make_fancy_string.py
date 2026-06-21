class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for i in s:
            if len(result) >= 2 and result[i -1] ==i  and result[i-2] ==i :
                continue
            result.append(i)
             
        return ''.join(result) # joined them to get them back as a string

        
        
        
        
        
#question requirements- no 3 consecutive characters should be equal to make a fancy string

#  in a list values are appended at the end add charcters element by element 



# len(result) >= 2: Make sure there are at least 2 characters already in result, otherwise you can't compare the last 2.

# result[-1] == i: Check if the last character added is equal to the current character i.

# result[-2] == i: Check if the second last character is also equal to i.

# 📌 If all three are equal — that means adding the current character would result in three in a row, which we do not want — so we skip it using continue.



# Time Complexity: O(n) – where n is the length of the input string.

# Space Complexity: O(n) – we may store up to n characters in the result list.
