import requests
import json
from mysite.settings import API_KEY


def api_call(url, api_host, params=None):
    url = url
    params = params
    headers = {"X-RapidAPI-Key": API_KEY, "X-RapidAPI-Host": api_host}
    response = requests.request("GET", url, headers=headers, params=params)
    return json.loads(response.text)
