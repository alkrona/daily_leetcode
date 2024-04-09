def timeRequiredToBuy(tickets:list[int], k :int)->int:
    count =0
    i=0
    while(tickets[k]>0):
        
        i = i if i<len(tickets) else i%len(tickets)
        if tickets[i]>0:
            count+=1
            tickets[i]-=1
        i=i+1
        
    return count
if __name__=="__main__":
    print(timeRequiredToBuy([2,3,2],2))
        