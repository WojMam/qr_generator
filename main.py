import os

import qrcode
from qrcode.image.svg import SvgPathImage
from PIL import Image

from generator_utils import generate_qr_code_for_all_set


if __name__ == '__main__':
    generate_qr_code_for_all_set()
