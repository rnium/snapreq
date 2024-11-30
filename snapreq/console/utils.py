from enum import Enum
from dataclasses import dataclass

@dataclass
class SuccesProps:
    border_style: str = "cyan"

@dataclass
class ErrorProps:
    border_style: str = "red"

@dataclass
class WarningProps:
    border_style: str = "yellow"

@dataclass
class ResponseType:
    SUCCESS = SuccesProps
    ERROR = ErrorProps
    WARNING = WarningProps

def status_detail(code: int):
    STATUS_DETAILS = {
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        204: 'No Content',
        400: 'Bad Request',
        401: 'Unauthorized',
        403: 'Forbidden',
        404: 'Not Found',
        500: 'Internal Server Error',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout'
    }
    return STATUS_DETAILS.get(code, 'Unknown Status Code')