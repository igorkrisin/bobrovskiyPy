#number = 00010
b = 0b0001

b |= 0b1010
#m = b'01010'
#bitarray('11010111')
#f = number | m
print(bin(b))

b = 0b000000000000000000000000000000000
c = 0b000000000000000000000000000000001
b |= c
b <<= 3
print(bin(b))
print(type(b))

f = '000000000000000000000000000000000'
print(bin(int(f)))
