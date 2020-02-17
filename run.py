"""Program will give live currency conversion from usd to inr"""
from requests import get, exceptions


def url_connect(url="https://free.currconv.com/api/v7/convert?q=USD_INR&"
                    "compact=ultra&apiKey=2904075a6c4da237d8d2"):
    """ Function to connect and verify SSL certificate """
    try:
        _ = get(url, verify=True)  # Verifying SSL certificate using verify
        return 'Success'
    except exceptions.ConnectionError as e_ex:
        return e_ex


if __name__ == '__main__':
    print(url_connect())
