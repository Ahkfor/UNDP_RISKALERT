from urllib import request
import pandas as pd
import json


def fetch_data(base_url):
    """
    Fetch data from the provided base_url with pagination support.

    Args:
    - base_url (str): The base URL endpoint to fetch data from.

    Returns:
    - list: A list of fetched results.
    """

    with request.urlopen(base_url) as response:
        json_data = json.loads(response.read().decode('utf-8'))
        data = json_data['data']
        df = pd.json_normalize(data, sep='_')
    df.to_csv('data.csv', index=False)
    return df


def construct_url(APP_IDENTIFIER, THEME, LIMIT, country=None):
    '''
    Construct an url for data requests
    :param APP_IDENTIFIER: string
    :param THEME: string
    :param LOCATION: string
    :return: constructed url as string
    '''
    if country:
        BASE_URL = (
            f"https://api.reliefweb.int/v1/{THEME}?"
            f"appname={APP_IDENTIFIER}"
            f"&query[fields][]=country&query[value]={country}"
            f"&limit={LIMIT}"
        )
    else:
        BASE_URL = (
            f"https://api.reliefweb.int/v1/{THEME}?"
            f"appname={APP_IDENTIFIER}"
            f"&limit={LIMIT}"
        )
    return BASE_URL


def read_report(url):
    with request.urlopen(url) as response:
        json_data = json.loads(response.read().decode('utf-8'))
        body = json_data["data"][0]["fields"]["body"]
    return body