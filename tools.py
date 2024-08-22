import math

def quick_inverse(a, m):
    """
    This function takes two coprime integers (a, m) as an input and returns the inverse of a modulo m
    """
    actual_target = m - 2
    mod_base = str(bin(actual_target))[2:]
    n = len(mod_base)
    final = 1
    i = 1
    while i <= n:          
        if mod_base[n-i] == "1":
            final = (final * a) % m
        a = (a*a) % m
        i += 1
    return final

def solve_a(m, n, s, t):
    """
    This function takes four integers (m, n, s, t) as an input with m and n being coprime. It's used to solve for a 
    where |a mod m = s| and |a mod n = t|.
    """
    m_inv = quick_inverse(m, n)
    a = m * ((m_inv * (t - s)) % n) + s
    return a 

def prime_list_len(upper_lim):
    """
    This function takes one integer (upper_lim) as an input and will return a list of that many prime numbers starting with 2.
    """
    primes = [2]
    i = 3
    while len(primes) < upper_lim:
        prime_check = True
        for prime in primes:
            if prime > math.sqrt(i):
                break
            if i % prime == 0:
                prime_check = False
                break
        if prime_check:
            primes.append(i)
        i += 1
    return primes

def prime_list_bin_len(maxlen):
    primes = [2]
    i = 3
    while len(bin(primes[-1]))-2 < maxlen:
        prime_check = True
        for prime in primes:
            if prime > math.sqrt(i):
                break
            if i % prime == 0:
                prime_check = False
                break
        if prime_check:
            primes.append(i)
        i += 1
    return primes


def prime_list_bound(upper_bound):
    """
    This function takes one integer (upper_lim) as an input and will return a list of prime numbers less than its square root starting with 2.
    """
    primes = [2]
    i = 3
    while primes[-1] < math.sqrt(upper_bound):
        prime_check = True
        for prime in primes:
            if prime > math.sqrt(i):
                break
            if i % prime == 0:
                prime_check = False
                break
        if prime_check:
            primes.append(i)
        i += 1
    return primes

def factorizer(n):
    primes = prime_list_bound(n)

    factors = {}




    def cycle(n, i):
        while i < len(primes):
            curr_path = []
            p = primes[i]
            if p > math.sqrt(n):
                if n > 1:
                    if n not in factors.keys():
                        factors[n] = 1
                    else:
                        factors[n] += 1
                    return
                else:
                    return
            a = p
            while a not in curr_path:
                curr_path.append(a)
                a = (a*p)%n
            if 1 not in curr_path:
                if p not in factors.keys():
                    factors[p] = 1
                else:
                    factors[p] += 1
                cycle(n//p, i)
                return
            else:
                i += 1

    cycle(n, 0)

    return factors

def upper_primorial_lim(n):
    """
    This function takes an integer n and returns the order of the smallest primorial number larger than n. 
    The kth primorial number is the product of the first k primes.
    """
    primes = [2]
    i = 3
    primorial = 2
    while primorial < n:
        prime_check = True
        for prime in primes:
            if prime > math.sqrt(i):
                break
            if i % prime == 0:
                prime_check = False
                break
        if prime_check:
            primes.append(i)
            primorial *= i
        i += 1
    return len(primes)