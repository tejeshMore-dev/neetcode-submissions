class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for i in range(n+1):
            cnt = 0
            while i>0:
                i = i&(i-1)
                cnt+=1
            results.append(cnt)

        return results