from heapq import heappush, heappop
    def nbest(ABs):    # no need to pass in k or n
        k = len(ABs)
        n = len(ABs[0][0])
        def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
            A, B = ABs[i] # A_i, B_i
            if p < n and q < n and (i,p,q) not in used:
                heappush(h, (A[p] + b[q], i, p, q, (A[p],B[q])))
                used.add((i, p, q))
        h, used = [], set()                 # initialize
        for i in range(k):  # NEED TO OPTIMIZE
            trypush(i, 0 , 0)
        for _ in range(n): 
            _, i, p, q, pair = heappop(h)
            yield pair     # return the next pair (in a lazy list)
            trypush(i,p+1,q)
            trypush(i,p,q+1)
