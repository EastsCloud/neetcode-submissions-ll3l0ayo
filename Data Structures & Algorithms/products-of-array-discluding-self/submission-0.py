class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfp = [1]
        rpfp = [1]
        ans = []
        for i, n in enumerate(nums):
            i = i+1
            if i != len(nums):
                pfp.append(pfp[i-1]*n)
        nums.reverse()
        for i, n in enumerate(nums):
            i = i+1
            if i != len(nums):
                rpfp.append(rpfp[i-1]*n)

        rpfp.reverse()

        for i in range(len(nums)):
            print(str(pfp[i]) + " " + str(rpfp[i]))
            ans.append(pfp[i]*rpfp[i])
        
        return ans