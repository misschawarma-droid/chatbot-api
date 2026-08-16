import random
from datetime import datetime, timedelta

def generate_verification_code() -> str:
    return "".join(random.choices("0123456789", k=6))

def get_expiry() -> datetime:
    return datetime.utcnow() + timedelta(minutes=10)