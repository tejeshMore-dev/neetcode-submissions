class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    
        L = 0
        R = k
        while R<len(arr):
            if abs(arr[L]-x) < abs(arr[R]-x) or abs(arr[L]-x) == abs(arr[R]-x) and arr[L]<arr[R]:
                return arr[L:R]
            else:
                L+=1
            R+=1
        return arr[L:R]