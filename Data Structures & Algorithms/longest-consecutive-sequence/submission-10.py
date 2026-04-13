class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        max_ = 0
        cur = 1
        last = "no"
        if len(nums) == 0:
            return 0
        for i, n in enumerate(nums):
            d[n] = i
        print(sorted(d))
        for k in sorted(d):
            if last == "no":
                last = k
                print("continue")
                continue
            print(last, cur, k)
            if k == last + 1:
                cur += 1
                last = k
                if max_ < cur:
                    max_ = cur
            else:
                cur = 1
                last = k
                print("end cycle", cur)
        if max_ < cur:
            max_ = cur
        return max_