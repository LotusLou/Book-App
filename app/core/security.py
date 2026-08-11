from hashlib import pbkdf2_hmac
from hmac import compare_digest
from os import urandom

_ITERATIONS = 310_000


def hash_password(password: str) -> str:
    salt = urandom(16)
    digest = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _ITERATIONS)
    return f"{_ITERATIONS}${salt.hex()}${digest.hex()}"


def verify_password(password: str, hashed_password: str) -> bool:
    iterations, salt_hex, digest_hex = hashed_password.split("$", 2)
    expected = pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt_hex),
        int(iterations),
    ).hex()
    return compare_digest(expected, digest_hex)
