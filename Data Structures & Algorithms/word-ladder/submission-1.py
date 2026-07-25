from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]     
                graph[pattern].append(word)
        

        queue = deque([])
        queue.append(beginWord)
        visited = set()
        ans = 0
        ans_found = False

        while queue:
            q_len = len(queue)
            ans += 1

            for _ in range(q_len):
                word = queue.popleft()

                if word == endWord:
                    ans_found = True
                    break

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for nei in graph[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            
            if ans_found:
                break
        
        return ans if ans_found else 0
            

