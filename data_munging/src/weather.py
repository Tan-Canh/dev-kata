from common.consts import Messages

from src.file_handler import FileHandler


class Weather:
    def __init__(self):
        self.file_name = "weather"

    def get_the_smallest_temperature_spread_day(self) -> dict:
        data = self.__get_data()
        if not data:
            raise ValueError(Messages.MSG_EMPTY_DATA)
        handled_data = []
        for record in data:
            handled_record = self.__handle_record(record)
            if handled_record:
                handled_data.append(handled_record)

        min_spread_day = handled_data[0]
        for record in handled_data:
            if record["spread"] < min_spread_day["spread"]:
                min_spread_day = record
        return min_spread_day

    def __get_data(self):
        raw_data = FileHandler().read_data_file(f"{self.file_name}.dat")
        FileHandler().write_data_to_csv(raw_data, f"{self.file_name}.csv")
        return FileHandler().read_csv_file(f"{self.file_name}.csv")

    def __handle_record(self, record):
        day = record["Dy"]
        max_temperature = record["MxT"]
        min_temperature = record["MnT"]
        try:
            day = int(day)
            max_temperature = int(max_temperature.replace("*", ""))
            min_temperature = int(min_temperature.replace("*", ""))
        except ValueError:
            return None

        temperature_spread = max_temperature - min_temperature
        return {"day": day, "spread": temperature_spread}
