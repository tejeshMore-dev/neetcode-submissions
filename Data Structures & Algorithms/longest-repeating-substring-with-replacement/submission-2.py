class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        lp = 0
        rp = lp
        frequencyMap = {}
        maxFrequency = 0

        while rp < len(s):
            frequencyMap[s[rp]] = frequencyMap.get(s[rp], 0) + 1
            maxFrequency =  max(frequencyMap[s[rp]], maxFrequency)

            while (rp - lp + 1) - maxFrequency > k:
                frequencyMap[s[lp]] = frequencyMap.get(s[lp], 0) - 1
                lp += 1

            result = max(result, rp - lp + 1)
            rp += 1

        return result

                