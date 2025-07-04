import os
import requests


def test_currency_list():
    url = f"https://restcountries.com/v3.1/currency/{os.getenv("CURRENCY")}"
    currency_req = requests.get(url=url)
    response = currency_req.json()
    assert currency_req.status_code == 200
    assert response[0].get("name").get("common") == "Vietnam"
    print(response[0].get("name"))


def test_language_list():
    url = f"https://restcountries.com/v3.1/lang/{os.getenv("LANGUAGE")}"
    language_req = requests.get(url=url)
    response = language_req.json()
    assert language_req.status_code == 200
    assert response[0].get("name").get("common") == "Vietnam"
    print(response[0].get("name"))


def test_capital():
    url = f"https://restcountries.com/v3.1/capital/{os.getenv("CAPITAL")}"
    capital_req = requests.get(url=url)
    response = capital_req.json()
    assert capital_req.status_code == 200
    assert response
    print(response[0].get("demonyms"))
