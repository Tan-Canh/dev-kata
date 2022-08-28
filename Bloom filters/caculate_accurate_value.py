from Bloom_Filters_QuangDG import BloomFilter
import random
import string


def random_word(length: int):
    output2 = ""
    for idx3 in range(length):
        char_output = random.choice(string.ascii_letters)
        output2 += char_output

    return output2


if __name__ == "__main__":
    word_file = open("wordlist.txt", "r")
    word_data = word_file.read().lower().split("\n")
    word_data.remove("")

    bloom_filter = BloomFilter(len(word_data), 0.05)
    bloom_filter.initialize_data(word_data)

    data_char = string.ascii_letters

    test_total = random.randint(100, 1000)
    true_possibility = 0
    false_possibility = 0
    true_negative = 0
    false_negative = 0

    for idx in range(test_total):
        test_item = random_word(5)
        output = bloom_filter.check(test_item)

        if output and test_item in word_data:
            true_possibility += 1
        elif output and test_item not in word_data:
            false_possibility += 1
        elif not output and test_item in word_data:
            false_negative += 1
        elif not output and test_item not in word_data:
            true_negative += 1

    print("Total: {} tests".format(test_total))
    print(
        "True positive: {} tests or {} %".format(
            true_possibility, true_possibility / test_total * 100
        )
    )
    print(
        "false negative: {} tests or {} %".format(
            false_negative, false_negative / test_total * 100
        )
    )
    print(
        "False positive: {} tests or {} %".format(
            false_possibility, false_possibility / test_total * 100
        )
    )

    print(
        "true negative: {} tests or {} %".format(
            true_negative, true_negative / test_total * 100
        )
    )
