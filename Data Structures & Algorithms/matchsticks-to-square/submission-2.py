class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        n = len(matchsticks)
        matchsticks.sort(reverse=True)

        if total % 4 != 0:
            return False
        
        target = total // 4
        path = set()

        def dfs(start, cur_sum, sets):
            if sets == 4:
                return True
            
            if cur_sum == target:
                return dfs(0, 0, sets + 1)

            
            for i in range(start, n):
                if i in path:
                    continue

                if matchsticks[i] + cur_sum > target:
                    continue

                path.add(i)
                
                if dfs(i+1, cur_sum + matchsticks[i], sets):
                    return True
                
                path.remove(i)
            
            return False

        return dfs(0,0,0)


        