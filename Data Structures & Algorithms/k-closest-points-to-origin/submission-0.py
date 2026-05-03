class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i1, i2 in points:
            heapq.heappush(heap, [-(i1*i1+i2*i2), i1, i2])
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for d, i1, i2 in heap:
            ans.append([i1, i2])
        return ans