# qr_generator

QR generator is a small side project to quickly generate QR codes with basic link to
our meetup resources.

## Pre-requisities

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all
required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

Before running the code, please check below file to adjust your properties/links:

```bash
/resources/app-config.properties
```

User can use application GUI to generate the QR codes. To run the GUI below command must be executed from the project root directory:

```bash
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to check pylint results in the Actions tab after commiting.

Last commit Pylink status:

[![Pylint](https://github.com/WojMam/qr_generator/actions/workflows/pylint.yml/badge.svg)](https://github.com/WojMam/qr_generator/actions/workflows/pylint.yml)

## Plan for the future:

- [x] Full initial refactor
- [x] Links in the seperate file, not hardcoded in the code
- [x] Possibility to put you own link in the command line to generate 1 QR code - removed :heavy_multiplication_x:
- [x] Possibility to generate QR codes for all the links from the configuration file via command line - removed :heavy_multiplication_x:
- [x] GUI
  - [x] Possibility to put you own link in the entry field
  - [x] Possibility to generate single QR code from the entry field
  - [x] Possibility to generate QR codes for all the links from the configuration file - removed :heavy_multiplication_x:
  - [x] Possibility to open OS explorer window in the "Results" directory
  - [x] GUI refactor to more modern one
  - [x] Possibility to decode the data from QR code image

## License

[MIT](https://choosealicense.com/licenses/mit/)
