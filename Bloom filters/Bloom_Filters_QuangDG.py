import math
import mmh3
from bitarray import bitarray
import hashlib


class BloomFilter:

    def __init__(self, quantity: int, false_possible_prob: float):
        self.false_possible_prob = false_possible_prob
        self.size = self.get_size(quantity, false_possible_prob)
        self.hash_count = int(self.size / quantity * math.log(2))
        self.bit_array = bitarray(self.size)

        self.bit_array.setall(0)

    def initialize_data(self, item_list):
        for item in item_list:
            self.add(item)

    def add(self, item):
        for idx in range(self.hash_count):
            hash_1 = hashlib.md5((item + str(idx)).encode())
            digest = mmh3.hash(hash_1.hexdigest(), idx) % self.size
            self.bit_array[digest] = True

    def check(self, item):
        item = item.lower()

        for idx in range(self.hash_count):
            hash_1 = hashlib.md5((item + str(idx)).encode())
            digest = mmh3.hash(hash_1.hexdigest(), idx) % self.size
            if not self.bit_array[digest]:
                return False

        return True

    @classmethod
    def get_size(cls, quantity: int, false_possible_prob: float):
        temp = -(quantity * math.log(false_possible_prob))/(math.log(2)**2)
        return int(temp)


if __name__ == '__main__':
    word_file = open("wordlist.txt", "r")
    word_data = word_file.read().lower().split('\n')
    word_data.remove('')

    bloom_filter = BloomFilter(len(word_data), 0.05)
    bloom_filter.initialize_data(word_data)

    while True:
        input_text = input("Enter your word to check: ")
        if input_text == "qwer":
            break
        print("this word is {} in dict".format("definitely not" if not bloom_filter.check(input_text) else "probably"))
