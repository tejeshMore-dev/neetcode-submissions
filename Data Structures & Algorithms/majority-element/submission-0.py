class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        majority_count = 0
        majority_element = nums[0]

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
            if count_map[num] > majority_count:
                majority_element = num
                majority_count = max(count_map[num], majority_count)

        return majority_element