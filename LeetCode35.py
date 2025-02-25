import bisect
class Solution:
    
    def binary_search_bisect(arr, x):
        i = bisect.bisect_left(arr, x)
        if i != len(arr) and arr[i] == x:
            return i
        else:
            return i + 1
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.binary_search_bisect(nums, target)
         
