class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        
        for string in strs:
            encodedString += str(len(string))
            encodedString += "#"
            encodedString += string
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []

        while i < len(s):
            lengthString = ""
            while s[i] != "#":
                lengthString += s[i]
                i += 1
            
            i += 1
            lengthOfString = int(lengthString)
            result.append(s[i:i+lengthOfString])
            i = i + lengthOfString

        return result 

        
