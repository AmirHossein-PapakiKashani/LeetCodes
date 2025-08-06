class Solution:
    romanToInDic = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    def romanToInt(self, s: str) -> int:
        a = 0
        b = 0
        for i in s:
            if b < self.romanToInDic[i]:
                a += self.romanToInDic[i] - (2*b)
                b =  self.romanToInDic[i]     
            else: 
                a += self.romanToInDic[i] 
                b =  self.romanToInDic[i]
        return a
    
a = Solution()
print(a.romanToInt("MCMXCIV"))
    