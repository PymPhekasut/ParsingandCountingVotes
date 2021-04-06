def create_wordcount_dict(filename):
    # Your code goes here to create and return a dictionary
    
        file = open("bigdata.txt","r")
        count = 0
        for line in file:
            words = line.split(" ")
            count += len(words)
        file.close()
        
        print("Number of words in a Text File : ", count)
        
        frequency = {}

        file = open("bigdata.txt","r")
        #convert the string of the document in lowercase and assign it to text_string variable.
        text =    file.read().lower()
        pattern = re.findall(r'\b[a-z]{,}\b', text)
        for word in pattern:
            count = frequency.get(word,0)
            frequency[word] = count + 1
            
        sorted_keys_list = sorted(frequency.items(), key = lambda x:x[1],reverse=True)
        for key in sorted_keys_list[:10]:
             print(key)
        

create_wordcount_dict("bigdata.txt")

  
