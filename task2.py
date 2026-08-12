from collections import Counter

def duplicates(l: list) -> list:
    return dict(filter(lambda item: item[1] > 1, Counter(l).items())).keys()

def dupl1(l:list) -> list:
    return [item for item, value in Counter(l).items() if value > 1]        

dupl = lambda l: dict(filter(lambda item: item[1] > 1, Counter(l).items())).keys()
      
ls = ['a', 'b', 'c', 'c', 'd',  'a']
print(duplicates(ls))
print(dupl(ls))
print(dupl1(ls))