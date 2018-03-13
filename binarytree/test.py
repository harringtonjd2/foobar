
def recursive_depth(node, h):
    if node == 2**h - 1:
        return 0
    else:
        bit = format(int(node), '08b') 
        bit = bit[::-1]
        bit = int(bit[h-1])
        return 1 + recursive_depth(node-(2**(h-1)-1)*bit, h-1)
'''
for i in range(1,64):
    print "Depth of %d is %d " % (i, recursive_depth(i, 6))
'''

def findParent(child, h):
    depth = h - recursive_depth(child, h)
    print "If left: %d" %(child + 2**(depth))
    print "If right: %d" % (child + 1)


findParent(6, 3)
