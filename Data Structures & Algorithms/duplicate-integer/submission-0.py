class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_map = {}

        contains_duplicate = False

        for n in nums:
            nums_map[n] = nums_map.get(n,0) + 1
            
        for keys in nums_map:
            if nums_map.get(keys) > 1:
                contains_duplicate = True
                break

        return contains_duplicate
        


        