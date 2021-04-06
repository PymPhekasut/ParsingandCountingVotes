escape_word =["a", "an", "the", "am" ,"is", "are", "and", "of", "in" , "on", "with", "from", "to"]

def capitalise(phrase):
    word=""
    cap = phrase.split()
    for x in cap:
        if x not in escape_word:
            word += (" " + x.title())
        else:
            word += (" " + x)

    return word

print(capitalise("I am an educator and a researcher"))
print(capitalise("big data is the future of information technology"))
print(capitalise("He wants to have breakfast with her in the hotel"))
    
