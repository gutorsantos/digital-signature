from file import is_file_empty, read_bytes, read_msg_file, write_bytes, write_file, read_file
from rsa import __RSA__
from oaep import OAEP
from aes import __AES__
import binascii
import base64
from hashlib import sha3_512, sha3_256

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def generate_aes_symetric_key(rsa: __RSA__, aes: __AES__, oaep: OAEP):
    print('Gerando chaves assimetrica e chave simetrica')
    while(True):
        rsa.generate_keys()

        decrypted = 0
        aes.generate_key()
        # print('AES KEY: ', aes.key)


        padd = oaep.oaep(int(aes.key), 128)
        encrypted = rsa.encrypt_using_public_key(int(padd))
        decrypted = rsa.decrypt_using_private_key(encrypted)
        unpadd = oaep.reverse_oaep(str(decrypted), 128)


        # padd = oaep.oaep(encrypted, encrypted.bit_length())
        # print('padd: ', padd)
        if(int(unpadd) == int(aes.key)):
            write_file(str(encrypted), 'aes.pem')
            break

    print(GREEN+'Chaves geradas com sucesso!'+RESET)
    print()

def sender(rsa: __RSA__, aes: __AES__, oaep: OAEP):
    generate_aes_symetric_key(rsa, aes, oaep)

    print('Simulando o envio de uma messagem!')

    # rsa.print_keys()
    # print(aes.key)

    msg = read_file('message.txt')
    encrypted = aes.encrypt(msg)
    write_bytes(encrypted, 'message_sent.txt')
    print('Messagem enviada!')
    print()

    hashed_encrypted_msg = sha3_512(str.encode(str(int.from_bytes(encrypted, 'big'))))
    # hashed_encrypted_msg = sha3_512(str.encode(int.from_bytes(encrypted, 'big')))
    write_file(hashed_encrypted_msg.hexdigest(), 'cert.pem')
    print('Assinatura gerada!')
    # decrypted = aes.decrypt(encrypted)

def receiver(rsa: __RSA__, aes: __AES__, oaep: OAEP):
    print('Simulando recebimento de uma mensagem!')
    encrypted_sk = read_file('aes.pem')
    decrypted_sk = rsa.decrypt_using_private_key(int(encrypted_sk))
    sk = oaep.reverse_oaep(str(decrypted_sk), 128)
    # print(sk)

    encrypted_msg = read_bytes('message_sent.txt')
    decrypted = aes.decrypt(encrypted_msg)
    print('Mensagem recebida: ', decrypted.decode('latin-1').rstrip('0'))
    # print(decrypted)
    

    print('Verificando autenticidade dessa mensagem!', end=' ')
    hashed_encrypted_msg = sha3_512(str.encode(str(int.from_bytes(encrypted_msg, 'big'))))
    signature = read_file('cert.pem')
    # print('HASHED AFTER DECRYPTION: ', hashed_encrypted_msg.hexdigest())
    # print('HASHED FROM FILE: ', signature)

    if(signature == hashed_encrypted_msg.hexdigest()):
        print(GREEN+"AUTENTICA! ✓"+RESET)
    else:
        print(RED+"NAO AUTENTICA! ✕"+RESET)



def main():

    if(not is_file_empty('message.txt')):
        print('Insira uma mensagem no arquivo "message.txt".')
        return

    
    rsa = __RSA__()
    oaep = OAEP(1024)
    aes = __AES__()


    sender(rsa, aes, oaep)
    print('Deseja verificar mensagem? (Y/n)', end='')
    x = str(input())
    print()
    if(x == 'y'):
        receiver(rsa, aes, oaep)


if __name__ == '__main__':
    main()

