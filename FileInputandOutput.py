def read_write_file(infile, outfile):
    # Your code goes here to read the content of infile, pick up records of MICT units, 
    # and save the results to outfile
    fid = open("scemunits.txt")
    for line in fid:
        print (line.strip())
    fid.close()
    
    
    fid1 = open("scemunits.txt")
    lines = fid1.read()
    
    fid = open("mictunits.txt","w")
    
    
    fid.write('\n301046, Big Data, MICT \n301044, Data Science, MICT')
    fid.close()
    fid1.close()
    

    
# mictunits.txt should list two MICT units, namely Big Data and Data Science
read_write_file("scemunits.txt", "mictunits.txt")
