import pytest
from src.utils.bit_vector import BitVector


class TestBitVector:

    def test_initialize(self):
        n = 100
        bit_vector = BitVector(n)
        for i in range(n):
            assert bit_vector.access(i) == 0

    def test_set_and_access(self):
        n = 100
        bit_vector = BitVector(n)

        indexes = (0, 15, 31, 32, 63, 96)
        for i in indexes:
            bit_vector.set(i)

        for i in range(n):
            if i in indexes:
                assert bit_vector.access(i) == 1
            else:
                assert bit_vector.access(i) == 0

    def test_access_failed_if_index_is_out_of_range(self):
        n = 100
        bit_vector = BitVector(n)

        with pytest.raises(IndexError):
            bit_vector.access(-1)
        with pytest.raises(IndexError):
            bit_vector.access(n)

    def test_set_failed_if_index_is_out_of_range(self):
        n = 100
        bit_vector = BitVector(n)

        with pytest.raises(IndexError):
            bit_vector.set(-1)
        with pytest.raises(IndexError):
            bit_vector.set(n)
