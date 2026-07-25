class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = []
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if stack and stack[-1][1] >= s:
                stack[-1][1] = max(e, stack[-1][1]) 
            else:
                stack.append(intervals[i])
        
        return stack