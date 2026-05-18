class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = nums.copy()

        if len(nums) > 2:
            dp[2] += dp[0]
        
        if len(nums) < 4:
            return max(dp)

        for i in range(3, len(nums)):
            dp[i] = max(dp[i]+dp[i-2], dp[i]+dp[i-3], dp[i-1])
        
        return dp[len(nums)-1]