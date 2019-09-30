class Permutation:

    def __init__(self, seq):
        """a list of the numbers from 0 up to some positive integer must be passed as
        seq parameter of the constructor"""
        self.seq = [int(seq[i]) for i in range(len(seq))]
        self.perm_dict = {i:self.seq[i] for i in range(len(self.seq))}

    @classmethod
    def from_dict(cls, perm_dict):
        """the method allows creating the permutation object from a dictionary"""
        seq = []
        for i in range(len(perm_dict)):
            seq.append(perm_dict[i])
        return cls(seq)

    def __mul__(self, other):
        """the method returns the composition of two permutations"""
        self_dict = self.perm_dict
        other_dict = other.perm_dict
        if len(self_dict) != len(other_dict):
            return None
        new_dict = {}
        for i in range(len(self_dict)):
            new_dict[i] = self_dict[other_dict[i]]
        return Permutation.from_dict(new_dict)

    def inverse(self):
        """the method returns the inverse of the permutation"""
        self_dict = self.perm_dict
        new_dict = {}
        for key, item in self_dict.items():
            new_dict[item] = key
        return Permutation.from_dict(new_dict)

    def canonical_cycle_notation(self):
        """the method returns the permutation in the canonical cycle notation"""
        self_dict = self.perm_dict
        support = set()
        cycles = []

        while len(support) < len(self.seq):
            stop = max(set(self.seq) - support)
            if self_dict[stop] == stop:
                cycles.append([stop])
                support.add(stop)
            else:
                orbit = self_dict[stop]
                cycle = [stop, orbit]
                while orbit != stop:
                    orbit = self_dict[orbit]
                    if orbit != stop:
                        cycle.append(orbit)
                cycles.append(cycle)
                support |= set(cycle)
        cycles.sort()

        return tuple([tuple(cycle) for cycle in cycles])

    def type_list(self):
        """the function returns the permutation type as a list"""
        lengths = [len(cycle) for cycle in self.canonical_cycle_notation()]
        res = [(val, lengths.count(val)) for val in range(1, len(self.seq) + 1) if lengths.count(val) != 0]
        res.sort()
        return res

    def type(self):
        """the function returns the permutation type as a string"""
        return "[{}]".format(", ".join([f"{val}^{num}" for val, num in self.type_list()]))

    def sign(self):
        """the method returns the sign of the permutation"""
        sign = 1
        for cycle in self.canonical_cycle_notation():
            if len(cycle) % 2 == 0:
                sign = -sign
        return sign

    def __str__(self):
        line_1 = " ".join([str(i) for i in sorted(list(self.perm_dict.keys()))])
        line_2 = " ".join([str(self.perm_dict[i]) for i in range(len(self.perm_dict))])
        return " /{}\ \n \{}/".format(line_1, line_2)








