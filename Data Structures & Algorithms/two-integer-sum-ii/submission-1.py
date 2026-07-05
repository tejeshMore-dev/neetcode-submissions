class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0 
        rp = len(numbers) -1
        result = None

        while lp < rp:
            sum = numbers[lp] + numbers[rp]

            if sum == target:
                result = [lp + 1,rp + 1]
                break
            elif sum < target:
                lp += 1
            else:
                rp -= 1   
        
        return result