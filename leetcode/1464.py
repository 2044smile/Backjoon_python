class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = nums[:2]
        if max2 > max1:
            max1, max2 = max2, max1
        for n in nums[2:]:
            if n > max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        return (max1-1) * (max2-1)
