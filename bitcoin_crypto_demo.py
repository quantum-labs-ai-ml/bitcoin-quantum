# Simplified Bitcoin Cryptography Demo
# WARNING: This uses a toy elliptic curve with small parameters for educational purposes.
# Bitcoin uses secp256k1, which is secure due to large parameters.

import hashlib
import random

# Toy elliptic curve parameters (small and insecure)
# y^2 = x^3 + ax + b (mod p)
a = 2
b = 3
p = 17  # Small prime modulus
G = (5, 1)  # Generator point (base point)
n = 19  # Order of G (small for demo)

# Point addition on elliptic curve
def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == -y2 % p:
        return None
    if P != Q:
        lam = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    else:
        lam = ((3 * x1 * x1 + a) * pow(2 * y1, -1, p)) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

# Scalar multiplication: k * P
def scalar_mult(k, P):
    result = None
    temp = P
    while k:
        if k & 1:
            result = point_add(result, temp)
        temp = point_add(temp, temp)
        k >>= 1
    return result

# Generate key pair
def generate_keys():
    private_key = random.randint(1, n-1)
    public_key = scalar_mult(private_key, G)
    return private_key, public_key

# Sign a message (simplified ECDSA-like)
def sign_message(message, private_key):
    k = random.randint(1, n-1)  # Ephemeral key
    R = scalar_mult(k, G)
    r = R[0] % n
    if r == 0:
        return sign_message(message, private_key)  # Retry if r=0
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % n
    s = (pow(k, -1, n) * (h + private_key * r)) % n
    if s == 0:
        return sign_message(message, private_key)  # Retry if s=0
    return (r, s)

# Verify signature
def verify_signature(message, signature, public_key):
    r, s = signature
    if r < 1 or r >= n or s < 1 or s >= n:
        return False
    h = int(hashlib.sha256(message.encode()).hexdigest(), 16) % n
    s_inv = pow(s, -1, n)
    u1 = (h * s_inv) % n
    u2 = (r * s_inv) % n
    P = point_add(scalar_mult(u1, G), scalar_mult(u2, public_key))
    if P is None:
        return False
    return P[0] % n == r

# Brute-force attack to recover private key
def brute_force_attack(public_key):
    print("Attempting brute-force attack...")
    for d in range(1, n):
        candidate = scalar_mult(d, G)
        if candidate == public_key:
            print(f"Private key found: {d}")
            return d
    print("Private key not found (should not happen in this demo).")
    return None

# Demo
def main():
    print("=== Bitcoin Cryptography Demo (Simplified) ===")
    
    # Generate keys
    private_key, public_key = generate_keys()
    print(f"Private key: {private_key}")
    print(f"Public key: {public_key}")
    
    # Sign a transaction
    message = "Send 1 BTC to Alice"
    signature = sign_message(message, private_key)
    print(f"Message: {message}")
    print(f"Signature: {signature}")
    
    # Verify signature
    is_valid = verify_signature(message, signature, public_key)
    print(f"Signature valid: {is_valid}")
    
    # Simulate attack
    print("\n=== Simulating Brute-Force Attack ===")
    recovered_key = brute_force_attack(public_key)
    if recovered_key:
        # Try signing with recovered key
        new_signature = sign_message(message, recovered_key)
        is_valid = verify_signature(message, new_signature, public_key)
        print(f"Signature with recovered key valid: {is_valid}")
    
    print("\nNote: This demo uses a tiny curve (p=17, n=19). Bitcoin uses secp256k1 with a 256-bit key, making brute-force infeasible.")

if __name__ == "__main__":
    main()
