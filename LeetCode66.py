class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = "".join(map(str, digits))
        b = str(int(a) + 1)
        c = b.split()
        return c
    
a  = Solution()
print(a.plusOne([1,2,3]))
        