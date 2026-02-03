from itertools import permutations
s="1010"
s1=["".join(i)for i in set(permutations(s))]
mini=min(s1)
print(int(mini,2))


