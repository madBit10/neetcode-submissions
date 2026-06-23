import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_dict = {}

        heap = []

        for n in nums:
            counter_dict[n] = counter_dict.get(n,0) + 1


        for val, cnt in counter_dict.items():
            heapq.heappush(heap, (cnt, val))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = [val for cnt, val in heap]

        return ans

        