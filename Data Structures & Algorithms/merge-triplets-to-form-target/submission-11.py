class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = target
        m1 = m2 = m3 = False

        inp = []
        for a, b, c in triplets:
            if a <= t1 and b <= t2  and c <= t3:
                inp.append([a, b, c])

        for a, b, c in triplets:
            if a > t1 or b > t2 or c > t3:
                continue
            
            if a == t1:
                m1 = True
            
            if b == t2:
                m2 = True
            
            if c == t3:
                m3 = True

        return m1 and m2 and m3



        