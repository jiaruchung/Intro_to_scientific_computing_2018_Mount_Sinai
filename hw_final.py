def complement(s):
	dec = {'A': 'T', 'C': 'G' , 'T': 'A', 'G': 'C'}
	return ''.join([dec.get(i, None) for i in list(s)])


## 5
input = 'ATTCGATCC'
print('5: {} -> {}'.format(input, complement(input)))

## 6
input = 'TCAATGCATGCGGGTCTATATGCAT'
cmp = complement(input)
input = cmp[:]
ret_final = []

for i in range(len(input) - 1):
	#import pdb; pdb.set_trace()
	k = 2
	tmp1 = input[i: i+k]
	tmp2 = complement(tmp1[::-1])
	while (tmp2 in input[i:]) and (len(tmp2) < len(input[i:])):
		ret = input[i:].find(tmp2+ tmp1)
		if ret > -1:
			print(i + ret, len(tmp1 + tmp2), tmp2+ tmp1)
			ret_final.append((i + ret, len(tmp1 + tmp2)))

		k += 1
		tmp1 = input[i: i+k]
		tmp2 = complement(tmp1[::-1])

print(sorted(list(set(ret_final))))
