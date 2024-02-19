""" This module contains the Parser class for """

from typing import Dict
import yaml

class Parser:
    """
    A class for parsing YAML files into dictionaries.
    
    Attributes:
        yaml_file_path (str): The file path to the YAML file.
    """

    def __init__(self, yaml_file_path: str) -> None:
        self.yaml_file_path = yaml_file_path


    def yaml_to_dict(self) -> Dict:
        """
        Converts a YAML file to a dictionary.

        Returns:
            A dictionary representation of the YAML file.

        Raises:
            yaml.YAMLError: If there is an error while loading the YAML file.
        """
        with open(self.yaml_file_path, 'r', encoding="UTF-8") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


class SLA4OIA(Parser):
    pass