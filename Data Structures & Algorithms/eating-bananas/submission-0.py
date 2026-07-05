class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minBananas = 1
        maxBananas = 0

        for n in piles:
            maxBananas = max(maxBananas, n)

        while minBananas <= maxBananas:
            mid = (minBananas + maxBananas) // 2

            ans  = 0
            for bananas in piles:
                ans += (bananas//mid)
                if bananas % mid:
                    ans += 1

            if ans > h:
                minBananas = mid + 1
            else:
                maxBananas = mid - 1

        return minBananas
            