import csv
import os

from common.consts import Messages, Paths


class FileHandler:
    def read_data_file(self, file_name):
        if file_name.split(".")[-1] != "dat":
            raise ValueError(Messages.MSG_NOT_SUPPORTED)

        file_path = os.path.relpath(f"{Paths.DEFAULT_DATA_FOLDER}/{file_name}")

        try:
            data = [line.strip().split() for line in open(file_path, "r").readlines()]
            return list(filter(lambda x: x, data))
        except FileNotFoundError as exc:
            exc.strerror = Messages.MSG_FILE_NOT_FOUND
            raise exc

    def write_data_to_csv(self, data, file_name):
        if file_name.split(".")[-1] != "csv":
            raise ValueError(Messages.MSG_NOT_SUPPORTED)

        file_path = os.path.relpath(f"{Paths.DEFAULT_DATA_FOLDER}/{file_name}")

        current_directory = os.getcwd()
        if not os.path.exists(f"{current_directory}/{Paths.DEFAULT_DATA_FOLDER}"):
            os.mkdir(f"{current_directory}/{Paths.DEFAULT_DATA_FOLDER}")

        try:
            with open(file_path, "w+") as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except FileNotFoundError as exc:
            exc.strerror = Messages.MSG_FILE_NOT_FOUND
            raise exc

    def read_csv_file(self, file_name):
        if file_name.split(".")[-1] != "csv":
            raise ValueError(Messages.MSG_NOT_SUPPORTED)

        file_path = os.path.relpath(f"{Paths.DEFAULT_DATA_FOLDER}/{file_name}")

        try:
            with open(file_path, "r") as file:
                csv_reader = csv.DictReader(file)
                return list(csv_reader)
        except FileNotFoundError as exc:
            exc.strerror = Messages.MSG_FILE_NOT_FOUND
            raise exc
