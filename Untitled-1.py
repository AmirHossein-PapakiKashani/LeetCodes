class Solution:
    
    def compress(self, chars):
       end=len(chars)-1
       start=end
       index=''
       
       while -1<=start:
           index=chars[end]
           if chars[start]==index:
               start-=1
               continue
           chars[start+1:end+1]=[index]
           if end-start > 1:
               chars=chars[:start+2]+list(str(end-start))+chars[start+2:]
           end=start
    
       print(chars)
       return len(chars)
        
       
s=Solution()
a=s.compress(["a","a","b","b","c","c","c"])
print(a)
