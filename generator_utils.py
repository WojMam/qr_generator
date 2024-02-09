""" This is a python module that has functions to generate QR codes images in
    different formats.
"""

import qrcode
from qrcode.image.svg import SvgPathImage
from PIL import Image

from results_utils import create_results_directory


def generate_qr_code_without_logo(configs, data_to_encode, filename_prefix):
    """
    This method is generating QR code image in black and white format
    without any logo inside of it in .png format.

    Parameters:
    configs (): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    """

    create_results_directory(configs)
    qr = qrcode.QRCode(version=None,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=configs.get("box_size").data,
                       border=configs.get("border").data)
    qr.add_data(data_to_encode)
    img = qr.make_image(fill_color=configs.get("fill_color").data,
                        back_color=configs.get("back_color").data)
    img.save(f'./results/{filename_prefix}_qr_code_without_logo.png')


def generate_qr_code_without_logo_svg(configs, data_to_encode, filename_prefix):
    """
    This method is generating QR code image in black and white format
    without any logo inside of it in .svg format.

    Parameters:
    configs (): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    """

    create_results_directory(configs)
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=configs.get("box_size").data,
        border=configs.get("border").data
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    # Create an SVG image from the QR code
    img = qr.make_image(image_factory=SvgPathImage)
    img.save(f'./results/{filename_prefix}_qr_code_without_logo.svg')


def generate_qr_code_with_logo(configs, data_to_encode, filename_prefix, logo_to_encode):
    """
    This method is generating QR code image in black and white format
    with a logo inside of it in .png format.

    Parameters:
    configs (): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    """

    create_results_directory(configs)
    logo = Image.open(logo_to_encode)
    basewidth = 100
    wpercent =(basewidth / float(logo.size[0])
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    qrcode_object = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qrcode_object.add_data(data_to_encode)
    qrcode_object.make()
    qr_color = configs.get("fill_color").data
    qr_image = qrcode_object.make_image(
        fill_color=qr_color, back_color=configs.get("back_color").data).convert('RGB')
    pos = ((qr_image.size[0] - logo.size[0]) // 2,
           (qr_image.size[1] - logo.size[1]) // 2)
    qr_image.paste(logo, pos)
    qr_image.save(f'./results/{filename_prefix}_qr_code_with_logo.png')


def generate_qr_code_for_all_set(configs):
    """
    This method  generating whole set of  QR code images at once.

    Parameters:
    configs (): Object with all the parameters set in the project configuration file
    data_to_encode (string): Data to be decoded inside QR code, for example webpage link
    filename_prefix (string): Prefix to the filename that will be saved as result
    """

    generate_qr_code_without_logo(configs, configs.get("luczniczqa_website"),
                                  'website')
    generate_qr_code_with_logo(configs, configs.get("luczniczqa_website"),
                               'website',
                               configs.get("logo_link"))
    generate_qr_code_without_logo(configs, configs.get("luczniczqa_slack"),
                                  'slack')
    generate_qr_code_with_logo(configs, configs.get("luczniczqa_slack"),
                               'slack',
                               configs.get("logo_link"))
    generate_qr_code_without_logo(configs, configs.get("luczniczqa_linkedin"),
                                  'linkedin')
    generate_qr_code_with_logo(configs, configs.get("luczniczqa_linkedin"),
                               'linkedin',
                               configs.get("logo_link"))
    generate_qr_code_without_logo(configs, configs.get("luczniczqa_facebook"),
                                  'facebook')
    generate_qr_code_with_logo(configs, configs.get("luczniczqa_facebook"),
                               'facebook',
                               configs.get("logo_link"))
    generate_qr_code_without_logo_svg(configs, configs.get("luczniczqa_website").data,
                                      'website')
