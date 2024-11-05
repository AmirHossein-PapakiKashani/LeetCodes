class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        uniqDict = {}
        for i in range(len(arr)):
            if(i == 0):
                uniqDict[f"{arr[i]}"] = 1
            else:
                if(str(arr[i]) in list(uniqDict.keys())):
                    uniqDict[f"{arr[i]}"] += 1
                else:
                    uniqDict[f"{arr[i]}"] = 1
        if(len(list(set(uniqDict.values())))  == len(list(uniqDict.values()))):
            return True
        else:
            return False
    
a = Solution()
print(a.uniqueOccurrences(arr=[1,2]))       
            