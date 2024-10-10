class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = []
        sumOfAltitude = 0
        for i in range(len(gain)):
            sumOfAltitude += gain[i] 
            highest.append(sumOfAltitude)
        return max(highest)
        
a = Solution()
print(a.largestAltitude([-5,1,5,0,-7]))