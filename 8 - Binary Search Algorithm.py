



def binarySearch(numberList, findValue):
    
    beginIndex = 0                  # The starting index
    
    # The len() function gives me the length of the list
    # Subtract by 1 to not be outside the range
    endIndex = len(numberList) - 1  # End index 

    # As long as the beginning index is less than ending index
    while beginIndex <= endIndex:

        # This equation helps me find the midpoint of the list
        midpointIndex = beginIndex + (endIndex - beginIndex) // 2

        # Midpoint will help me cut the list in half
        midpointValue = numberList[midpointIndex]

        # If the value was found
        if midpointValue == findValue:
            return midpointIndex     # Return the value

        # If the value < midpoint, that means the 
        # algorithm will look at the lesser half of the list 

        # If the value is less than the midpoint
        elif findValue < midpointValue:
            endIndex = midpointIndex - 1     # Decrease the midpoint by 1

        # If the value > midpoint, that means the 
        # algorithm will look at the greater half of the list 

        # We change the beginIndex to 
        # start at the greater half side of the list

        else:
            beginIndex = midpointIndex + 1

    # If the value was not found in the list
    # Return none
    return None


numberList = [10, 11, 12, 13, 14, 15, 16]

print("All the number in the list:", numberList)

findValue = int(input("What number do you want me to find: "))

# print("You are looking for " + str(findValue) + " in the list.")

print("The number is found at index",  binarySearch(numberList, findValue) )
