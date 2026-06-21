class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))

        s_l = len(s)
        t_l = len(t)

        for i, j in zip(sorted_s, sorted_t):
            if i != j:
                return False
        
        return True
        