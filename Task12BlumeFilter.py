class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.b_filter = 0b1 << f_len
        self.val = bin(self.b_filter)


    def hash1(self, str1):
        rand = 17
        ind = 0
        res = 0
        for c in str1:
            code = ord(c)
            ind = (ind * rand + code)
            res = ind % self.filter_len
        return 0b1 << (self.filter_len - 1 - res)



    def hash2(self, str1):
        rand = 223
        ind = 0
        res = 0
        for c in str1:
            code = ord(c)
            ind = (ind * rand + code)
            res = ind % self.filter_len
        return 0b1 << (self.filter_len - 1 - res)

    def add(self, str1):
        self.b_filter |= self.hash1(str1)
        self.b_filter |= self.hash2(str1)

    def is_value(self, str1):
        index1 = self.filter_len - len(bin(self.hash1(str1))) + 5
        index2 = self.filter_len - len(bin(self.hash2(str1))) + 5
        return bin(self.b_filter)[index1] == '1' and bin(self.b_filter)[index2] == '1'


bloomF: BloomFilter = BloomFilter(32)

bloomF.add('0123456789')
bloomF.add('1234567890')
bloomF.add('2345678901')
bloomF.add('3456789012')
bloomF.add('4567890123')
bloomF.add('5678901234')
bloomF.add('6789012345')
bloomF.add('7890123456')
bloomF.add('8901234567')
bloomF.add('9012345678')

print(bloomF.is_value('0123456789'))
print(bloomF.is_value('1234567890'))
print(bloomF.is_value('2345678901'))
print(bloomF.is_value('3456789012'))
print(bloomF.is_value('4567890123'))
print(bloomF.is_value('5678901234'))
print(bloomF.is_value('6789012345'))
print(bloomF.is_value('7890123456'))
print(bloomF.is_value('8901234567'))
print(bloomF.is_value('9012345678'))

print(bloomF.is_value('333334445556'))





print('bv', bin(bloomF.b_filter))



