import os

from common.consts import Messages, Paths


class FileHandler:
    def read_java_file(self, file_name):
        if file_name.split(".")[-1] != "java":
            raise ValueError(Messages.MSG_NOT_SUPPORTED)

        file_path = os.path.relpath(f"{Paths.DEFAULT_DATA_FOLDER}/{file_name}")

        try:
            return [line.replace("\n", "") for line in open(file_path, "r").readlines()]
        except FileNotFoundError as exc:
            exc.strerror = Messages.MSG_FILE_NOT_FOUND
            raise exc
