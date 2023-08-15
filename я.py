print("длина объекта1: ", len("hello Alise"), " букв")
a8 = "a"
l5="l"
i9="i"
s1='s'
e3="e"


print("длина объекта2: ", len(a8+l5+i9+s1+e3), " букв")
print("o"+"2")


def str_len(string):
    i = 0
    while string[i] != '/n':
        i += 1
    return string[i]

