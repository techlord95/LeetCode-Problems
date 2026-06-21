class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, it's impossible for s2 to contain its permutation
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase English letters 
        s1Count, s2Count = [0] * 26, [0] * 26

        # Build initial frequency counts for: (basically a frequency map)
        # - entire s1
        # - first window of s2 (same size as s1)
        
        # We build:
        # Full frequency map of s1
        # Frequency map of the first window in s2 (same size as s1)
        
        # At this point:  
        # We have a valid window to compare against s1
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # Count how many characters (out of 26) have matching frequencies in the frequency map 
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        # Left pointer of sliding window
        l = 0

        # Start sliding the window from index len(s1) to end of s2
        for r in range(len(s1), len(s2)):
            
            # If all 26 characters match, we found a permutation
            if matches == 26:
                return True

            # ---- STEP 1: Add new character (right side of window) ----
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1

            # If after increment, counts match → increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If they were matching before but now exceeded → decrease matches
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # ---- STEP 2: Remove old character (left side of window) ----
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # If after decrement, counts match → increase matches
            if s1Count[index] == s2Count[index]:
                matches += 1
            # If they were matching before but now fell below → decrease matches
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            # Move left pointer forward (shrink window)
            l += 1

        # Final check after loop ends
        return matches == 26
    
  
# Time: O(n)$, Space: O(1) where n is `len(s2)`.
    
# Why arrays of size 26?

# We assume only lowercase English letters ('a' to 'z')
# Each index represents a character:
# 'a' → 0, 'b' → 1, ..., 'z' → 25

# This is faster than using a dictionary (Counter) because:

# No hashing
# Constant-time access
    


