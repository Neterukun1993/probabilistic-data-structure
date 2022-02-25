import pytest
from src.counting_bloom_filter import CountingBloomFilter


class TestCountingBloomFilter:

    def test_empty_counting_bloom_filter(self):
        key_count = 1000
        counting_bloom_filter = CountingBloomFilter(key_count, key_count * 100)

        for int_key in range(key_count):
            key = str(int_key)
            assert key not in counting_bloom_filter

    def test_add_key_to_counting_bloom_filter(self):
        key_count = 1000
        counting_bloom_filter = CountingBloomFilter(key_count, key_count * 100)

        for int_key in range(key_count):
            key = str(int_key)
            counting_bloom_filter.add(key)

        for int_key in range(key_count):
            key = str(int_key)
            assert key in counting_bloom_filter

    def test_remove_key_from_counting_bloom_filter(self):
        key_count = 1000
        counting_bloom_filter = CountingBloomFilter(key_count, key_count * 100)

        for int_key in range(key_count):
            key = str(int_key)
            counting_bloom_filter.add(key)

        for int_key in range(key_count):
            key = str(int_key)
            counting_bloom_filter.remove(key)
            assert key not in counting_bloom_filter

    def test_add_duplicate_key_to_counting_bloom_filter(self):
        key_count = 1000
        counting_bloom_filter = CountingBloomFilter(key_count, key_count * 100)

        for int_key in range(key_count):
            key = str(int_key)
            counting_bloom_filter.add(key)
            counting_bloom_filter.add(key)  # add key twice

        for int_key in range(key_count):
            key = str(int_key)
            counting_bloom_filter.remove(key)
            assert key in counting_bloom_filter

            counting_bloom_filter.remove(key)
            assert key not in counting_bloom_filter

    def test_remove_key_from_empty_counting_bloom_filter(self):
        key_count = 1000
        counting_bloom_filter = CountingBloomFilter(key_count, key_count * 100)

        for int_key in range(key_count):
            key = str(int_key)
            assert not counting_bloom_filter.remove(key)
