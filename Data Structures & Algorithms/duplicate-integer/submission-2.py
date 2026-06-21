class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums_map = {}
        for n in nums:
            nums_map[n] = nums_map.get(n,0) + 1
        

        for key in nums_map:
            if nums_map.get(key) > 1:
                return True
                break
        
        
        return False