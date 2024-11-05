class Solution:
    def canPlaceFlowers(self, flowerbed, n) :
        # Initialize count to 1 to handle potential empty space at the start
        count = 1
        # Initialize result to store the number of new flowers that can be planted
        res = 0
        
        # Traverse each plot in the flowerbed
        for i in flowerbed:
            if i == 0:
                # Increment count for each empty plot
                count += 1
            else:
                # Calculate number of flowers that can be planted in the current segment of empty plots
                res += int((count - 1) / 2)
                # Reset count when encountering a planted plot
                count = 0
        
        # Final calculation for the last segment of empty plots
        res += int(count / 2)
        
        # Return True if the number of new flowers that can be planted is at least n, otherwise False
        return res >= n
    
    
S=Solution()
print(S.canPlaceFlowers(flowerbed=[1,0,0,0,1],n=55))
a = Solution()
print(a.canPlaceFlowers([1,0,0,0,1,0,0], 2))