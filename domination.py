# Created by VerifiedAndHacked ... program 1 of SuperB's event

#function to convert integer to a list
def numToList(n):
    num_list = [int(a) for a in str(n)]
    return num_list

#function to get the most frequent number in a digit
def frequent_dig(List):
    counter = 0
    num = List[0]

    for i in List:
        frequency = List.count(i)
        if frequency > counter:
            counter = frequency
            num = i
    return num
#Returns how many times the frequent number is present in the digit
def Domination_Checker(List,fnum):
    counter = 0
    for i in range(len(List)):
        if List[i] == fnum:
            counter += 1
    return counter


counter = 0
for i in range(10**2022):
    List = numToList(i)
    fnum = frequent_dig(List)
    fnumCount = Domination_Checker(List,fnum)
    leng = len(List)
    if fnumCount > leng//2: 
        counter += 1
#prints the result
print(counter - 1)




