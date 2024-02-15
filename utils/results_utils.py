""" This is a python module that has project utilities functions."""

import os
from jproperties import Properties


def properties():
    """
    This method is loading the project properties file

    Returns:
    int:Returning value
    """

    configs = Properties()

    with open('resources/app-config.properties', 'rb') as config_file:
        configs.load(config_file)
    return configs

def create_results_directory(configs):
    """
    This method is checking if the directory for the produced results is available
    in the project and if not- it is creating it in the root of the project.

    Parameters:
    configs (): Object with all the parameters set in the project configuration file
    """

    if not os.path.exists(configs.get("results_directory").data):
        os.mkdir(configs.get("results_directory").data)
