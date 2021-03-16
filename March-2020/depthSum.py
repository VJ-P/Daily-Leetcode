# Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, 
# or a list -- whose elements may also be integers or other lists.

def depthSum(nestedList):
    def dfs(array, depth):
        nonlocal sumDepth
        for item in array:
            if type(item) == int:
                sumDepth += item * depth
            else:
                dfs(item, depth + 1)

    sumDepth = 0
    dfs(nestedList, 1)
    return sumDepth

# print(depthSum([[1,1],2,[1,1]]))
# print(depthSum([1,[4,[6]]]))