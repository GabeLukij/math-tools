# math-tools
This repo contains some useful functions I made while doing research in number theory. I've consolidated them into one file for ease of integration in case anyone would like to use them in their own scripts.

### Quick Inverse, quick_inverse(a, m):
This function is used for finding a numbers inverse modulo m. At the moment it is only designed to work using a prime number for m. It utilizes Fermat's Little Theorem, which states <br />
&emsp; $$a^{p-1} \equiv 1 \mod p\$$ <br />
for $a \in \mathbb{Z} _p    $, $p \in \mathbb{P}$ where $\mathbb{P}$ denotes the set of prime numbers.

An implication of this theorem is the following: <br />
&emsp; $$a^{p-2} \equiv a^{-1}\mod p\$$ <br />
where $$aa^{-1} \equiv 1\mod p\$$.

Instead of creating a loop that iterates $p$ times, this function uses the binary equivalent of $p$ and performs one loop for each binary digit, allowing the process to complete in $O(log(n))$ time instead of $O(n)$ time.

### Solve a, solve_a(m, n, s, t):
Given an integers $a, m, n$ where $m$ and $n$ are coprime, $a \equiv s \mod m$ and $a \equiv t \mod n$, this function solves for the integer $u$ such that $a \equiv u \mod mn$.

This function uses quick_inverse(m, n), so it is recommended to use the smaller of the two modular bases as n.

The motivation for this was to help solve for inverses under non-prime moduli.
Consider a $b$ such that $b \in \mathbb{Z}_{mn}$. Say $b \equiv b_m \mod m$ and $b \equiv b_n \mod n$. It follows by necessity that $b^{-1} \equiv b_m^{-1} \mod m$ and $b^{-1} \equiv b_n^{-1} \mod n$. This function makes it possible to find the inverse of a number modulo a non-prime number by breaking that modulus up into its prime factors, solving for each of those individual inverses, and then using those smaller inverses to compute the inverse under the original modulus. Note that this function alone will not be enough if the modulus is divisible by any $p_i^a$ with $a>1$.

## Prime number list generators
I included a few different versions of a prime list generating functions, all of which I've had to use at some point. They all use the Sieve of Eratosthenes and basically only differ by the loop parameters.

### Length-based, prime_list_len(upper_lim):
This returns the list of primes starting at 2 with length (upper_lim).

### Binary length-based, prime_list_bin_len(maxlen):
This returns the list of primes whose binary representation as at most (maxlen) digits.

### Square root-based, prime_list_root_bound(upper_bound):
This returns the list of primes up to the square root of (upper_bound). One use of this list is to check whether or not any number less than or equal to the input is itself prime.

### Simple bound input-based, prime_list_bound(upper_bound):
This returns the list of primes up to (upper_bound).


____________________________________

### Factoring function, factorizer(n):
Returns the prime factorization of $n$ in the form of a dictionary where the prime factors are the keys and the exponents are their corresponding values.
For example, with an input of 24 you'd get the following dictionary: {2: 3, 3:1}. 
<br /> NOTE! It gets slow once you get past 7 digits.

### Smallest primorial less than input, upper_primorial_lim(n):
This function returns the smallest primorial number less than a given $n$. Primorial numbers (denoted by $p_i$#) are the product of the first $i$ consecutive primes.
