from common.consts import Messages

from src.file_handler import FileHandler


class Soccer:
    def __init__(self):
        self.file_name = "football"

    def get_the_smallest_goal_difference_team(self) -> dict:
        data = self.__get_data()
        if not data:
            raise ValueError(Messages.MSG_EMPTY_DATA)
        handled_data = []
        for record in data:
            handled_record = self.__handle_record(record)
            if handled_record:
                handled_data.append(handled_record)

        min_goal_difference_team = handled_data[0]
        for record in handled_data:
            if record["difference"] < min_goal_difference_team["difference"]:
                min_goal_difference_team = record
        return min_goal_difference_team

    def __get_data(self):
        raw_data = FileHandler().read_data_file(f"{self.file_name}.dat")
        FileHandler().write_data_to_csv(raw_data, f"{self.file_name}.csv")
        return FileHandler().read_csv_file(f"{self.file_name}.csv")

    def __handle_record(self, record):
        try:
            team = record["P"]
            goal_for = record["A"]
            last_key = list(record.keys())[-1]
            goal_against = record[last_key][0]
            goal_for = int(goal_for)
            goal_against = int(goal_against)
        except (TypeError, ValueError):
            return None

        goal_difference = goal_for - goal_against
        return {"team": team, "difference": goal_difference}
