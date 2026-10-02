from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        freq1=freq.most_common(k)
        return [key for key , values in freq1]