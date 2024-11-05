# def xor_func(n):
#     numbers = list(range(n)) 
#     valid_numbers=[]
#     valid_numbers=numbers.copy()

#     for num in numbers:
#         for other in numbers:
#             result = num ^ other 
#             if not(0 <= result < n): 
#                 valid_numbers.remove(num)
#                 print(num,other,result  )
#                 break 
#     return valid_numbers




# mm = int(input())
# for i in range(mm):
#     n = int(input())
#     print(xor_func(n)) 
    
    
    
    
    
    
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2

    return True

def xor_func(n):
    if n%2 == 1:
        return 1
    elif isPowerOfTwo(n):
        return n
    else:
        return 2

mm = int(input())
ans=[]
for i in range(mm):
    n = int(input())
    ans+=[xor_func(n)]
    
#print("ans:")
for i in ans:
    print (i)