class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                current_length = 1
                while True:
                    if num + current_length in num_set:
                        current_length += 1
                    else:
                        break
                longest = max(longest, current_length)
        return longest