import random
import string

CHARS = string.ascii_uppercase + string.digits + "!#@"

def generate_coupon_code() -> str:
    suffix = "".join(random.choices(CHARS, k=7))
    return f"MISS-{suffix}"