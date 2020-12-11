def factorial(n):
    l = [1] * (n + 1)
    for i in range(2, n + 1):
        l[i] = l[i - 1] * i
    return l

def combinations(n, k, fac=None):
    if k > n or k < 0: return 0
    if k == 0 or k == n: return 1
    if fac is None:
        fac = factorial(n)
    return fac[n] // (fac[k] * fac[n - k])

def data_prob(n, max_number=9, pieces=10, fixed=0):
    if fixed > n: return 0
    if n < 0 or n > pieces: return 0
    total = ((max_number + 1) * (max_number)) // 2
    total += max_number + 1
    fac = factorial(total)
    num = combinations(max_number + 1 - fixed, n - fixed, fac) * combinations(total - max_number - 1, pieces - n, fac)
    den = combinations(total, pieces)
    return num / den

def one_piece_prob(max_number=9, pieces=10):
    total = ((max_number + 1) * (max_number)) // 2
    total += max_number + 1
    fac = factorial(total)
    num = combinations(total - 1, pieces - 1, fac)
    den = combinations(total, pieces)
    return num / den

def possible_hands(total, k, players=4):
    fac = factorial(total)
    result = 1
    for _ in range(players):
        result *= combinations(total, k, fac)
        total -= k
    return result

if __name__ == "__main__":
    print(data_prob(int(input('Cuantas quieres en la data: '))))
    
