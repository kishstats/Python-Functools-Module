import requests
import time
from functools import wraps


def retry_requests(max_retries=3, delay=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    response = func(*args, **kwargs)
                    print(
                        f"Request to {response.url} returned status code {response.status_code}"
                    )

                    if response.status_code == 200:
                        return response
                    elif response.status_code == 429:
                        print("Rate limited. Waiting and retrying.")
                        time.sleep(delay)
                    elif 500 <= response.status_code < 600:
                        print("Server error. Retrying after delay.")
                        time.sleep(delay)
                    else:
                        response.raise_for_status()
                except requests.RequestException as e:
                    if attempt < max_retries - 1:
                        print(
                            f"Request failed with error: {str(e)}. Retrying in {delay} seconds."
                        )
                        time.sleep(delay)
                    else:
                        print("Max retries reached. Request failed.")
                        raise
            return None

        return wrapper

    return decorator


@retry_requests(max_retries=2, delay=3)
def fetch_data(url, params=None):
    """Say Hello

    Parameters:
    url (string)
    params (dict|None)
    """
    return requests.get(url, params)


httpbin_url = "https://httpbin.org/get"
httpbin_error_url = "https://httpbin.org/status/429"

# response = requests.get(httpbin_url, params={"test": "true"})
response = fetch_data(httpbin_url, params={"test": "true"})
if response:
    result = response.json()
    print("result", result)
else:
    print("No reponse received")

response = fetch_data(httpbin_error_url, params={"test": "true"})
if response:
    result = response.json()
    print("result", result)
else:
    print("No reponse received")

print(fetch_data.__name__)  # fetch_data

print(fetch_data.__doc__)
# prints:
# Say Hello

#     Parameters:
#     url (string)
#     params (dict|None)
