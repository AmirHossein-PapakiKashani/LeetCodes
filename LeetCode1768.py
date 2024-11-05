class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        minummLen = min(len(word1), len(word2))
        sumoftwoWord = len(word1)+ len(word2)
        for i in range(minummLen):
            mergedWord += word1[i] + word2[i] 
        if(len(word1) < len(word2)):
            mergedWord += word2[minummLen:]
        else:
            mergedWord += word1[minummLen:]
        return mergedWord
    
a = Solution()
print(a.mergeAlternately("abc","pqr"))