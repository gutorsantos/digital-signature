import os

def read_msg_file():
    lines = ''
    with open('message.txt', 'r') as f:
        lines = f.readlines()

    return ' '.join(lines)

def read_file(filename):
    lines = ''
    with open(filename, 'r') as f:
        lines = f.readlines()

    return ' '.join(lines)


def read_bytes(filename):
    lines = ''
    with open(filename, 'rb') as f:
        lines = f.readlines()
    return lines[0]
    # return lines[1].rstrip()

def write_bytes(aes_key, filename):
    with open(filename, 'wb') as f:
        f.write(aes_key)


def write_file(txt, filename):
    with open(filename, 'w') as f:
        f.write(txt)

def is_file_empty(filename):
    return os.path.getsize(filename)