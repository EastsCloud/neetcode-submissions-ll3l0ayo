class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        max_ = 0
        while p1 < p2:
            print(p1, p2, (p2-p1)*min(heights[p1], heights[p2]))
            if (p2-p1) * min(heights[p1], heights[p2]) > max_:
                max_ = (p2-p1) * min(heights[p1], heights[p2])
            if heights[p1] < heights[p2]:
                p1 += 1
            elif heights[p2] < heights[p1]:
                p2 -= 1
            else:
                p1 += 1
                p2 -= 1
        return max_