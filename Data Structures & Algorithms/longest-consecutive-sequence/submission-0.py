class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)

        if not nums:
            return 0

        curr = 1
        longest = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                curr = curr + 1
                longest = max(longest, curr)
            elif sorted_nums[i] == sorted_nums[i-1]:
                continue
            else:
                curr = 1

        return longest
