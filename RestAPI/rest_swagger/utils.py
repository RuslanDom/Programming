from models import Owner
from typing import Optional




def division_name(name: str) -> Optional[Owner]:
    data_name = name.split()
    if len(data_name) > 1:
        return Owner(first_name=data_name[0], last_name=data_name[1])
    elif len(data_name) == 1:
        return Owner(first_name=data_name[0], last_name=None)
    else:
        return None








