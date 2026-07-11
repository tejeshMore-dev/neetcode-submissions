class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if s[i] == ']':
                word = ""
                while stack and stack[-1]!='[':
                    word = stack[-1]+word
                    stack.pop()
                
                stack.pop()
                num = int(stack[-1])
                stack.pop()
                ans = num*(word)
                stack.append(ans)

            elif s[i].isdigit():
                num = ""
                while s[i]!='[':
                    num += s[i]
                    i+=1
                num = int(num)
                stack.append(num)
                stack.append('[')
            else:
                stack.append(s[i])
            i+=1
        
        ans = ""
        while stack:
            ans = stack[-1]+ans
            stack.pop()

        return ans