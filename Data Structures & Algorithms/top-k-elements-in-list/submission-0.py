class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter_dict = {}

        for n in nums:
            counter_dict[n] = counter_dict.get(n,0) + 1

        sorted_counter_dict = dict(sorted(counter_dict.items(), key=lambda item: item[1], reverse=True))

        ans = list(sorted_counter_dict)[:k]

        return ans