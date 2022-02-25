from math import log
from hashlib import md5
from typing import List, Iterator


class CountingBloomFilter:
    m: int
    k: int
    array: List[int]

    def __init__(self, key_count: int, array_size: int) -> None:
        self.array_size = array_size
        self.k = int((array_size / key_count) * log(2))
        self.array = [0] * array_size

    def __contains__(self, key: str) -> bool:
        return all(self.array[i] for i in self._hash(key))

    def _hash(self, key: str) -> Iterator[int]:
        h = md5()
        b = key.encode("utf-8")
        for _ in range(self.k):
            h.update(b)
            x = int.from_bytes(h.digest(), "big")
            yield x % self.array_size

    def add(self, key: str) -> None:
        for i in self._hash(key):
            self.array[i] += 1

    def remove(self, key: str) -> bool:
        if key not in self:
            return False
        for i in self._hash(key):
            self.array[i] -= 1
        return True
