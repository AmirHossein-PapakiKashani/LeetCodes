class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        i = 0
        j = 0
        zero_Count = 0
        while True:
            if(i <= len(nums) - 1):
                if(nums[i] == 0) :
                    i +=1
                    zero_Count += 1
                    continue
                else:   
                    total *= nums[i]
                    i += 1
            if(zero_Count > 1):
                return [0] * len(nums)
            if(i == len(nums) and j <= len(nums) -1 ):
                if(nums[j] == 0):
                    nums[j] = total
                    j += 1
                if(j == len(nums) ):
                    break
                if(zero_Count == 1):
                    nums[j] = 0
                    j += 1
                else:
                    nums[j] = total // nums[j]
                    j += 1
                
        return  nums
            
                
a = Solution()
print(a.productExceptSelf([1,2,3,4]))