import os
from pathlib import Path
from datetime import date
import datetime
from sqlalchemy import func
print("1 example:", Path(__file__).resolve().parent / "test_area_5.py")
print("2 example:",date(2024, 3, 4))
print("3 example:",datetime.datetime.now().strftime("%Y-%m-%d"))
print("4 example:",datetime.date.today())