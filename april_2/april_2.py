def isIsomorphic(s:str, t :str)->bool:
    dict ={}
    for index,char in enumerate(s):
        if char not in dict:
            #print(f"{char}not in here ")
            dict[char]= t[index]
        elif char in dict:
            #print(f"{char }in here")
            if dict[char]==t[index]:
                pass
            else:
                return False
    return True
if __name__ =="__main__":
    print(isIsomorphic("egg","add")) 