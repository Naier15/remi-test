from django.utils.timezone import localtime
import aiofiles
from dateutil.parser import parse


class Currency:
    __file_path = r'./static/data/currencies.txt'

    @classmethod
    def load(cls, USD_RUB: float, EUR_RUB: float) -> None:
        try:
            with open(cls.__file_path, 'w+') as file:
                file.write(f'{round(USD_RUB, 2)},{round(EUR_RUB, 2)},{localtime()}')
        except Exception as e:
            raise Exception(f'[ERROR] Currency - function load went wrong. {e}')

    @classmethod
    def dump(cls) -> tuple[str, str, int, int]:
        try:
            with open(cls.__file_path, 'rt') as file:
                line = file.readline()
                dollar, euro, updated_time = line.split(',')
                updated_time = localtime() - parse(updated_time)
                minutes, seconds = updated_time.seconds//60%60, updated_time.seconds%60
                return (dollar, euro, minutes, seconds)
        except Exception as e:
            raise Exception(f'[ERROR] Currency - function dump went wrong. {e}')

