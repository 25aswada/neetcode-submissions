class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowercase_string_list = []
        
        for char in s:
            if char.isalnum():
                char = char.lower()
                lowercase_string_list.append(char)
            else:
                continue

        left = 0
        right = len(lowercase_string_list) - 1

        while left < right:
            if lowercase_string_list[left] == lowercase_string_list[right]:
                right -= 1
                left += 1
            else:
                return False
        
        return True