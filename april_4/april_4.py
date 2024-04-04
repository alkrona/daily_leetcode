def maxDepth(s:str)->int:
    max_count,counter = 0,0
    for char in s:
        if char =='(':
            counter+=1
            max_count=max(max_count,counter)
        elif char ==')':
            counter-=1
        else:
            pass
    return max_count
if __name__=='__main__':
    print(maxDepth("(1+(2*3)+((8)/4))+1"))