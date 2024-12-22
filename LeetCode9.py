import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringifyNumber = str(x)
        leftString = ""
        rightString = ""
        if len(stringifyNumber) % 2 == 0 :
            for i in range(len(stringifyNumber)) :
                if i + 1 <= len(stringifyNumber) // 2:
                    leftString += stringifyNumber[i]
                else :
                    rightString += stringifyNumber[i]
            if leftString == rightString[::-1] : 
                return True 
            else: 
                return False    
        elif 0 < x <= 9 : return True
        elif x < 0 : return False
        else:
            for i in range(len(stringifyNumber)) : 
                print(math.ceil(len(stringifyNumber) / 2) )
                if i + 1 < math.ceil(len(stringifyNumber) / 2) :
                    leftString += stringifyNumber[i]
                elif i +1 == math.ceil(len(stringifyNumber) / 2):
                    continue
                else: 
                    rightString += stringifyNumber[i]
            if leftString == rightString[::-1] : 
                return True 
            else: 
                return False
            
a = Solution()
print(a.isPalindrome(1001))