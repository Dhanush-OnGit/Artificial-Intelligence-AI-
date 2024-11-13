from sys import maxsize
from itertools import permutations
v= 4
gragh =[[10,10,15,20],[10,0,35,20],
        [23,17,0,21],[20,25,30,0]]
s=0
def salesmanprobles(gragh,s):
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    best_tour = None
    next_permutaion = permutations(vertex)
    for i in next_permutaion:
        current_pathwight = 0
        k=s
        for j in i:
            current_pathwight += gragh[k][j]
            k=j
        current_pathwight += gragh[k][s]
        if current_pathwight < min_path:
            min_path = min(min_path,current_pathwight)
            best_tour = [s] + list(i) + [s]
    return min_path,best_tour
min_path,best_tour = (salesmanprobles(gragh,s))
print("min path : ",min_path)
print("best path : ",best_tour)
        