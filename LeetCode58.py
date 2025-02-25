class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        b = a.pop()
        print(b)
        return int(len(b))
    
a = Solution()
print(a.lengthOfLastWord("   fly me   to   the moon  "))