import json
from urllib import request


def fetch_data(base_url, limit=1000):
    """
    Fetch data from the provided base_url with pagination support.

    Args:
    - base_url (str): The base URL endpoint to fetch data from.
    - limit (int): The number of records to fetch per request.

    Returns:
    - list: A list of fetched results.
    """

    idx = 0
    results = []

    while True:
        offset = idx * limit
        url = f"{base_url}&offset={offset}&limit={limit}"

        with request.urlopen(url) as response:
            print(f"Getting results {offset} to {offset+limit-1}")
            json_response = json.loads(response.read())

            results.extend(json_response['data'])

            # If the returned results are less than the limit,
            # it's the last page
            if len(json_response['data']) < limit:
                break

        idx += 1

    return results


APP_IDENTIFIER = {'U2h1cmVuIFdhbmc6c3czOTkxQGNvbHVtYmlhLmVkdQ=='}
THEME = "coordination-context/operational-presence"
LOCATION = "AFG"
BASE_URL = (
    f"https://hapi.humdata.org/api/v1/{THEME}?"
    f"output_format=json"
    f"&location_code={LOCATION}"
    f"&app_identifier={APP_IDENTIFIER}"
)

LIMIT = 1000

results = fetch_data(BASE_URL, LIMIT)
print(results)