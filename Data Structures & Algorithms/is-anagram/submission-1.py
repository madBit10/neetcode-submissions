class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        valid_anagram = True

        if len(s) != len(t):
            valid_anagram = False

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        for i, j in zip(sorted_s, sorted_t):
            if i != j:
                valid_anagram = False
                break


        # if set(s) == set(t):
        #     valid_anagram = True
        
        
        return valid_anagram