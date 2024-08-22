# math-tools
This repo contains some functions I made that were useful during some number theory research. I've consolidated them into one file for ease of integration in case anyone would like to try them out.

## Quick Inverse: quick_inverse(a, m):
This function is used for finding a numbers inverse modulo m. At the moment it is only designed to work using a prime number for m. It utilizes Fermat's Little Theorem.
$$ a^(p-1) equiv 1 mod p $$
