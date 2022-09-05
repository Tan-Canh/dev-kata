from unittest import TestCase
from bloom_filters_quang_dg import BloomFilter
from bitarray import bitarray
import hashlib
import mmh3


class BloomFiltersTest(TestCase):
    def test_create_bloom_filters(self):
        bloom_filter = BloomFilter(1000, 0.05)
        bit_array = bitarray(6235)
        bit_array.setall(0)

        self.assertEqual(0.05, bloom_filter.false_possible_prob)
        self.assertEqual(6235, bloom_filter.size)
        self.assertEqual(4, bloom_filter.hash_count)
        self.assertEqual(bit_array, bloom_filter.bit_array)

    def test_add_item_in_the_bit_array(self):
        bloom_filter = BloomFilter(1000, 0.05)
        text = "30k long xao dua"
        bit_array = bitarray(6235)
        bit_array.setall(0)
        hash_count = 4

        for idx in range(hash_count):
            hash_1 = hashlib.md5((text + str(idx)).encode())
            digest = mmh3.hash(hash_1.hexdigest(), idx) % 6235
            bit_array[digest] = True

        bloom_filter.add(text)

        self.assertEqual(0.05, bloom_filter.false_possible_prob)
        self.assertEqual(6235, bloom_filter.size)
        self.assertEqual(4, bloom_filter.hash_count)
        self.assertEqual(bit_array, bloom_filter.bit_array)

    def test_check_item_in_the_bit_array_or_not(self):
        bloom_filter = BloomFilter(1000, 0.05)
        text_1 = "30k long xao dua"
        text_2 = "shark like bup be"

        bloom_filter.add(text_1)
        bloom_filter.add(text_2)

        self.assertEqual(True, bloom_filter.check(text_1))
        self.assertEqual(True, bloom_filter.check(text_2))

    def test_initialize_data_into_bit_array(self):
        bloom_filter = BloomFilter(1000, 0.05)
        bit_array = bitarray(6235)
        bit_array.setall(0)
        hash_count = 4

        word_list = [
            "abound",
            "abounds",
            "abundance",
            "abundant",
            "accessible",
            "bloom",
            "blossom",
            "bolster",
            "bonny",
            "bonus",
            "bonuses",
            "coherent",
            "cohesive",
            "colorful",
            "comely",
            "comfort",
            "gems",
            "generosity",
            "generous",
            "generously",
            "genial",
        ]

        for word in word_list:
            for idx in range(hash_count):
                hash_1 = hashlib.md5((word + str(idx)).encode())
                digest = mmh3.hash(hash_1.hexdigest(), idx) % 6235
                bit_array[digest] = True

        bloom_filter.initialize_data(word_list)

        self.assertEqual(0.05, bloom_filter.false_possible_prob)
        self.assertEqual(6235, bloom_filter.size)
        self.assertEqual(4, bloom_filter.hash_count)
        self.assertEqual(bit_array, bloom_filter.bit_array)
