import asyncio
import datetime

from aioudp import UDPServer
import threading
import time
import json

class SubjectSample:
    def __init__(
            self, 
            x: float, 
            y: float, 
            width: float, 
            height: float, 
            sample_time: float
            ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sample_time = sample_time