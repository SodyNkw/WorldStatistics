import requests
import plotly.express as px
import os
from dotenv import load_dotenv

load_dotenv(override=True)
api_key=os.getenv("SECRET_API_KEY")

headers = {
    'X-CSCAPI-KEY': api_key
}

response = requests.get(
    'https://api.countrystatecity.in/v1/countries',
    headers=headers
)
countries = response.json()
data = []
for i in range(len(countries)):
    country_code = countries[i]["iso3"]
    capital_city = countries[i]["capital"]
    data.append((country_code, capital_city))



fig = px.choropleth(data, locations=0, color=1)
fig.show()