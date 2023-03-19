import argparse

args = argparse.ArgumentParser()
args.add_argument("--file")
args = args.parse_args()

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()
opened_file.close()


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


decode_Caesar_cipher(encoded_text, -13)
