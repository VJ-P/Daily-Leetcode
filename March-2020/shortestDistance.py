def shortestDistance(words, word1, word2):
    i1 = -1
    i2 = -1
    minDist = float('inf')

    for i in range(len(words)):
        if words[i] == word1:
            i1 = i
        elif words[i] == word2:
            i2 = i

        if i1 != -1 and i2 != -1:
            minDist = min(minDist, abs(i2 - i1))

    return minDist



# print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))
# print(shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"makes","coding"))
# print(shortestDistance(["a", "a", "b", "b"], "a", "b"))