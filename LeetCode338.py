

class Solution:
    def countBits(self, n: int) -> list[int]:
        result = []
        for i in range(6):
            result.append(self.CountingOnes(i))
        return result
    
    def CountingOnes(self,binaryNumber):
        a = bin(binaryNumber)
        b = a.replace("0b", "")
        c = b.count('1')
        return c
    
a = Solution()
print(a.countBits(2))

    