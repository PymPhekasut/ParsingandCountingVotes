def grep(filename, expr): 
  
    line_number = 0
    list_of_results = []
    # Open the file 
    with open("bigdata.txt", 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if expr in line:
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results
   
# display all lines from bigdata.txt containing Big data
grep("bigdata.txt", "Big data")
# display all lines from bigdata.txt containing technology
grep("bigdata.txt", "technology")
