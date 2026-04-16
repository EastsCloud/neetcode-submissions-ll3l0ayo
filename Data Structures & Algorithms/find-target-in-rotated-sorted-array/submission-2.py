class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if r == -1:
            return -1
        if r == 0 and target == nums[0]:
            return 0
        if r == 1:
            if target == nums[0]:
                return 0
            if target == nums[1]:
                return 1
        while l < r-1:
            m = int((l+r) / 2)
            print(l, r, m, nums[m], target)
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[l] < nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            if nums[m] < nums[r]:
                if nums[m] <= target and target <= nums[r]:
                    l = m
                else:
                    r = m
        return -1
