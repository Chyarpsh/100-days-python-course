import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("3969d049c6e5303149e86f63fd2973ae")
account_sid = "ACb6af81946239f5fc3b281ac4e2c2657b"
auth_token = os.environ.get("de9284a75203ec64cdfa7e453f9dd80a")

weather_params = {
    "lat": 46.947975,
    "lon": 7.447447,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18557302536",
        to="+16824454930"
    )
    message = client.messages.create(
        from_="+1 (415) 523-8886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="+16824454930"
    )
    print(message.status)