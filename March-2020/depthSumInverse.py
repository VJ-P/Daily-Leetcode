# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up.
# i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

def depthSumInverse(nestedList):

    def getDepth(array, depth):
        nonlocal d
        for item in array:
            if type(item) == int:
                d = max(d, depth)
            else:
                getDepth(item, depth + 1)

    def dfs(array, depth):
        nonlocal sumDepth
        for item in array:
            if type(item) == int:
                sumDepth += item * depth
            else:
                dfs(item, depth - 1)

    d = 1
    sumDepth = 0
    getDepth(nestedList, d)
    dfs(nestedList, d)
    return sumDepth

# print(depthSumInverse([[1,1],2,[1,1]]))
# print(depthSumInverse([1,[4,[6]]]))