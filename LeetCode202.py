class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10 :
            n = n ** 2
        a = list(map(int, str(n)))
        s = 0
        
        while True :   
            for i in a:
                s += i ** 2
            if  s == 4 :
                return False
            a = list(map(int, str(s)))
            s = 0
            if len(a) == 1 : 
                if a[0] == 1:
                    return True
                else :
                    return False

a = Solution()
print(a.isHappy(1111111))