class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ans = []
        st = set()

        for i in range(0,n-1):

            j = i + 1
            k = n - 1

            while j<k:
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i], nums[j], nums[k]]
                    temp.sort()
                    # print(temp)
                    st.add(tuple(temp))
                    # print(st)
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        ans = [list(triplet) for triplet in st]
        return ans

        # Time - O(n^2) {near about}

        