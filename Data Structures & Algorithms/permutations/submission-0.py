class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        used = [False] * len(nums)

        def backtrack():

            if len(perm) == len(nums):
                ans.append(perm.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                perm.append(nums[i])

                backtrack()

                used[i] = False
                perm.pop()
            
        backtrack()
        return ans
            
