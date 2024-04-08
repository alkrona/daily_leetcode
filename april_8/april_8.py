def countStudents(students:list[int],sandwiches:list[int])->int:
    count_ones=0
    count_zeros=0
    for student in students:
        if student==1:
            count_ones+=1
        else:
            count_zeros+=1
    for sandwich in sandwiches:
        if sandwich==1:
            if count_ones>0:
                count_ones-=1
            else:
                return count_zeros
        else :
            if count_zeros>0:
                count_zeros-=1
            else:
                return count_ones
    return 0
if __name__ =='__main__':
    print(countStudents([1,1,0,0],[0,1,0,1]))
