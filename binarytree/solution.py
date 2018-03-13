

h = 3
root = 2**h - 1

tree1 = list(range(8))
del(tree1[0])
print tree1
rows = []
for i in range(h):
	rows.append([])	
rows[0] = [*tree1[i:i+2] for i in range(0, root-1, 3)]
print rows
