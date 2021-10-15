def multiply_list(Lalisalist):
	# Multiply the Numbers in the list one by one
    result = 1
    for i in Lalisalist:
          try:
               int(i)
          except:
               return False

    for i in Lalisalist:
         result = result * i
         
    return result

#Insert Desired numbers
yourList = []
yourList = list(map(int,input("Input: ").split()))
print("Input: ",yourList)
print("Output: ",multiply_list(yourList))