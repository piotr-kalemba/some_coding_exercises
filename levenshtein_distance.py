

def memoize(func):
    memo = {}
    def memoizer(*args):
        key = str(args)
        if key not in memo:
            memo[key] = func(*args)
        return memo[key]
    return memoizer

@memoize
def ld(s, t):
    if len(s) == 0 or len(t) == 0:
        return max(len(s), len(t))
    cost = 1 if s[-1] != t[-1] else 0
    return min([ld(s[:-1], t) + 1, ld(s, t[:-1]) + 1, ld(s[:-1], t[:-1]) + cost])


if __name__ == '__main__':
    s = 'levenhaim'
    t = 'levenshtein'
    dist = ld(s, t)
    print(dist)