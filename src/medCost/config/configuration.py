import os
from src.medCost.utils.common import read_yaml,create_directories
from src.medCost.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            param_filepath = PARAMS_FILE_PATH ):
        
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(param_filepath)

        create_directories([self.config.artifacts_root])
        