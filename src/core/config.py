import json
import os
from core.utils import get_base_dir

class Config:
    def __init__(self, filename="config.json"):
        self.path = os.path.join(get_base_dir(), filename)
        self.data = {}

    def load(self):
        if not os.path.exists(self.path):
            raise FileNotFoundError("[core] config.json not found")
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)
