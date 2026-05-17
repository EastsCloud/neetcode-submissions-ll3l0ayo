class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        s = 0

        def backtrack(i):
            nonlocal s

            if s == target:
                ans.append(subset.copy())
                return

            if i == len(nums):
                return
            
            if s > target:
                return

            s += nums[i]
            subset.append(nums[i])
            backtrack(i)
            s -= nums[i]
            subset.pop()

            backtrack(i+1)

        backtrack(0)
        return ans