from __future__ import annotations


class DNA:
    def __init__(self, sequence: str):
        ...

    def __str__(self):
        ...

    @property
    def adenines(self):
        ...

    @property
    def cytosines(self):
        ...

    @property
    def guanines(self):
        ...

    @property
    def thymines(self):
        ...

    def __add__(self, other: DNA):
        ...

    def __len__(self):
        ...

    def stats(self) -> dict[str, float]:
        ...

    def __mul__(self, other):
        ...

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        ...

    def dump_to_file(self, path: str) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    def __setitem__(self, index: int, base: str) -> None:
        ...
