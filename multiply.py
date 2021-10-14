def multiply_list(myList):

	# Multiply elements one by one
    result = 1
    for i in myList:
          try:
               int(i)
          except:
               return False

    for i in myList:
         result = result * i
         
    return result

#input your willing number in the list here

yourList = []
yourList = list(map(int,input("Input: ").split()))
print("Input: ",yourList)


print("Output: ",multiply_list(yourList))