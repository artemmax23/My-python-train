def brackets_validation(str1: str) -> bool:
    brackets_dict = {'(': ')', '[': ']', '{': '}'}
    sb = []
    for s in str1:
        if s in brackets_dict.keys(): 
            sb.append(s)
        elif (len(sb) == 0):
            return False
        elif (s in brackets_dict.values()) and (s != brackets_dict[sb.pop()]):
            return False
    if len(sb) == 0:
        return True
    else:
        return False
        
print(brackets_validation("({[]})")) 