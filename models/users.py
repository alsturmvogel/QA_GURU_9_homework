from dataclasses import dataclass
from pathlib import Path


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    gender_number: int  # ← добавили
    phone: str
    birth_day: str
    birth_month: str
    birth_month_value: str
    birth_year: str
    subject: str
    hobby: str
    hobby_number: int
    picture: Path
    address: str
    state: str
    city: str


student = User(
    first_name='Иван',
    last_name='Петров',
    email='ivanov@example.com',
    gender='Male',
    gender_number=1,  # ← теперь совпадает с полем датакласса
    phone='1234567890',
    birth_day='10',
    birth_month='February',
    birth_month_value='1',
    birth_year='1995',
    subject='Maths',
    hobby='Sports',
    hobby_number=1,
    picture=Path(__file__).parent.parent / 'resources' / 'images.jpeg',
    address='Москва, ул.Гоголя 10',
    state='NCR',
    city='Delhi',
)
