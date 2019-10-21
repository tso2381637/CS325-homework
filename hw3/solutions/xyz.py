#!/usr/bin/env python

def _find(a):
    
    a.sort()
    
    for i, z in enumerate(a):
        j, k = 0, len(a)-1
        while j < k:
            s = a[j] + a[k]
            if j == i or s < z:
                j += 1
            elif k == i or s > z:
                k -= 1
            else: # s==z
                yield (a[j], a[k], z)
                j += 1
                k -= 1

find = lambda a: list(_find(a))

if __name__ == "__main__":
    
    print(find([1, 4, 2, 3, 5]))
    print(find([1]))
    print(find([-5, -2, -3, 3, 5, 2]))
    print(find([]))
