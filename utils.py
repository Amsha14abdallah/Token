import random
import string
import time

def generate_token(meter_number: str, units: int)-> str:
    base = meter_number[-4:] + str(units).zfill(4)
    rand_part = ''.join(random.choices(string.digits, k=8))
    timestamp = str(int(time.time()))[-4:]
    token = base + rand_part + timestamp
    return ' '.join([token[i:i+5] for i in range(0, len(token), 5)])
    '''Generate a 20-digit token for electricity purchase.
    Token is a mix of meter, time, and random data.'''
