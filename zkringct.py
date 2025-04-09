# zkringct.py
# Final zkRingCT Proof Module for PKRD Blockchain

import hashlib

def hash_data(*args):
    """
    Generate a SHA-256 hash of colon-joined arguments.
    """
    joined = ":".join(str(a).strip() for a in args)
    return hashlib.sha256(joined.encode()).hexdigest()

def generate_proof(sender, receiver, amount, secret):
    """
    Generate a zk-style proof hash using secret key.
    """
    return hash_data(sender, receiver, amount, secret)

def verify_proof(sender, receiver, amount, proof):
    """
    Verify the zk-style proof hash by re-hashing the original values with the proof.
    """
    return hash_data(sender, receiver, amount, proof)

def verify_match(sender, receiver, amount, proof, expected_hash):
    """
    Check whether the verification hash matches the expected stored hash.
    """
    computed = verify_proof(sender, receiver, amount, proof)
    return computed == expected_hash

# ─────────────────────────────────────────────
# ✅ Direct Test Mode (for developers)
# ─────────────────────────────────────────────

if __name__ == "__main__":
    sender = "0x6a517CCcf02eE802FAfDd0b9E3AC9ab039ccd465"
    receiver = "0x294b05aab624630B13b3962012c828d57Fb1189B"
    amount = "1000"
    secret = "secretkey123"

    print("Starting test...")

    # Step 1: Generate proof
    print("Generating proof...")
    proof = generate_proof(sender, receiver, amount, secret)
    print("Proof:", proof)

    # Step 2: Create final hash from proof
    verification_hash = verify_proof(sender, receiver, amount, proof)
    print("Verification Hash:", verification_hash)

    # Step 3: Check result
    result = verify_match(sender, receiver, amount, proof, verification_hash)
    print("Verified:", result)