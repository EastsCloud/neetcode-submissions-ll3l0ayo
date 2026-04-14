class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        # print(nums)
        ans = []
        for i, ni in enumerate(nums):
            if i >= n-2:
                continue
            req = ni
            p1 = i+1
            p2 = n-1
            # print(i, req)
            while p1 < p2:
                # print(p1, p2, nums[p1], nums[p2], req + nums[p1] + nums[p2])
                if req + nums[p1] + nums[p2] == 0:
                    if [req, nums[p1], nums[p2]] not in ans:
                        ans.append([req, nums[p1], nums[p2]])
                    p2 -= 1
                    p1 += 1
                else:
                    if req + nums[p1] + nums[p2] > 0:
                        p2 -= 1
                    else:
                        p1 += 1                        
                if p1 >= p2 or p1 > n:
                    break
        return ans