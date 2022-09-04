from common.consts import BookRules, Coefficients, Messages

from src.how_big import HowBig


class HowFast:
    @staticmethod
    def compute_tranmission_time(
        number_of_pages: int, baud_rate: int, modem_coeficient: int = 1
    ) -> int:
        if number_of_pages <= 0 or baud_rate <= 0 or modem_coeficient <= 0:
            raise ValueError(Messages.INTEGER_OTHER_THAN_ZERO_REQUIRED)

        book_size = (
            (BookRules.CHAR_IN_LINE * BookRules.LINE_IN_PAGE)
            * number_of_pages
            * Coefficients.LATINH_CHAR_TO_BIT
        )
        modem_velocity = baud_rate * modem_coeficient

        return book_size // modem_velocity

    @staticmethod
    def compute_binary_search_tree_time(number_of_records: int) -> float:
        if number_of_records <= 0:
            raise ValueError(Messages.INTEGER_OTHER_THAN_ZERO_REQUIRED)

        binary_tree_level = HowBig().get_binary_level_by_number_of_node(
            number_of_records
        )
        return Coefficients.SEARCH_VELOCITY * (binary_tree_level - 1)

    @staticmethod
    def compute_brute_force_time(hash_length: int) -> int:
        if hash_length <= 0:
            raise ValueError(Messages.INTEGER_OTHER_THAN_ZERO_REQUIRED)

        return (
            hash_length**Coefficients.HASH_CHARS_PER_POSITION
        ) * Coefficients.HASH_TIME_MS
