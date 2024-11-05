class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        fisrtDict = set(nums1)
        secondDict =  set(nums2)
        listDistinc = []
        listDistinc.append(fisrtDict - secondDict)
        listDistinc.append(secondDict - fisrtDict)
        return listDistinc
        
        