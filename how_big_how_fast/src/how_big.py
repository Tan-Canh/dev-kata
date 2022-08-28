from common.consts import Coefficients, DataLengthRules, Messages


class HowBig:
    @staticmethod
    def count_bit(number: int) -> int:
        if number < 0:
            raise ValueError(Messages.INTEGER_REQUIRED)
        if number in (0, 1):
            return 1

        count = 0
        while number != 0:
            number = number // 2
            count += 1
        return count

    def compute_storage_space(self, record_count: int) -> int:
        if record_count < 0:
            raise ValueError(Messages.INTEGER_REQUIRED)
        if record_count == 0:
            return 0

        record_size = (
            DataLengthRules.NAME + DataLengthRules.ADDRESS + DataLengthRules.PHONE
        ) * Coefficients.LATINH_CHAR_TO_BYTE
        return record_size * record_count

    @staticmethod
    def get_binary_level_by_number_of_node(node_count: int = 0) -> int:
        if node_count < 0:
            raise ValueError(Messages.INTEGER_REQUIRED)
        if node_count == 0:
            return 0

        level = 0
        while True:
            if 2**level >= node_count:
                return level + 1
            level += 1
