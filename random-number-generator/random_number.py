# random_number.py

MOD = 2**32        # 4294967296, modulus
A = 1664525        # multiplier (A % 4 == 1)
C = 1013904223     # increment (must be odd and gcd(C, MOD) == 1)

# Global seed variable
seed = None

def generate_seed():
    # Generate a seed using the memory address of a temporary object
    temp = object()
    return id(temp) % MOD

# Initialize seed
seed = generate_seed()

def random_seed():
    # Update and return the next pseudo-random seed using the LCG formula
    global seed
    seed = (A * seed + C) % MOD
    return seed

def random_number(low, high):
    """
    Return a pseudo-random number between low and high (inclusive).
    
    Args:
        low (int): Lower bound of the range.
        high (int): Upper bound of the range.
    
    Returns:
        int: Random number in [low, high]
    """
    if low > high:
        raise ValueError("low must be less than or equal to high")
    r = random_seed()
    return low + (r % (high - low + 1))

# Example usage
if __name__ == "__main__":
    print("Random number between 0 and 10:", random_number(0, 10))
