class Solution:
    def reverseWords(self, s: str) -> str:
        listOfSplitedWord = s.split()
        result = ""
        if(len(s) == 0):
            return ""
        if(len(s) == 1):
            return s
        for i in listOfSplitedWord:
            result = i + " " + result
        return result[0:-1]
    
a = Solution()
print(a.reverseWords("hellot world "))    
                