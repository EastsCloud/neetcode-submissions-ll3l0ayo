class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        cur = {s[0]}
        p1 = 0
        p2 = 0
        max_ = 0
        while p1 < n and p2 < n-1:
            p2 += 1
            if s[p2] not in cur:
                cur.add(s[p2])
            else:
                while p1 < p2:
                    if s[p1] == s[p2]:
                        p1 += 1
                        break
                    cur.discard(s[p1])
                    p1 += 1
            if p2 - p1 + 1 > max_:
                max_ = p2 - p1 + 1
            print(p1, p2, max_)
        return max_