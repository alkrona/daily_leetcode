def makeGood(s:str)->str:
    new_s =list(s)
    i=0
    while(i<=len(new_s)-2):
        
        if new_s[i].isupper() and new_s[i+1].islower() and new_s[i]==new_s[i+1].upper():
            new_s = new_s[:i] + new_s[i+2:]
            
            
            i=0
        elif new_s[i].islower() and new_s[i+1].isupper() and new_s[i]==new_s[i+1].lower():
            
            new_s = new_s[:i] + new_s[i+2:]
            
            i=0
        else :
            i+=1
    if new_s:
        return ''.join(map(str, new_s))
    else:
        return ""
if __name__=="__main__":
    print(makeGood("leEeetcode"))