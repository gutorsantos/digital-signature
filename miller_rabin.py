import random
r = random.SystemRandom()

def test(n, a):
    e = n - 1
    while not e & 1:
        e >>= 1
        
    if pow(a, e, n) == 1:
        return True
        
    while e < n - 1:
        if pow(a, e, n) == n - 1:
            return True
            
        e <<= 1
        
    return False
    
def miller_rabin(n, k=10):
    for i in range(k):
        a = r.randrange(2, n - 1)
        if not test(n, a):
            return False
            
    return True
    

            