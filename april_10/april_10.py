def deckRevealedIncreasing(deck:list[int])->list[int]:
    
    deck.sort(reverse=True)
    
    accum_list =[]
    for element in deck:
        temp_list=[]
        temp_list.append(element)
        if len(accum_list)>0:
            temp_list.append(accum_list[-1])
            if len(accum_list)>1:
                for index in range(len(accum_list) -1):
                    temp_list.append(accum_list[index])
        accum_list=temp_list
    return accum_list
if __name__=='__main__':
    print(deckRevealedIncreasing([1,1000]))