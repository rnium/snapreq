from typing import Dict, Optional
import requests
from .utils import HttpMethod

def fetch(url: str, method: HttpMethod, headers: Optional[Dict]=None, data=None):
    res = requests.request(method.value, url, headers=headers, data=data)
    return res