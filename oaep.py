from hashlib import sha3_512, sha3_256
from generate_random import generate_random_int

class OAEP():
    k0 = 256
    size = 0

    def __init__(self, size):
        self.size = size

    def padding(self, m, msg_len):

        k1 = self.size - self.k0 - msg_len
        m_padded_bits = m
        while(m_padded_bits.bit_length() != self.size - self.k0):
            m_padded_bits = m_padded_bits << 1

        return m_padded_bits
    
    def unpadding(self, m_padded, msg_len):
        k1 = self.size - self.k0 - msg_len
        m_bits = m_padded
        while(m_bits.bit_length() != msg_len):
            m_bits = m_bits >> 1
        

        return m_bits

    def oaep(self, m, msg_len):
        bl_x = 0
        bl_y = 0
        while(True):
            m_padded_bits = self.padding(m, msg_len)
            r = generate_random_int(self.k0)
            G = sha3_512(str.encode(str(r)))
            X = m_padded_bits ^ int(G.hexdigest(), 16)

            H = sha3_256(str.encode(str(X)))

            Y = int(H.hexdigest(), 16) ^ r

            bl_x = X.bit_length()
            bl_y = Y.bit_length()
            if(bl_x == 768 and bl_y == 256):
                return str(X)+str(Y)

    def reverse_oaep(self, m_padded, msg_len):
        pos = int(3*len(m_padded)/4)
        X = m_padded[:pos]
        Y = m_padded[pos:]

        H = sha3_256(str.encode(X))
        r = int(Y) ^ int(H.hexdigest(), 16)
        
        G = sha3_512(str.encode(str(r)))
        m_padded = int(X)  ^ int(G.hexdigest(), 16)

        m_bits = self.unpadding(m_padded, msg_len)
        return m_bits

