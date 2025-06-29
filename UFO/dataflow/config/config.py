# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from ufo.config.config import Config as BaseConfig
from .secure_config import load_secure_config


class Config(BaseConfig):
    _instance = None

    def __init__(self, config_path="dataflow/config/"):
        """
        Initializes the Config class with secure API key management.
        :param config_path: The path to the config file.
        """
        # Use secure config loader that prioritizes environment variables
        self.config_data = load_secure_config(config_path)
        
        # Apply optimizations
        self.config_data = self.optimize_configs(self.config_data)

    @staticmethod
    def get_instance():
        """
        Get the instance of the Config class.
        :return: The instance of the Config class.
        """

        if Config._instance is None:
            Config._instance = Config()

        return Config._instance

    def optimize_configs(self, configs):
        """
        Optimize the configurations.
        :param configs: The configurations to optimize.
        :return: The optimized configurations.
        """
        
        self.update_api_base(configs, "PREFILL_AGENT")
        self.update_api_base(configs, "FILTER_AGENT")

        return configs
