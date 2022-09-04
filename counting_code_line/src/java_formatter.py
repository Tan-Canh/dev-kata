class JavaFormatter:
    @staticmethod
    def remove_single_line_comments(lines: list) -> list:
        for line in lines:
            if line[:2] == "//":
                lines.remove(line)
        return lines

    @staticmethod
    def remove_block_comments(lines: list) -> list:
        while True:
            is_multi_lines_comment = False
            line_changed_count = 0
            for index, line in enumerate(lines):
                if not is_multi_lines_comment:
                    if "/*" not in line:
                        continue
                    start_index = line.find("/*")
                    if "*/" not in line:
                        lines[index] = line[:start_index] or ""
                        line_changed_count += 1
                        is_multi_lines_comment = True
                        continue
                    end_index = line.find("*/") + 1
                    lines[index] = (line[:start_index] + line[end_index + 1 :]) or ""
                    line_changed_count += 1
                    continue
                if "*/" not in line:
                    lines[index] = ""
                    line_changed_count += 1
                    continue
                end_index = line.find("*/") + 1
                lines[index] = line[end_index + 1 :] or ""
                line_changed_count += 1
                is_multi_lines_comment = False
                continue

            if line_changed_count == 0:
                return lines

    @staticmethod
    def remove_blank_lines(lines: list) -> list:
        valid_lines = []
        for line in lines:
            checking_line = line.strip().replace(" ", "").replace("\t", "")
            if len(checking_line) > 0:
                valid_lines.append(line)
        return valid_lines
