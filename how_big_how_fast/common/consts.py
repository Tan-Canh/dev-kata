class Messages:
    INTEGER_REQUIRED = "Required an unsigned integer"
    INTEGER_OTHER_THAN_ZERO_REQUIRED = "Required an unsigned integer other than 0"


class DataLengthRules:
    NAME = 50
    ADDRESS = 255
    PHONE = 10


class Coefficients:
    LATINH_CHAR_TO_BYTE = 1
    LATINH_CHAR_TO_BIT = 8
    SEARCH_VELOCITY = 0.34
    HASH_TIME_MS = 1
    HASH_CHARS_PER_POSITION = 96


class BookRules:
    CHAR_IN_LINE = 100
    LINE_IN_PAGE = 50
