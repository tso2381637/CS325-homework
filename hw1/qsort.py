def sort(a):
    if not a:
        return a
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]


def print_node(a, result):
    if len(a) == 3:
        print_node(a[0], result)
        result.append(a[1])
        print_node(a[2], result)


def sorted(a):
    result = []
    print_node(a, result)
    print(result)


def insert(a, value):
    if a == value:
        return 0
    if len(a) == 3:
        if value < a[1]:
            if a[0] != []:
                insert(a[0], value)
            else:
                a[0] = value
        elif value > a[1]:
            if a[2] != []:
                insert(a[2], value)
            else:
                a[2] = value

def search(a, value):
    if len(_search(a))==3:
        if a[1]==value:
            return True
        if search(a[0],value):
            return True
        if search(a[2],value):
            return True
    else:
        if a==value:
            return True
    return False

def _search(a,value):
    if type(a)==list:
        if len(a)==3:
            if value == a[1]:
                print(a)
            elif value < a[1]:
                _search(a[0],value)
            else:
                _search(a[2],value)
    else:
        print(a)


#