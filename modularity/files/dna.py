class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'

    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    @property
    def adenines(self):
        return self.sequence.count(DNA.ADENINE)

    @property
    def cytosines(self):
        return self.sequence.count(DNA.CYTOSINE)

    @property
    def guanines(self):
        return self.sequence.count(DNA.GUANINE)

    @property
    def thymines(self):
        return self.sequence.count(DNA.THYMINE)

    def __add__(self, other):
        new_sequence = ''.join(
            [max(b1, b2) for b1, b2 in zip(self.sequence, other.sequence)]
        )
        return DNA(new_sequence)

    def stats(self) -> tuple[float]:
        total_bases = len(self.sequence)
        adenines_rate = self.adenines / total_bases * 100
        cytosines_rate = self.cytosines / total_bases * 100
        guanines_rate = self.guanines / total_bases * 100
        thymines_rate = self.thymines / total_bases * 100
        return adenines_rate, cytosines_rate, guanines_rate, thymines_rate

    def __mul__(self, other):
        new_sequence = ''.join(
            [b1 for b1, b2 in zip(self.sequence, other.sequence) if b1 == b2]
        )
        return DNA(new_sequence)


dna1 = DNA('ATTAGCTCCGTAACT')
dna2 = DNA('TAACGCTTAGTAGGC')

print(dna1.adenines)
print(dna1.cytosines)
print(dna1.guanines)
print(dna1.thymines)

print(dna1 + dna2)

print(dna1.stats())

print(dna1 * dna2)
