class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        maximumCandies = max(candies)
        for i in range(len(candies)) :
            if(candies[i] + extraCandies >= maximumCandies):
                result.append(True)
            else:
                result.append(False)
        return result



a = Solution()
print(a.kidsWithCandies([2,3,5,1,3], 3))