""" This is a main pproject python module."""

from generator_utils import generate_qr_code_for_all_set
from results_utils import properties


if __name__ == '__main__':
    generate_qr_code_for_all_set(configs=properties())
