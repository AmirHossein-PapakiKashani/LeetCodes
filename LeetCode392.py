class Solution:
    def isSubsequence(self,s, t):
        m = len(s)
        n = len(t)
    
        # Initializing a matrix of size (m+1)*(n+1)
        dp = [[0] * (n + 1) for x in range(m + 1)]
    
        # Building dp[m+1][n+1] in bottom-up fashion
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if(dp[i ][j -1] > 0):
                    dp[i][j] = dp[i][j-1]
                    
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                   
                    continue
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                   
                else:
                    dp[i][j] = dp[i - 1][j - 1]
    
        # dp[m][n] contains length of LCS for S1[0..m-1]
        # and S2[0..n-1]
        return dp[m][n]==m

s=Solution()
print(s.isSubsequence("abc", "ahbgdc"))