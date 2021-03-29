# function definitions
def mysum(xlist):
    sum = 0
    for i in xlist:
        sum = sum + i
    
    return sum
 
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
xlist = range(10)

#print("sum= ", mysum(list1)) 


def mymax(xlist):

    # Assume first number in list is largest and initially assign to max 
    max = xlist[0] 
   
    # maximize value to max 
    for x in xlist: 
        if x > max : 
             max = x 
      
    return max
  
# Driver code 
xlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

#print("max= ", mymax(list2)) 

def mymin(xlist):
    
# Assume first number in list is minimum and initially assign to min
    min = xlist[0] 

    # minimize value to min 
    for x in xlist: 
        if x < min : 
             min = x 
      
    return min
  
# Driver code 
xlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

#print("min= ", mymin(list3)) 

print("Sum: ",mysum(xlist),"Max: ", mymax(xlist),"Min: ", mymin(xlist))
