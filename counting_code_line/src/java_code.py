from src.file_handler import FileHandler
from src.java_formatter import JavaFormatter


class JavaCode:
    @staticmethod
    def get_valid_lines(file_name: str) -> list:
        lines = FileHandler().read_java_file(file_name)
        if not lines:
            return []

        lines = JavaFormatter().remove_single_line_comments(lines)
        lines = JavaFormatter.remove_block_comments(lines)
        lines = JavaFormatter.remove_blank_lines(lines)
        return lines
