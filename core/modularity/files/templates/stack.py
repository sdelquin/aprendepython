from __future__ import annotations


class IntegerStack:
    def __init__(self, *, max_size: int = 10):
        ...

    def push(self, item: int) -> bool:
        '''Si la pila está llena retornar False, en otro caso retornar True'''
        ...

    def pop(self) -> int:
        '''Extraer el elemento que está en el TOP de la pila'''
        ...

    def top(self) -> int:
        '''Devolver el elemento que está en el TOP de la pila (sin extracción)'''
        ...

    def is_empty(self) -> bool:
        '''Indica si la pila está vacía'''
        ...

    def is_full(self) -> bool:
        '''Indica si la pila está llena -> max_size'''
        ...

    def expand(self, factor: int = 2) -> None:
        '''Expande el tamaño máximo de la pila en el factor indicado'''
        ...

    def dump_to_file(self, path: str) -> None:
        '''Vuelca la pila a un fichero. Cada item en una línea'''
        ...

    @classmethod
    def load_from_file(cls, path: str) -> IntegerStack:
        '''Crea una pila desde un fichero. Si la pila se llena al ir añadiendo elementos
        habrá que expandir con los valores por defecto'''
        ...

    def __getitem__(self, index: int) -> int:
        '''Devuelve el elemento de la pila en el índice indicado'''
        ...

    def __setitem__(self, index: int, item: int) -> None:
        '''Establece el valor de un elemento de la pila mediante el índice indicado'''
        ...

    def __len__(self):
        '''Número de elementos que contiene la pila'''
        ...

    def __str__(self):
        '''Cada elemento en una línea distinta empezando por el TOP de la pila'''
        ...

    def __add__(self, other: IntegerStack) -> IntegerStack:
        '''La segunda pila va "encima" de la primera'''
        ...

    def __iter__(self) -> IntegerStackIterator:
        ...


class IntegerStackIterator:
    def __init__(self, stack: IntegerStack):
        ...

    def __next__(self) -> int:
        ...
