import requests
from typing import Dict


def _make_response(method: str, url: str, headers: Dict, params: Dict, timeout: int, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def _get_endpoint(method: str, url: str, endpoint: str, headers: Dict, params: Dict, timeout: int, func=_make_response):
    url = f"{url}/{endpoint}"
    response = func(method, url, headers=headers, params=params, timeout=timeout)
    return response














