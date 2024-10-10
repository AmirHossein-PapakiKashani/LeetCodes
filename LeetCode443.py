class Solution:
    def compress(self, chars: list[str]) -> int:
        finalLen = 0
        dynamicLen = 0
        dynamicChar = chars[0]
        if(chars[1] not in  dynamicChar):
            finalLen = finalLen + 1
        if(len(chars) == 1):
            return 1
        for j in range(1,len(chars)):
            if(chars[j] in dynamicChar):
                dynamicChar += chars[j]
                if(len(dynamicChar) == 1):
                    finalLen = finalLen + 1
            else:  
                if(finalLen > )
                dynamicLen = 1 +len(str(len(dynamicChar)))
                finalLen = dynamicLen + finalLen
                dynamicLen = 0
                dynamicChar = chars[j]
            if(j == len(chars) -1):
                dynamicLen = 1 +len(str(len(dynamicChar)))
                finalLen = dynamicLen + finalLen
        return finalLen

a = Solution()
print(a.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))