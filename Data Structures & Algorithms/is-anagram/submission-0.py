class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        valid_anagram = False

        if set(s) == set(t):
            valid_anagram = True
        
        
        return valid_anagram