class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = [] # building an empty list 

        used = [False] * len(strs)

        for i in range(len(strs)):
            if used[i]:
                continue
            group = [strs[i]]
            used[i] = True
            sorted_i = sorted(strs[i])
            for j in range(i+1, len(strs)):

                if not used[j] and sorted_i == sorted(strs[j]):
                    group.append(strs[j])
                    used[j] = True
            output.append(group)

        return output