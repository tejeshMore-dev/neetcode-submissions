from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(["0000"])
        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1

        queue = deque(["0000"])
        ans = 0

        isEnded = False
        while queue and not isEnded:
            length = len(queue)

            for _ in range(length):
                ele = queue.popleft()
                

                if ele == target:
                    isEnded = True
                    break

                for i in range(4):

                    val = int(ele[i])

                    temp = list(ele)
                    temp[i] = str((val + 1) % 10)
                    new_ele = "".join(temp)

                    if new_ele not in deadends_set and new_ele not in visited:
                        queue.append(new_ele)
                        visited.add(new_ele)

                        
                    temp = list(ele)
                    temp[i] = str((val - 1) % 10)
                    new_ele = "".join(temp)

                    if new_ele not in deadends_set and new_ele not in visited:
                        queue.append(new_ele)
                        visited.add(new_ele)
            
            if queue and not isEnded:
                ans += 1
        
        if isEnded:
            return ans
        return -1



        



