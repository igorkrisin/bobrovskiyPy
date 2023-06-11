class PowerSet:

    def __init__(self):
        self.pow_set = []

    def size(self) -> int:
        return len(self.pow_set)

    def put(self, value) -> None:
        if self.pow_set.count(value) == 0:
            self.pow_set.append(value)

    def get(self, value) -> bool:
        if value in self.pow_set:
            return True
        return False

    def remove(self, value) -> bool:
        for i in range(0, len(self.pow_set)):
            if value == self.pow_set[i]:
                self.pow_set.pop(i)
                return True
        return False

    def intersection(self, set2: 'PowerSet'):
        set_summ: PowerSet = PowerSet()
        for i in range(0, len(self.pow_set)):
            if self.pow_set[i] in set2.pow_set:
                set_summ.put(self.pow_set[i])
        if len(set_summ.pow_set) > 0:
            return set_summ.pow_set
        return set_summ.pow_set

    def union(self, set2: 'PowerSet'):
        for i in range(0, set2.size()):
            self.put(set2.pow_set[i])
        return self.pow_set

    def difference(self, set2: 'PowerSet'):
        summ_set: PowerSet = PowerSet()
        for i in self.pow_set:
            if i not in set2.pow_set:
                summ_set.put(i)
        return summ_set.pow_set

    def issubset(self, set2: 'PowerSet'):
        summ_set: PowerSet = PowerSet()
        for i in self.pow_set:
            if i in set2.pow_set:
                summ_set.put(i)
        if summ_set.size() == set2.size():
            return True
        return False