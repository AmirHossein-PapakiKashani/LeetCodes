class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        lengthFlowerBed = len(flowerbed)
        if(lengthFlowerBed == 1 and flowerbed[0] == 0 and n == 1):
            return True
        if(lengthFlowerBed > 1 and flowerbed[0] == 0 and n == 1):
            return True
        if(lengthFlowerBed > 1 and flowerbed[0] == 0 and n > 1):
            flowerbed[0] = 1
            n -= 1
        if(lengthFlowerBed > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0 and n == 1):
            return True
        for i in range(1,len(flowerbed)-1):
            if(flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0):
                flowerbed[i] = 1
                n -= 1
        if(n == 0):
            return True
        else:
            return False
a = Solution()
print(a.canPlaceFlowers([0,0,1,0,0], 1))