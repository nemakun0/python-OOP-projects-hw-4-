numList=[]
numbers=input("please enter numbers with a space between them:")
numList = [int(item) for item in numbers.split()]
target=int(input("please enter target:"))

def two_sum(numL,trg):  
    output=[]
    for i in range(len(numList)):
            for j in range(i + 1, len(numList)):
                if numL[i] + numL[j] == trg:
                    output.append([i,j]) 
             
    return output         

result=two_sum(numList,target)
print (result)
