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
    