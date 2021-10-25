import random
die = random.SystemRandom() # A single dice.

def single_test(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
        
    if pow(a, exp, n) == 1:
        return True
        
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
            
        exp <<= 1
        
    return False
    
def miller_rabin(n, k=10):
    for i in range(k):
        a = die.randrange(2, n - 1)
        if not single_test(n, a):
            return False
            
    return True
    

            