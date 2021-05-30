import time
from concurrent.futures import ThreadPoolExecutor
from functools import wraps

import requests
from tqdm import tqdm


def timeit(method):
    @wraps(method)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        return result

    return wrapper


def attack_one(url):
    try:
        response = requests.request("GET", url)
        return response.text.encode("utf8")
    except Exception as e:
        print(f"We caught exception! It says that: {e}")



@timeit
def attack_all(urls):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(
            tqdm(executor.map(attack_one, urls, timeout=60), total=len(urls))
        )
        return results


if __name__ == "__main__":
    url = "http://localhost:8000/channel"
    urls = [url] * 500

    results = attack_all(urls)