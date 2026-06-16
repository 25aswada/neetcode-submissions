class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for num in nums:
            if num not in frequency:
                frequency[num] = 0
            frequency[num] += 1

        new_array = sorted(frequency, key=lambda x: frequency[x], reverse=True)

        return new_array[:k]
        