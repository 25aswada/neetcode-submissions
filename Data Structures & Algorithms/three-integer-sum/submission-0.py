class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_list = sorted(nums)
        results = []

        for i in range(len(sorted_list)):
            if i > 0 and sorted_list[i] == sorted_list[i-1]:
                continue

            left = i + 1
            right = len(sorted_list) - 1

            while left < right:
                if sorted_list[left] + sorted_list[right] == -sorted_list[i]:
                    results.append([sorted_list[i], sorted_list[left], sorted_list[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_list[left] == sorted_list[left - 1]:
                        left += 1
                    while left < right and sorted_list[right] == sorted_list[right + 1]:
                        right -= 1
                elif sorted_list[left] + sorted_list[right] > -sorted_list[i]:
                    right -= 1
                else:
                    left += 1

        return results