from slowapi import Limiter
from slowapi.util import get_remote_address

# Create limiter instance in main.py or a separate initialization function
limiter = Limiter(key_func=get_remote_address)