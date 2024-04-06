def minRemoveToMakeValid(s:str)->str:
    counter=0
    s_list = list(s)
    i=0
    while(i<len(s_list)):
        #print(f" i is {i} and the word is {s_list}")
        if s_list[i]==')':
            if counter>0:
                counter+=-1
                i+=1
            elif i-1<len(s_list):
                s_list=s_list[:i]+s_list[i+1:]
                
            else:
                s_list=s_list[:i]
                i+=1
        elif s_list[i]=='(':
            counter+=1
            i+=1
        else :
            i+=1
    counter =0
    i=len(s_list)-1
    while(i>=0):
        #print(f" i is {i} and the word is {s_list}")
        
        if s_list[i]=='(':
            if counter>0:
                counter+=-1
                i-=1
            elif i>0:
                s_list=s_list[:i]+s_list[i+1:]
                i-=1
            else:
                s_list=s_list[i+1:]
                i-=1
        elif s_list[i]==')':
            counter+=1
            i-=1
        else :
            i-=1
    if s_list:
        return ''.join(map(str, s_list))
    else :
        return ""
if __name__=="__main__":
    print(minRemoveToMakeValid("))avb(("))