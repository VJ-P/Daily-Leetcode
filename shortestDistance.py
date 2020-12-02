class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        wmap = {}
        for i in range(len(words)):
            w = words[i]
            if w in wmap:
                wmap[w].append(i)
            else:
                wmap[w] = [i]
        print(wmap)
        dist = float('inf')
        for i in wmap[word1]:
            for j in wmap[word2]:
                dist = min(abs(j-i), dist)
        return dist