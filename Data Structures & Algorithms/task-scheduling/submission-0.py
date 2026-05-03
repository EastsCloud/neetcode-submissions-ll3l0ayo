class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        heap = []
        for i in d:
            heapq.heappush(heap, [-d[i], i])
        
        dq = deque()
        cycle = 0
        while heap or dq:
            cycle += 1
            # print("cycle", cycle)
            if heap:
                fi, ti = heapq.heappop(heap)
                # print("heappop", fi, ti)
                if fi < -1:
                    dq.append([cycle+n, fi+1, ti])
                    # print("push", ti, "to dq")
            if dq:
                if dq[0][0] == cycle:
                    _, nfi, nti = dq.popleft()
                    heapq.heappush(heap, [nfi, nti])
                    # print("push", nfi, nti, "to heap")
            # print(dq, heap)

        return cycle
        