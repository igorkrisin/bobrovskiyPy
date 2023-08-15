def is_palindrom(string: str) -> bool:
    if len(string) == 0:
        return True
    if len(string) == 1:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return is_palindrom(string[1:len(string)-1])

print(is_palindrom('fffg'))