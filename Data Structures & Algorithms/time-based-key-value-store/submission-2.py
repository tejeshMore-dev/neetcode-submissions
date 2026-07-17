from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.k_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.k_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.k_map[key]
        n = len(arr)
        if n == 0:
            return ""
        
        L = 0
        R = n-1
        ans = ""

        while L<=R:
            mid = L + (R-L)//2

            if arr[mid][0] > timestamp:
                R = mid-1
            else:
                ans = arr[mid][1]
                L = mid+1
        
        return ans
