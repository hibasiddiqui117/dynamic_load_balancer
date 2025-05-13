# utils.py

import random

def generate_request_load(min_load=5, max_load=25):
    return random.randint(min_load, max_load)
