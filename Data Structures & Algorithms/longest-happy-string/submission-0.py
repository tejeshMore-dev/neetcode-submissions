class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        f_map = {
            'a': a,
            'b': b,
            'c': c
        }
        
        for char, freq in f_map.items():
            if freq > 0:
                heapq.heappush(max_heap,(-freq,char))
        
        ans = []

        while max_heap:
            f, char = heapq.heappop(max_heap)
            
            if len(ans)>=2 and char == ans[-1] and char == ans[-2]:
                if not max_heap:
                    break
                f1, char1 = heapq.heappop(max_heap)
                ans.append(char1)
                f1 += 1
                if f1 < 0:
                    heapq.heappush(max_heap, (f1,char1))
            else:
                ans.append(char)
                f += 1
            if f < 0:
                heapq.heappush(max_heap, (f,char))
        
        return "".join(ans)