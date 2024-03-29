""" This is a python module that has functions to generate QR codes images in
    different formats.
"""

import qrcode
import cv2
from qrcode.image.svg import SvgPathImage
from PIL import Image

from utils.results_utils import create_results_directory


def generate_qr_code_without_logo(configs, data_to_encode, filename_prefix):
    """
    This method is generating QR code image in black and white format
    without any logo inside of it in .png format.

    Parameters:
    configs (Properties): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    """

    create_results_directory(configs)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=configs.get("box_size").data,
        border=configs.get("border").data,
    )
    qr.add_data(data_to_encode)
    img = qr.make_image(
        fill_color=configs.get("fill_color").data,
        back_color=configs.get("back_color").data,
    )
    img.save(f"./results/{filename_prefix}_qr_code_without_logo.png")


def generate_qr_code_without_logo_svg(configs, data_to_encode, filename_prefix):
    """
    This method is generating QR code image in black and white format
    without any logo inside of it in .svg format.

    Parameters:
    configs (Properties): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    """

    create_results_directory(configs)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=configs.get("box_size").data,
        border=configs.get("border").data,
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    # Create an SVG image from the QR code
    img = qr.make_image(image_factory=SvgPathImage)
    img.save(f"./results/{filename_prefix}_qr_code_without_logo.svg")


def generate_qr_code_with_logo(
    configs, data_to_encode, filename_prefix, logo_to_encode
):
    """
    This method is generating QR code image in black and white format
    with a logo inside of it in .png format.

    Parameters:
    configs (Properties): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    logo_to_encode (string): Path to a logo to encode
    """

    create_results_directory(configs)
    logo = Image.open(logo_to_encode)
    basewidth = 100
    wpercent = basewidth / float(logo.size[0])
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    qrcode_object = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qrcode_object.add_data(data_to_encode)
    qrcode_object.make()
    qr_color = configs.get("fill_color").data
    qr_image = qrcode_object.make_image(
        fill_color=qr_color, back_color=configs.get("back_color").data
    ).convert("RGB")
    pos = (
        (qr_image.size[0] - logo.size[0]) // 2,
        (qr_image.size[1] - logo.size[1]) // 2,
    )
    qr_image.paste(logo, pos)
    qr_image.save(f"./results/{filename_prefix}_qr_code_with_logo.png")


def decode_qr_code(data_to_decode):
    """
    This method is decoding QR code image into text.

    Parameters:
    data_to_decode (string): Data to be encoded (QR code image)

    Returns:
    str:File directory
    """

    detector = cv2.QRCodeDetector()  # pylint: disable=no-member
    text, b, c = detector.detectAndDecode(  # pylint: disable=unused-variable
        cv2.imread(data_to_decode)  # pylint: disable=no-member
    )
    return text
