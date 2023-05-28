import math
import sys
import zlib
import warnings
import random
import itertools


def kolmogorov(binary_str):
    st = bytes(binary_str, encoding='utf-8')
    if len(st) < 5:
        warnings.warn('''Kolmogorov approximation is not valid for strings 
                         smaller than len 5''')
    l = float(len(st))
    compr = zlib.compress(st)
    c = float(len(compr)-8)
    return c
