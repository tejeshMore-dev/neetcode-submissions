class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sp, fp = 0, 0
        
        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]

            if sp == fp:
                break

        sp2 = 0
        while True:
            sp = nums[sp]
            sp2 = nums[sp2]

            if sp2 == sp:
                return sp
        