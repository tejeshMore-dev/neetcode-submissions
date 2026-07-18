class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr = sorted(self.arr)
        n = len(self.arr)
        if n%2==1:
            return float(self.arr[n//2])
        else:
            l = (n-1)//2
            r = n//2
            return float((self.arr[l] + self.arr[r])/2)
        