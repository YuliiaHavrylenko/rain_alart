import requests
from twilio.rest import Client

account_sid = "account_sid"
auth_token = "auth_token"
api_key = "api_key"
parameters = {
    "lat": 34.693737,
    "lon": 135.502167,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                        params=parameters)
response.raise_for_status()
weather_data = response.json()
id_list = []


def check_rain():
    for id_weather in id_list:
        if id_weather < 700:
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body="It's going to rain today. Remember to bring an ☔️",
                from_="number",
                to="number"
            )
            print(message.status)
            break


for i in range(0, 12):
    id_list.append(weather_data["hourly"][i]["weather"][0]["id"])


check_rain()