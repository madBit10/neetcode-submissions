class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in range(0,len(nums)):
            prod = 1
            for j, num in enumerate(nums):
                if j == i:
                    continue
                prod *= num
            ans.append(prod)
        

        return ans