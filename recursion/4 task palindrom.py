def main_func(string: str) -> bool:
    i = 0
    return is_palindrom(string, i)    
    
def is_palindrom(string: str, i) -> bool:
    if i >= len(string)-1:
        return True
    if string[i] != string[len(string)-i-1]:
        return False

    return is_palindrom(string, i+1)

print(main_func('fffffjfffff'))















def is_palindrom_loop(string: str) -> bool:
    for i in range(0, len(string)-1//2):
        if string[i] != string[len(string) - i-1]:
            return False
    return True
#print(is_palindrom_loop('ffgggggggsdfsdff'))
#print(is_palindrom('fffffjf'))