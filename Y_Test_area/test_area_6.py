import ast
import os, re
from pathlib import Path
from datetime import date
import datetime
from sqlalchemy import func

# print("1 example:", Path(__file__).resolve().parent / "test_area_5.py")
# print("2 example:",date(2024, 3, 4))
# print("3 example:",datetime.datetime.now().strftime("%Y-%m-%d"))
# print("4 example:",datetime.date.today())


def validate_phone(phone: str) -> None:
    # pattern = "[7/(9][0-9]{2}[/)]/.[0-9]{3}/.[0-9]{2}/.[0-9]{2}"
    pattern = "[/+][7][/(]\d{3}[/)][/-]\d{3}[/-]\d{2}[/-]\d{2}"
    res = re.match(pattern, phone)
    print(res)
    if not res:
        raise 'Phone number must be entered in the format: + 7(9**)-***-**-**, where * - digit from 0 to 9'

# validate_phone(input("Enter your phone number: "))
# +7(905)-122-33-11
i = input("enter num: ")
print(ast.literal_eval(i))
