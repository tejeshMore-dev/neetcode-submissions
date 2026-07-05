class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0

        for num in nums:
            if num != val:
                nums[write_index] = num
                write_index += 1
            
        return write_index