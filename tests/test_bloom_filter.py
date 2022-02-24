import pytest
from src.bloom_filter import BloomFilter


class TestBloomFilter:

    def test_empty_bloom_filter(self):
        n = 1000
        bloom_filter = BloomFilter(n)

        for int_key in range(n):
            key = str(int_key)
            assert key not in bloom_filter

    def test_added_bloom_filter(self):
        n = 1000
        bloom_filter = BloomFilter(n)

        for int_key in range(n):
            key = str(int_key)
            bloom_filter.add(key)

        for int_key in range(n):
            key = str(int_key)
            assert key in bloom_filter
