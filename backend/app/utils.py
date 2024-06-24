def hash_password(password: str) -> str:
    # Example function to hash passwords
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
