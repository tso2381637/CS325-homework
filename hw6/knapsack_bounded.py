

def best(limit,items2):
    items = sum( ([(wt, val,n)]*n for wt, val,n in items2), [])
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        wt, val,n = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    a = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
        if was_added:
            wt, val,n = items[j-1]
            a.append(items[j-1])
            w -= wt
    
  
    rsum = 0
    for i in range(len(a)):
         rsum += a[i][1]   
    c=[0 for x in range(len(items2))]
    for i in range(len(items2)):
        for j in range(len(a)):
            if a[j][0]== items2[i][0] and a[j][1]== items2[i][1] and a[j][2]== items2[i][2]:
                c[i]+=1


    result ={}
    result[limit] = (rsum,c)
    
    return result[limit]

