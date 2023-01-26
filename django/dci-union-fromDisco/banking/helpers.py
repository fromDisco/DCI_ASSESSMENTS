from forex_python.converter import CurrencyRates
from countryinfo import CountryInfo

def get_country_names_currs():
    currency_instance = CurrencyRates()
    currency_names = currency_instance.get_rates("USD").keys()
    key = "name"
    val = "currencies"
    country_info = CountryInfo()
    countries_all = country_info.all()

    response = []
    for country_val in countries_all.values():
        if country_val.get(val, [""])[0] in currency_names:
            response.append((country_val.get(val)[0], country_val.get(key)))

    return response
    

def get_country_name(country_curr) -> str:
    countries_list = get_country_names_currs()
    country_name = [ country[1] for country in countries_list if country[0] == country_curr]


if __name__ == "__main__":
    print(get_country_name("MYR"))