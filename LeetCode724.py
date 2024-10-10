class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        next = 0 
        previous = 0
        for i in range(1,len(nums)):
            previous = previous + nums[i -1]
            for j in range(i+1, len(nums)):
                
                next = next + nums[j]
                if(i == 0 and next == 0):
                    return i
                if(j == len(nums) - 1 and previous == 0):
                    return j
                
            if(previous == next):
                return i
            next = 0
            
        return -1
a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))