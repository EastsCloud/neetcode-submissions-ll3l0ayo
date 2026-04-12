class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = i

        for i, n in enumerate(nums):
            if target-n in d and i != d[target-n]:
                return [i, d[target-n]]