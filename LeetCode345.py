class Solution:
    def reverseVowels(self, mainString: str) -> str:
        v=['a','e','i','o','u','A','E','I','O','U']
        newString = list(mainString)
        firstPointer = 0
        p1 = -1
        p2 = len(newString)
        while p2> p1 and  len(newString) > 0 :
            while p1 < len(newString) - 1:
                p1-=1
                if newString[p1] in v :
                    break
            while  p2 > 0:
                p2-=1
                if newString[p2] in v :
                    break
            if p2> p1> -1:
                temp = newString[p1]
                s[p1] = s[p2]
                s[p2] = temp
        s = ''.join(s)
        return s
                
s = Solution()
print(s.reverseVowels("IceCreAm"))