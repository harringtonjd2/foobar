#!/usr/bin/python

def answer(total):
	stingy, generous = [1], [1]
	total -=1
	stingy_total, gen_total = total, total
	i = 0
	while stingy_total >= 0:
		maximum = generous[i]*2
		minimum = (stingy[i] + stingy[i-1]) if i>0 else stingy[i]
		if (stingy_total - minimum > 0):
			stingy.append(minimum)
			stingy_total -= minimum
		if (gen_total - maximum > 0):
			generous.append(maximum)
			gen_total -= maximum
		else:
			break
		i+=1
	print "Generous: " + str(generous)
	print "Stingy: " + str(stingy)
	print "Answer: %d" % (len(stingy) - len(generous))

answer(10)
answer(143)

