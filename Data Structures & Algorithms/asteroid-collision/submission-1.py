class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        stack = []
        for asteroid in asteroids:
            
            if stack:
                top=stack[-1]

            if stack and top>0 and asteroid<0:
                while stack and top>0 and asteroid<0:
                    top = stack[-1]
                    stack.pop()
                    if abs(top)>abs(asteroid):
                        stack.append(top)
                        break
                    elif abs(top) == abs(asteroid):
                        break
                    elif not stack or stack[-1]<0:
                        stack.append(asteroid)
                        break
            else:
                stack.append(asteroid)
        return stack

