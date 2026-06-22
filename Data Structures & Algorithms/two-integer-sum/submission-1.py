class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}
        
        for i, n in enumerate(nums):
            nums_map[n] = i
            

        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums_map and nums_map[comp] != i:
                return [i, nums_map[comp]]
        
        
        
        


        