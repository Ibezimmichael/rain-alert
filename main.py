import requests
from twilio.rest import Client

twilio_sid = "Your twilio sid"
twilio_token = "Your twilio token"


url_token = "http://api.weatherapi.com/v1/current.json?"
forecast_token = "http://api.weatherapi.com/v1/forecast.json?"

parameters = {
    "q": "6.466990,3.287720",
    "key": 'Your API key',

}

response = requests.get(url=forecast_token, params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
forecast_data = weather_data["forecast"]["forecastday"]
hour_data = forecast_data[0]["hour"][0]["condition"]

new_data = forecast_data[0]["hour"][0:11]
condition_list = [data["condition"]["code"] for data in new_data]

will_rain = False
for data in new_data:
    condition_code = data["condition"]["code"]
    if 1175 <= condition_code <= 1195:
        will_rain = True

if will_rain:
    print("bring umbrella")
    client = Client(twilio_sid, twilio_token)
    message = client.messages \
        .create(
        body="it will rain today take and umbrella",
        from_='Your twilio number',
        to='Your personal number'
    )
    print(message.status)

else:
    client = Client(twilio_sid, twilio_token)
    message = client.messages \
        .create(
        body="no rain today",
        from_='Your twilio number',
        to='Your personal number'
    )
    print(message.status)
