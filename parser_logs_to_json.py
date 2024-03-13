import re
import os
import json
from datetime import datetime


def parse_log_line(log_lines: str) -> list:
    """
    Parses log lines and returns a list of dictionaries containing the timestamp, level, and description.

    Args:
        log_lines (list): The list of log lines to be parsed.

    Returns:
        list: A list of dictionaries containing the parsed log information.
    """
    logs = []
    current_log = {}

    for log_line in log_lines:
        pattern = re.compile(
            r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<description>.+)$"
        )
        match = pattern.match(log_line)
        if match:
            timestamp_str = match.group("timestamp")
            level = match.group("level")
            description = match.group("description")

            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            current_log = {
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "level": level,
                "description": description,
            }
            logs.append(current_log)
        else:
            if current_log:
                current_log["description"] += " " + log_line.strip()

    return logs


def parse_log_file(log_file_path: str) -> list:
    """
    Parses a log file and returns a list of parsed log lines.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries representing the parsed log lines.
    """
    with open(log_file_path, "r", encoding="utf-8") as file:
        log_lines = file.readlines()

    parsed_logs = parse_log_line(log_lines)

    return parsed_logs


def save_json_file(data: list, json_file_path: str) -> None:
    """
    Save the given data as a JSON file.

    Args:
        data (list): The data to be saved as JSON. It should be a list of dictionaries.
        json_file_path (str): The path to the JSON file.

    Returns:
        None
    """

    json_string = "\n".join(json.dumps(entry) for entry in data)

    with open(json_file_path, "w", encoding="utf-8") as file:
        file.write(json_string)


def main():
    logs_paths = os.listdir("log")
    for log_path in logs_paths:
        print(f"Procesando archivos en la carpeta: {log_path}")
        for log_file in os.listdir(f"log/{log_path}"):
            if log_file.endswith(".json"):
                print(f"El archivo {log_file} ya ha sido parseado a JSON")
                continue

            log_file_path = f"log/{log_path}/{log_file}"
            parsed_logs = parse_log_file(log_file_path)
            json_file_path = f"log/{log_path}/{log_file.split('.')[0]}.json"
            save_json_file(parsed_logs, json_file_path)


if __name__ == "__main__":
    main()
