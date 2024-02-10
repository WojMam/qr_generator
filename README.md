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

Afterwards, to generate all the possible QR codes varations below code be used (included in the main.py):

```python
from generator_utils import generate_qr_code_for_all_set
from results_utils import properties


if __name__ == '__main__':
    generate_qr_code_for_all_set(configs=properties())
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to check pylint results in the Actions tab after commiting.

## Plan for the future:

- [x] Full refactor
- [X] Links in the seperate file, not hardcoded in the code
- [ ] Possibility to put you own link in the command line
- [ ] GUI

## License

[MIT](https://choosealicense.com/licenses/mit/)
