# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 10:04:57 2023

@author: Heng2020
"""


def powerset(lst, n=None):
    powerset_list = []

    if isinstance(n, int):
        n_values = [n]
    elif isinstance(n, list):
        n_values = n
    elif isinstance(n, str):
        if n.startswith("<"):
            if n.startswith("<="):
                cutoff = int(n[2:])
                n_values = list(range(1, cutoff + 1))
            else:
                cutoff = int(n[1:])
                n_values = list(range(1, cutoff))
        elif n.startswith(">"):
            if n.startswith(">="):
                cutoff = int(n[2:])
                n_values = list(range(cutoff, len(lst) + 1))
            else:
                cutoff = int(n[1:])
                n_values = list(range(cutoff, len(lst) + 1))
        else:
            n_values = None
    else:
        n_values = None
    
    for i in range(1, 2**len(lst)):
        subset = [lst[j] for j in range(len(lst)) if (i & (1 << j)) > 0]
        
        if n_values is not None and len(subset) not in n_values:
            continue
        
        powerset_list.append(tuple(subset))
    
    return powerset_list

list01 = [1, 2, 3]
list02 = [1,2]
list03 = [1,2,3,4,5]


res01 = powerset(list01)
res02 = powerset(list02)
res03 = powerset(list03,n="<=3")

print(res01)
print(res02)
print(res03)
print(len(res03))
