class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}

        for i, char in enumerate(order):
            order_map[char] = i

        new_words = sorted(words, key= lambda word: [order_map[c] for c in word])

        return new_words == words