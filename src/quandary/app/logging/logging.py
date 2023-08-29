"""

Logging standardisation within quandary
"""

from enum import Enum
from datetime import datetime

class QuandaryLogType(Enum):
    WARN  = '[WARNING]'
    ERR   = '[ERROR]  '
    DEBUG = '[DEBUG]  '

class QuandaryLog():
    """A log entry within quandary"""


    def __init__(self, logtype: QuandaryLogType, value: any):
        current_datetime = datetime.now()
        self.type = logtype
        self.value = str(value)
        self.timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"{self.timestamp} {self.type} {self.value}"