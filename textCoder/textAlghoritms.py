from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode(plaintext, rails):
    p = rail_pattern(rails)
    # this relies on key being called in order, guaranteed?
    return ''.join(sorted(plaintext, key=lambda i: next(p)))


def decode(ciphertext, rails):
    p = rail_pattern(rails)
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)
    for i, c in zip(indexes, ciphertext):
        result[i] = c
    return ''.join(result)