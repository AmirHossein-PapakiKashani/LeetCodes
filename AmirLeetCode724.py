class Solution:
    def pivotIndex(self, nums) :
        total=sum(nums)
        current_total=0
        
        for index,i in enumerate(nums):
            if current_total==total-current_total:
                return index
            current_total+=i
        return -1
