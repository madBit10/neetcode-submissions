class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        cnt = 0
        curr_cnt = 1
        n = len(nums)

        for i in range(n):
            curr_ele = nums[i]
            for j in range(i+1, n):
                if nums[j] == curr_ele:
                    curr_cnt = curr_cnt + 1
                cnt = max(curr_cnt, cnt)

        if cnt > 1:
            return True

        return False


        