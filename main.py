import qrcode
from PIL import Image


def generate_qr_code():
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data("https://www.luczniczqa.pl")
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code_without_logo.png")


def generate_qr_code_matrix():
    logo = Image.open("logo.png")
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data("https://www.luczniczqa.pl")
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    logo_size = int(min(img.size) * 0.1)  # Rozmiar logo jako 1/4 rozmiaru kodu QR
    logo = logo.resize((logo_size, logo_size))
    logo_pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
    img.paste(logo, logo_pos)
    img.save("false_qr_code_with_logo.png")


def generate_geeks_forge():
    logo_link = 'logo.png'
    logo = Image.open(logo_link)
    basewidth = 100
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    url = 'https://www.luczniczqa.pl'
    QRcode.add_data(url)
    QRcode.make()
    qr_color = 'Black'
    qr_image = QRcode.make_image(
        fill_color=qr_color, back_color="white").convert('RGB')
    pos = ((qr_image.size[0] - logo.size[0]) // 2,
           (qr_image.size[1] - logo.size[1]) // 2)
    qr_image.paste(logo, pos)
    qr_image.save('qr_code_with_logo.png')


if __name__ == '__main__':
    generate_qr_code()
    generate_geeks_forge()
