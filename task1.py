from collections import defaultdict

def even_odd(l: list) -> dict:
    d = {'even' : [], 'odd': []}
    for i in l:
        if i % 2 == 0:
            d['odd'].append(i)
        else:
            d['even'].append(i)
    return d

def even_odd2(l: list) -> dict:
    d = defaultdict(list)
    for i in l:
       if i % 2 == 0:
            key = 'even'
       else:
            key = 'odd'
       d[key].append(i)
    return d
                                                                                                            
p = [1, 2, 3, 4, 5, 6]
result = even_odd2(p)
print(result)