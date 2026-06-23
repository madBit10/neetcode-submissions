class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_map = {}

        ans = []

        for n in nums:
            counter_map[n] = counter_map.get(n,0) + 1

        # print(counter_map)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, cnt in counter_map.items():
            buckets[cnt].append(num)

        for i in range(len(buckets)-1, -1, -1):
            for val in buckets[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans

        return ans
        
            

        