class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency_map = {}
        for num in nums:
            num_to_frequency_map[num] = num_to_frequency_map.get(num, 0) + 1
        
        frequency_to_num_bucket = [ [] for _ in range(len(nums) +  1) ]
        for key, value in num_to_frequency_map.items():            
            frequency_to_num_bucket[value].append(key)

        index = len(frequency_to_num_bucket) - 1
        result = []

        while k > 0 and index >= 0:
            if len(frequency_to_num_bucket[index]) > 0:
                for num in frequency_to_num_bucket[index]:
                    k -= 1
                    result.append(num)

                    if k == 0:
                        break

            index -= 1

        return result