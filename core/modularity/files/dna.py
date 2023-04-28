from __future__ import annotations


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

    def __add__(self, other: DNA):
        new_sequence = ''.join([max(b1, b2) for b1, b2 in zip(self.sequence, other.sequence)])
        if len(self) > len(other):
            new_sequence += self.sequence[len(other) :]
        elif len(other) > len(self):
            new_sequence += other.sequence[len(self) :]
        return DNA(new_sequence)

    def __len__(self):
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        total_bases = len(self.sequence)
        adenines_rate = self.adenines / total_bases * 100
        cytosines_rate = self.cytosines / total_bases * 100
        guanines_rate = self.guanines / total_bases * 100
        thymines_rate = self.thymines / total_bases * 100
        return {
            DNA.ADENINE: adenines_rate,
            DNA.CYTOSINE: cytosines_rate,
            DNA.GUANINE: guanines_rate,
            DNA.THYMINE: thymines_rate,
        }

    def __mul__(self, other):
        new_sequence = ''.join([b1 for b1, b2 in zip(self.sequence, other.sequence) if b1 == b2])
        return DNA(new_sequence)

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        f = open(path)
        return cls(f.read().strip())

    def dump_to_file(self, path: str) -> None:
        f = open(path, 'w')
        f.write(str(self))

    def __getitem__(self, index: int) -> str:
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        if base not in (DNA.ADENINE, DNA.THYMINE, DNA.GUANINE, DNA.CYTOSINE):
            base = DNA.ADENINE
        aux_seq = list(self.sequence)
        aux_seq[index] = base
        self.sequence = ''.join(aux_seq)
