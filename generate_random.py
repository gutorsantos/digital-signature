import random

from miller_rabin import miller_rabin

def generate_random_int(size=100):
    return random.getrandbits(size)

def generate_prime_random(size=1024):
    while(True):
        r = generate_random_int(size)
        if(miller_rabin(r)):
            return r
