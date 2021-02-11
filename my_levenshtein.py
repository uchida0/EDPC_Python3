#重み付きレーベンシュタイン、Damerau-Levenshtein

def weighted_levenshtein(a, b, insert = 1, delete=1, substitute=1):
    if a == "" or b == "":
        print("str1 is null or str2 is null")
        exit(0)


    a_length = len(a)
    b_length = len(b)
    
    dist = [[0]*(b_length+1) for _ in range(a_length+1)]

    for i in range(a_length+1):
        dist[i][0] = i * delete
    for j in range(b_length+1):
        dist[0][j] = j * insert
    
    
    for i in range(1, a_length):
        for j in range(1, b_length):

            if a[i-1] == b[j-1]:
                substitute_cost = 0
            else:
                substitute_cost = substitute
            
            dist[i][j] = min( dist[i-1][j]+delete, dist[i][j-1]+insert, dist[i-1][j-1]+substitute_cost )

    """
    for d in dist:
        print(d)
    """

    return dist[a_length][b_length]


def damerau_levenshtein(a, b):
    if a == "" or b == "":
        print ("str1 is null or str2 is null")
        exit(0)
    
    a_length = len(a)
    b_length = len(b)

    if a_length == 0:
        return b_length
    if b_length == 0:
        return a_length
    
    dist = [[0]*(b_length+1) for _ in range(a_length+1)]

    for i in range(a_length):
        dist[i][0] = i
    for j in range(b_length):
        dist[0][j] = j

    
    insert = 1
    delete = 1
    
    
    for i in range(1, a_length+1):
        for j in range(1, b_length+1):
            
            if a[i-1] == b[j-1]:
                substitute_cost = 0
                swap_cost = 0
            else:
                substitute_cost = 1
                swap_cost = 1
            
            dist[i][j] = min( min(dist[i-1][j]+delete, dist[i][j-1]+insert), dist[i-1][j-1]+substitute_cost)

            if i>1 and j>1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:
                dist[i][j] = min(dist[i][j], dist[i-2][j-2]+swap_cost)
    
    """
    for d in dist:
        print(d)
    """

    return dist[a_length][b_length]

