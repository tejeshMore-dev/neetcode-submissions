class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}

        for num in nums:
            f_map[num] = f_map.get(num, 0) + 1

        f_num =  [ [] for _ in range(len(nums)+ 1) ]

        for num, f in f_map.items():
            f_num[f].append(num)
        
        i = len(nums) - 1
        res = []

        while k > 0:
            if f_num[i] and k > 0:
                for num in f_num[i]:
                    res.append(num)
                    k -=1
                    
            i -=1

        return res


        


        