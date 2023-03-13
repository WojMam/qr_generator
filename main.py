import os

import qrcode
from PIL import Image

# QR code properties:
box_size = 10
border = 4
fill_color = 'black'
back_color = 'white'
logo_link = 'logo.png'
error_correction = qrcode.constants.ERROR_CORRECT_H

# URLs and filenames:
results_directory= 'results'
luczniczqa_website = 'https://www.luczniczqa.pl'
luczniczqa_slack = 'https://join.slack.com/t/luczniczqa/shared_invite/zt-1r2pi3ckz-AmsPdWoFelLzPMscYRbf1A'
luczniczqa_facebook = 'https://www.facebook.com/LuczniczQA'
luczniczqa_linkedin = 'https://www.linkedin.com/company/luczniczqa/'


def create_results_directory(directory=results_directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def generate_qr_code_without_logo(data_to_encode, filename_prefix):
    create_results_directory()
    qr = qrcode.QRCode(version=None, error_correction=error_correction, box_size=box_size,
                       border=border)
    qr.add_data(data_to_encode)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f'./results/{filename_prefix}_prefix_qr_code_without_logo.png')


def generate_qr_code_with_logo(data_to_encode, filename_prefix, logo_to_encode):
    create_results_directory()
    logo = Image.open(logo_to_encode)
    basewidth = 100
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=error_correction
    )
    QRcode.add_data(data_to_encode)
    QRcode.make()
    qr_color = fill_color
    qr_image = QRcode.make_image(
        fill_color=qr_color, back_color=back_color).convert('RGB')
    pos = ((qr_image.size[0] - logo.size[0]) // 2,
           (qr_image.size[1] - logo.size[1]) // 2)
    qr_image.paste(logo, pos)
    qr_image.save(f'./results/{filename_prefix}_qr_code_with_logo.png')


def generate_qr_code_for_all_set():
    generate_qr_code_without_logo(luczniczqa_website, 'website')
    generate_qr_code_with_logo(luczniczqa_website, 'website', logo_link)
    generate_qr_code_without_logo(luczniczqa_slack, 'slack')
    generate_qr_code_with_logo(luczniczqa_slack, 'slack', logo_link)
    generate_qr_code_without_logo(luczniczqa_linkedin, 'linkedin')
    generate_qr_code_with_logo(luczniczqa_linkedin, 'linkedin', logo_link)
    generate_qr_code_without_logo(luczniczqa_facebook, 'facebook')
    generate_qr_code_with_logo(luczniczqa_facebook, 'facebook', logo_link)


if __name__ == '__main__':
    generate_qr_code_for_all_set()
