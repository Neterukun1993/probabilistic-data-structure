from typing import List


class BitVector:
    size: int
    block_num: int
    bit: List[int]

    def __init__(self, size: int) -> None:
        # self.BLOCK_WIDTH = 32
        self.size = size
        self.block_num = (size + 31) >> 5
        self.bit = [0] * self.block_num

    def set(self, i: int) -> None:
        if not 0 <= i < self.size:
            raise IndexError
        self.bit[i >> 5] |= 1 << (i & 31)

    def access(self, i: int) -> int:
        if not 0 <= i < self.size:
            raise IndexError
        return (self.bit[i >> 5] >> (i & 31)) & 1
