import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lowercase_map = dict.fromkeys(string.ascii_lowercase, 0)

        for char in s:
            lowercase_map[char] = lowercase_map.get(char, 0) + 1
        
        for char in t:
            lowercase_map[char] = lowercase_map.get(char, 0) - 1

        for val in lowercase_map:
            if lowercase_map.get(val) != 0:
                return False
        
        return True