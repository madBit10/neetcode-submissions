class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        st = set()

        for i in range(0,n):
            hashset = set()
            for j in range(i+1, n):
                
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    st.add(tuple(temp))

                hashset.add(nums[j])

        ans = [list(triplet) for triplet in st]

        return ans

        