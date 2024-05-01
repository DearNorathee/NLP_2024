# seems useless: count, repeat, cycle, starmap
# most of it I can do them without the need for these 

# combination => order doesn't matter
# permutation => when the order does matter
from itertools import combinations
from itertools import permutations


letters = [chr(97+i) for i in range(4)]

numbers = list(range(4))

names = ['Corey','Nicole']

ans01 = list(combinations(letters,2))
ans02 = list(permutations(letters,2))

print(ans01)
print(ans02)