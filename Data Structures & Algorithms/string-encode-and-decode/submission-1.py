class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += f"{len(word)}#{word}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        words = []
        i=0
        while i < len(s):
            num = []

            while s[i] != "#":
                num.append(s[i])
                i+=1
            
            word_len = int("".join(num))
            
            words.append(s[i+1:i+word_len+1])
            i=i+word_len+1
        
        return words



            
