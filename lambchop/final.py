
def fibbo(n):
    	stingy = [1, 1]
	i = 2
	while ( sum(stingy) <= n):
		stingy.append(stingy[i-1] + stingy[i-2])
		i += 1
	print stingy[:-1]
	return len(stingy[:-1])

def twos(n):
	powers = [1]
	i = 1
	while ( sum(powers) <= n ):
		powers.append(2**i)
		i += 1
	remainder = n - sum(powers[:-1])
	if ( remainder >= (powers[i-2] + powers[i-3]) ):
		powers.insert(-1, remainder)
	print powers[:-1] 
			
	return len(powers[:-1])

def answer(total):
	if total in [0,1, 2, 3]:
		print "Answer: %d " % 0
		return 0
	stingy = fibbo(total)
	generous = twos(total)
	print "Answer: %d " % (stingy-generous)
	return stingy - generous
answer(13)
