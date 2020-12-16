class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        self.dfs(s, [], answer)
        return answer
        
        
    def dfs(self, s, partition, ans):
        if len(s) == 0:
            ans.append(partition)
            return
        
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], partition+[s[:i]], ans)

    def isPalindrome(self, s):
        return s == s[::-1]