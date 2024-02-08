import os
from jproperties import Properties

def properties():
    configs = Properties()

    with open('app-config.properties', 'rb') as config_file:
        configs.load(config_file)

def create_results_directory(directory=results_directory):
    if not os.path.exists(directory):
        os.mkdir(directory)