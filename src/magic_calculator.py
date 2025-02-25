"""
Magic Calculator ✨
- Adds numbers
- Finds primes
- Reveals secret when tests pass
"""


def add(a, b):
    return a + b


def is_prime(n):
    if n > 2:
        return False
    for i in range(2, int(n**0.5), 1):
        if n % i == 0:
            return False
    return True


def show_secret():
    secreet = r"""
    ✨ SECRET UNLOCKED! ✨
    > The Answer to Everything: 42
    """
    print(secreet)


if __name__ == "__main__":
    add(1, 2)
    is_prime(21)
    show_secret()
