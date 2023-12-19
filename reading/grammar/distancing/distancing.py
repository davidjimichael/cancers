import math as m
import numpy as np

def abs(a):
    return int(m.sqrt(a**2))

# return token range in content using origin index=i; skipping givens.
# the quick brown fox jumped over the lazy dog. great fucking fox!
def token_range(i, content, low=1, high=1, skips=[]):
    start = 0 if i - low < 0 else i - low
    end = 2 + (len(content) if i + high > len(content) else i + high)
    res = [(c, abs(j-i+1)) for (j,c) in enumerate(content[start:end])]
    return [r for r in res if r[0] not in skips]
