numList=[]
numbers=input("please enter numbers with a space between them:")
numList = [int(item) for item in numbers.split()]


def three_sum(numL):  
    output_set = set()
    for i in range(len(numList)):
            for j in range(i + 1, len(numList)):           
                   for k in range (j+1, len(numList)):
                          if numL[i] + numL[j] + numL[k]== 0 :
                               triplet = tuple(sorted([numL[i], numL[j], numL[k]]))
                               output_set.add(triplet)             
    return list(output_set)       
result=three_sum(numList)
print (result)
