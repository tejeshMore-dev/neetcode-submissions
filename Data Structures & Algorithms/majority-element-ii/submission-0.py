class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1, num2 = -1, -1
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                ctn2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
        
        ans = []
        if cnt1 > len(nums)//3:
            ans.append(num1)
        
        if cnt2 > len(nums)//3:
            ans.append(num2)
        
        return ans
