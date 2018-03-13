
def fibbo(n):
    a, b = 1, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

def twos(n):
    for _ in xrange(n):
        yield 2**_

def answer(total_lambs):
	generous_sum = 0
	stingy_sum = 0
	gen_count = 0
	stin_count = 0
	for i in fibbo(10**3):
	    if stingy_sum < total_lambs:
	        stingy_sum += i
		stin_count +=1
		print i,
	    else:
		stin_count -=1
		break
	print ""
	for i in twos(10**3):
	    if generous_sum < total_lambs:
	        generous_sum += i
		gen_count += 1
		print i,
	    else:
		gen_count -=1
		break
	print ""
	diff = stin_count - gen_count
	if (generous_sum == total_lambs or stingy_sum == total_lambs):
		diff += 1
	print diff
answer(10**8)
