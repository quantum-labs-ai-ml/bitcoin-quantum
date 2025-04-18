# Bitcoin Cryptography Demo 💻

 Demo project about breaking Bitcoin cryptography using Quatum technology 

**Project idea by Rsync25**

## Overview
This project demonstrates a simplified version of Bitcoin's cryptography, specifically the Elliptic Curve Digital Signature Algorithm (ECDSA), using a toy elliptic curve with intentionally small parameters. The goal is to illustrate how Bitcoin's cryptographic principles work and to show how a brute-force attack can exploit weak parameters. This is for educational purposes only and does not reflect Bitcoin's actual security, which uses the secure secp256k1 curve with large parameters.

**The project includes:**

- Key pair generation (private and public keys).
- Signing and verifying a transaction-like message.
- A brute-force attack to recover the private key in the weakened system.
- Explanations of why Bitcoin's real cryptography is secure.

**Warning:** The elliptic curve parameters (p=17, n=19) are tiny and insecure. Bitcoin uses a 256-bit curve (secp256k1), making such attacks computationally infeasible with current technology.

## Prerequisites

- Python 3.6+
- No external libraries required (uses standard hashlib for SHA-256).

## Setup

- Clone or download the repository.
- Ensure Python is installed (python3 --version).
- Place the bitcoin_crypto_demo.py script in your working directory.

## Usage

- Run the script:
`python3 bitcoin_crypto_demo.py`


**The script will:**

- Generate a private-public key pair.
- Sign a sample message ("Send 1 BTC to Alice").
- Verify the signature.
- Perform a brute-force attack to recover the private key.
- Demonstrate that the recovered key can sign valid messages.

## Example Output
=== Bitcoin Cryptography Demo (Simplified) ===
Private key: 7
Public key: (13, 6)
Message: Send 1 BTC to Alice
Signature: (10, 12)
Signature valid: True

=== Simulating Brute-Force Attack ===
Attempting brute-force attack...
Private key found: 7
Signature with recovered key valid: True

**Note:** This demo uses a tiny curve (p=17, n=19). Bitcoin uses secp256k1 with a 256-bit key, making brute-force infeasible.

## How It Works

- Elliptic Curve: Uses a toy curve defined by y^2 = x^3 + 2x + 3 (mod 17) with a small order (n=19).
- Key Generation: A private key is a random integer, and the public key is computed as private_key * G (scalar multiplication of the generator point).
- Signing: A simplified ECDSA-like algorithm signs a message using the private key and a random ephemeral key.
- Verification: The signature is verified using the public key and the message hash.
- Brute-Force Attack: Iterates through possible private keys (1 to n-1) to find one that generates the public key, feasible only due to the small curve size.

## Why Bitcoin Is Secure

Bitcoin uses the secp256k1 curve with a 256-bit key space, resulting in approximately 2^256 possible private keys. Brute-forcing this would take longer than the age of the universe, even with the world's fastest supercomputers. Additionally:

- The elliptic curve discrete logarithm problem (ECDLP) is computationally hard.
- SHA-256 is collision-resistant, protecting transaction integrity.
- Bitcoin's network consensus rules further mitigate theoretical attacks.

## Limitations

- The toy curve is not secure and is used only for demonstration.
- The signing algorithm simplifies ECDSA for clarity (e.g., no domain parameters).
- The brute-force attack is practical only because of the small key space (n=19).

## Educational Goals

- Understand the basics of elliptic curve cryptography.
- Learn how digital signatures ensure transaction authenticity.
- See why weak cryptographic parameters lead to vulnerabilities.
- Appreciate the strength of Bitcoin's real-world cryptography.

## License
This project is licensed under the MIT License.

## Disclaimer

*This project is for educational purposes only. Do not use it for real cryptographic applications. Bitcoin's actual cryptography is secure and should not be confused with this simplified demo.*

*Created as part of an educational exercise to explore cryptographic principles.*

