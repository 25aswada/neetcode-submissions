class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0

        for i in range(len(height)):
            if i == 0:
                continue
            else:
            
                left = height[0:i]
                right = height[i:len(height)]

                left_max = max(left)
                right_max = max(right)
            
    
                water_index = max(0, min(left_max, right_max) - height[i])
                
                total_water += water_index

        return total_water