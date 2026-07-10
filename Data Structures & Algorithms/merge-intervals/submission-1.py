class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)

        past = intervals[0]

        ans = [past]
        for interval in intervals[1:]:
            if past[-1]>=interval[0]:
                ans[-1][-1] = max(interval[-1], past[-1])
            else:
                ans.append(interval)
            past = ans[-1]
        
        return ans