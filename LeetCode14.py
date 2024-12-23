class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        LCP = ""
        counter = 0
        sortedWords = sorted(strs, key=len)
        firstWord = sortedWords[0]
        for i in range(len(firstWord)):
            for s in sortedWords:
                a = s[0:i+1]
                b = firstWord[0:i+1]
                if s[0:i+1] == firstWord[0:i+1]:
                    counter += 1
                else:
                    break
            if counter == len(strs):
                LCP = firstWord[0:i+1]
                counter = 0
            else:
                counter = 0
                continue
        return LCP
    
a = Solution()
print(a.longestCommonPrefix(["dog","racecar","car"]))