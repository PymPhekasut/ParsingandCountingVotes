def count_votes(votes):
    VoteCount = {}
    
    for c in votes.casefold().replace(',','').replace(" ", ""):
        if c not in VoteCount:
            VoteCount[c] = 1
        else:
            VoteCount[c] += 1  

        total =  len(''.join(votes.replace(',',"").replace(" ", "")))

    print("Vote rejected: ", total,"votes in total", VoteCount)

votes = "N , Y, Y,N,n , N , N , N ,n ,y, n,N,Y, y,Y,N , N , n ,y, N"
count_votes(votes)
