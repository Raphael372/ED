def max(e, d, v):
    if e == d:
        return v[d]
    else:
        m = (e+d)/2
        maxe = max(e, m, v)
        maxd = max(m+1, d, v)
        if maxe >= maxd:
            return maxe
        else:
            return maxd
