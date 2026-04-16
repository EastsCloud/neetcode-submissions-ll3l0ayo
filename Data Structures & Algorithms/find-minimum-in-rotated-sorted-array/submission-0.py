class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            if l == r-1 and nums[l] > nums[r]:
                return nums[r]
            m = int((l+r)/2)
            print(l, r, m)
            if nums[l] < nums[m]:
                l = m
            elif nums[m] < nums[r]:
                r = m
        return nums[r]
            