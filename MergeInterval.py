# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        count = 1
        for x in intervals:
            s = x.start
            t = x.end
            n = len(ans)

            find = 0
            for y in ans:
                if (y.start <= x.start and x.start <= y.end) \
                or (x.end >= y.start and x.end <= y.end) \
                or (x.start <= y.start and x.end >= y.end):
                    y.start = min(x.start, y.start)
                    y.end   = max(x.end, y.end)
                    find = 1
                    break
                    
            if find == 0:
                ans.append(x)
                continue
        return ans