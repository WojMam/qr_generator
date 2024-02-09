import os
from jproperties import Properties

def properties():
    configs = Properties()

    with open('resources/app-config.properties', 'rb') as config_file:
        configs.load(config_file)
    return configs

def create_results_directory(configs):
    if not os.path.exists(configs.get("results_directory").data):
        os.mkdir(configs.get("results_directory").data)