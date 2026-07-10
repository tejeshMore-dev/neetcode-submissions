class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)

        past = intervals[0]

        cnt = 0
        for interval in intervals[1:]:
            if past[-1]>interval[0]:
                if interval[-1] < past[-1]:
                    past = interval
                cnt += 1
            else:
                past = interval 
        return cnt
             
