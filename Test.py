class Solution:
    def decodeString(self, s: str) -> str:
        final_string=""
        string= ""
        
        stack=[]
        counter=0
        temp_num=""
        temp_str=""
        
        for i in s:
            print('\ni=',i,)
            print(string,'string')
            print(temp_str,'temp_str')
            print(temp_num,'temp_num')
            print(stack,'stack','\n')
            
            if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0' :
                if len(temp_str)>0:
                    stack.append(temp_str)
                    temp_str=""
                temp_num+=i
                
                # continue
            elif i=='[':
                counter+=1
                stack.append(int(temp_num))
                
                temp_num=""
            
            elif i==']':
                if len(temp_str)>0:
                    stack.append(temp_str)
                
                counter-=1
                temp_str=stack.pop()
                temp_num=stack.pop()
                string = temp_num * (temp_str + string)
                temp_num=""
                temp_str=""
                
                if  counter==0:
                    final_string += string
                    string = ""
                    
            elif i.isalpha:
                temp_str+=i
            # string=''.join(stack)
            
            else:
                temp_str+=i
            
            if counter==0 and len(stack)>0:
                final_string+=stack.pop()
        return final_string + temp_str
    
S=Solution()
print(S.decodeString("2[2[y]pq4[2[jk]e1[f]]]ef"))
print("yypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")








if str(i).isdigit(): 
                        if current_Character  != "":
                            current_String = current_Character + final
                            current_String = int(myStack.pop()) * current_String
                            current_Character = ""
                            if final == "": 
                                final = final + current_String
                                current_String = ""
                                myList.append(final)
                                final = ""
                            else:
                                final = ""
                                final = final + current_String
                                current_String = ""
                        else:
                            current_String = int(myStack.pop()) * current_Character
                            current_Character = ""
                            final = final + current_String
                            current_String =""
                            
                    else:
                        current_Character =   myStack.pop() + current_Character
                    