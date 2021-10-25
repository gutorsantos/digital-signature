from ctypes import sizeof
from generate_random import generate_prime_random, generate_random_int
from math import gcd, lcm

class __RSA__:
    p: int
    q: int
    n: int
    totient: int
    e: int
    d: int

    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.totient = 0
        self.e = 0
        self.d = 0

    def generate_keys(self):
        self.p = generate_prime_random()
        self.q = generate_prime_random()

        while(self.p == self.q):
            self.q = generate_prime_random()

        if(self.p < self.q):
            self.p, self.q = self.q, self.p

        self.n = self.p * self.q
        self.totient = lcm(self.p-1, self.q-1)
        # self.generate_public_key()
        self.e = 65537
        self.generate_private_key()

    def generate_public_key(self):
        self.e = 2
        tmp = 0
        while(self.e < self.totient):
            tmp = gcd(self.e, self.totient)
            if(tmp == 1):
                break
            self.e = self.e + 1

    def mod_inverse(self):
        if gcd(self.e, self.totient) != 1:
            return None
        u1, u2, u3 = 1, 0, self.e
        v1, v2, v3 = 0, 1, self.totient
        
        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
        return u1 % self.n

    def generate_private_key(self):
        self.d = self.mod_inverse()

    def print_keys(self):
        print('p: ', self.p)
        print('q: ', self.q)
        print('n: ', self.n)
        print('totient: ', self.totient)
        print('e: ', self.e)
        print('d: ', self.d)

    def encrypt_using_public_key(self, m: int):
        c = pow(m, self.e, self.n)
        return c

    def encrypt_using_private_key(self, m: int):
        c = pow(m, self.d, self.n)
        return c

    def decrypt_using_public_key(self, c: int):
        m = pow(c, self.e, self.n)
        return m

    def decrypt_using_private_key(self, c: int):
        m = pow(c, self.d, self.n)
        return m
