#!/usr/bin/env python3
"""moduldule for web-related functions.
"""

import redis
import requests

# Initialize Redis connection
redis_client = redis.Redis()

def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a URL and caches the result in Redis.
    """
    # Check if the URL content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Retrieve HTML content from the URL
    response = requests.get(url)

    # Increment access count for the URL
    redis_client.incr(f"count:{url}")

    # Cache the HTML content with a 10-second expiration
    redis_client.setex(url, 10, response.text)

    return response.text

def get_url_access_count(url: str) -> int:
    """
    Retrieves the access count for a particular URL.
    """
    # Retrieve the access count from Redis
    count = redis_client.get(f"count:{url}")
    return int(count) if count else 0

if __name__ == "__main__":
    # Test the get_page function
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/https://example.com"
    print(get_page(url))

    # Test the get_url_access_count function
    print(f"Access count for {url}: {get_url_access_count(url)}")

