class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        counter =  0 
        index = 1
        compare = nums[0]
        for i in range(1, len(nums) - 1):
            if(nums[i] > compare):
                compare = nums[i]
                counter += 1
                index += 1
            while True:

                if(index < i):
                     compare = nums[i]
                index += 1     
            if(counter == 2):
                return True
            
        return False
    
a = Solution()
print(a.increasingTriplet([1,2,1,3]))