from math import log
from hashlib import md5
from typing import Iterator
from src.utils.bit_vector import BitVector  # type: ignore


class BloomFilter:
    m: int
    k: int
    array: BitVector

    def __init__(self, capacity: int, false_positive: float = 0.01) -> None:
        self.m = int(-capacity * log(false_positive) / log(2) ** 2)
        self.k = int((self.m / capacity) * log(2))
        self.array = BitVector(self.m)

    def __contains__(self, key: str) -> bool:
        return all(self.array.access(i) for i in self._hash(key))

    def _hash(self, key: str) -> Iterator[int]:
        h = md5()
        b = key.encode("utf-8")
        for _ in range(self.k):
            h.update(b)
            x = int.from_bytes(h.digest(), "big")
            yield x % self.m

    def add(self, key: str) -> None:
        for i in self._hash(key):
            self.array.set(i)
