import itertools

A = 'AAAAAABBBBBCCCCCDDDDDEEEEE'

for a in itertools.groupby(A):
    print(str(a))
print('d')
