def find_pairs(target):
    pairs = []  
    for i in range(1, 20):
        for j in range(i + 1, 20):
            if i != target and j != target and  i != j and target % (i + j) == 0:
                pairs.append((i, j))
    return pairs

for target in range(3, 21):
    print(f'Число {target} - {find_pairs(target)}')    
