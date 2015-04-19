same_block=[1,2,3,10,11,12,19,20,21]

diff_block=[]
diff_block.append(same_block)

starting=[4,7,28,31,34,55,58,61]

for num in starting:
	te=same_block[:]
	diff=num-1
	te=[x+diff for x in same_block]
	diff_block.append(te)

print diff_block

for block in diff_block:
	if 13 in block:
		print block
