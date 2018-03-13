
def getParent(node, h):
    size = 2**h-1 
    if ( node == size ):
        return -1
    rank = size
    index = size
    while (rank > 0):
        left = index - (rank + 1)/2
        right = index - 1

        if (node == left or node == right):
            return index
        index = left if (node < left) else right
        rank = (rank-1)/2
    return index

def answer(query, h):
    parents = []
    for node in query:
        parents.append(getParent(node, h))

    print parents

query = [19, 14, 28]
h = 5

answer(query, h)
