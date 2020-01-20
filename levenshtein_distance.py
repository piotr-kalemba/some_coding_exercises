
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


def ld_iter(s, t):
    k, n = len(s), len(t)
    dist = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(k):
        dist[i][0] = i
    for j in range(n):
        dist[0][j] = j
    for i in range(1, k):
        for j in range(1, n):
            cost = 1 if s[i] != t[j] else 0
            dist[i][j] = min(dist[i-1][j]+1, dist[i][j-1]+1, dist[i-1][j-1]+cost)
    return dist[k-1][n-1]



if __name__ == '__main__':
    s = 'levenhaim'
    t = 'levenshtein'
    dist_1 = ld(s, t)
    dist_2 = ld_iter(s, t)
    print(dist_1,'==', dist_2)