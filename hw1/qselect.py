import random
def qselect(order, array):
    pivot = array[random.randint(0,len(array)-1)]
    right = []
    left = []
    array.remove(pivot)
    for e in array:
        if e<pivot:
            left.append(e)
        else:
            right.append(e)
    if order< len(left)+1:
        return qselect(order,left)
    elif order == len(left)+1:
        return pivot
    else:
        return qselect(order-(len(left)+1),right)

