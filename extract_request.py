"""
This module provides functions for filtering logs and extracting requests.
"""

import os


def filter_logs(file: str) -> None:
    """
    Filters the logs in the given file and writes the filtered logs to a new file.

    Args:
        file (str): The path to the input file.

    Returns:
        None
    """
    file_write = file.replace(".json", "_filtered.json")
    with open(file, "r", encoding="utf-8") as f:
        with open(file_write, "w", encoding="utf-8") as f_out:
            for line in f:
                if "GET" in line or "HTTP/1.1" in line:
                    f_out.write(line)


def main():
    """
    Process the files in the 'log' directory and filter the ones
    with a '.json' extension to extract the requests.
    """
    directory_logs = os.listdir("log")
    for folder in directory_logs:
        print(f"Procesando archivos en la carpeta: {folder}")
        folder_api = os.path.join("log/", folder)
        for file in os.listdir(folder_api):
            if file.endswith(".json"):
                filter_logs(os.path.join("log/", folder, file))


if __name__ == "__main__":
    main()
