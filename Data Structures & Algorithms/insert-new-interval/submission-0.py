class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0
        while i<len(intervals):
            if intervals[i][0]<newInterval[0]:
                i+=1
            else:
                break
        
        intervals.insert(i, newInterval)
        print(intervals)

        past = intervals[0]

        i = 1
        while i<len(intervals):
            if past[-1] >= intervals[i][0]:
                past[-1] = max(past[-1], intervals[i][-1])
                intervals.pop(i)
            else:
                past = intervals[i]
                i+=1
        
        return intervals
