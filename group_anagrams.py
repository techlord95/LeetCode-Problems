# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# hash table 

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1️⃣ Create a dictionary that will hold: signature → list of anagrams
        result = defaultdict(list)

        # 2️⃣ Process each word in the input list
        for i in strs:
            # 3️⃣ Build a 26‑element frequency vector for the current word
            count = [0] * 26               # one slot for each letter a‑z

            # 4️⃣ Count occurrences of each character
            for c in i:
                # ord('a') = 97, ord('b') = 98, ….
                # Subtracting ord('a') gives an index 0‑25
                count[ord(c) - ord("a")] += 1

            # 5️⃣ Convert the mutable list into an immutable tuple so it can be a dict key
            #    All words with the same tuple are anagrams.
            result[tuple(count)].append(i)

        # 6️⃣ Return the grouped values as a plain list of lists
        return list(result.values())


# Time and Space 

# O(n.K)

# best case scenario



"""
COMPARISON: Regular dict vs. defaultdict
---------------------------------------------------------------------------
| Feature       | Regular dict                 | defaultdict              |
|---------------|------------------------------|--------------------------|
| Missing Key   | Raises KeyError              | Creates key with default |
| Method Needed | .get() or .setdefault()      | Direct access: d[key]    |
| Setup         | None (Built-in)              | from collections import  |
---------------------------------------------------------------------------
"""