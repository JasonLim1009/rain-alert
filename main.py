import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "79b888d2b147d0f96b2ca714cad2d847"
account_sid = 'ACc67530b1a4c2c0695ab0ab91cb702443'
auth_token = 'fa53ed9217a7fefdcbbb561f35cfaa79'

weather_params = {
    "lat": 3.001595,
    "lon": 101.542589,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.json())

response.raise_for_status()
weather_data = response.json()
# print(weather_data['hourly'][0]['weather'][0])

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_='+12342306987',
        to='+60149849038'
    )

    print(message.status)

    # https://www.latlong.net/Show-Latitude-Longitude.html
    # https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
    # https: // www.pythonanywhere.com / user / JASONLIM9 / tasks_tab /
    # 在这个网站的代码不一样，需要添加一些代码在里面才能发送sms

    # import requests
    # import os
    # from twilio.rest import Client
    # from twilio.http.http_client import TwilioHttpClient
    #
    # OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
    # api_key = os.environ.get('OWM_API_KEY')
    # account_sid = 'ACc67530b1a4c2c0695ab0ab91cb702443'
    # auth_token = os.environ.get('AUTH_TOKEN')
    #
    # weather_params = {
    #     "lat": 3.001595,
    #     "lon": 101.542589,
    #     "appid": api_key,
    #     "exclude": "current,minutely,daily"
    # }
    #
    # response = requests.get(OWM_Endpoint, params=weather_params)
    #
    # response.raise_for_status()
    # weather_data = response.json()
    #
    # weather_slice = weather_data["hourly"][:12]
    #
    # will_rain = False
    #
    # for hour_data in weather_slice:
    #     condition_code = hour_data["weather"][0]["id"]
    #     if int(condition_code) < 700:
    #         will_rain = True
    #
    # if will_rain:
    #     proxy_client = TwilioHttpClient()
    #     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    #
    #     client = Client(account_sid, auth_token, http_client=proxy_client)
    #
    #     message = client.messages \
    #         .create(
    #         body="It's going to rain today. Remember to bring an ☔",
    #         from_='+12342306987',
    #         to='+60149849038'
    #     )
    #
    #     print(message.status)

        # 隐藏api / token
        # export OWM_API_KEY=79b888d2b147d0f96b2ca714cad2d847
        # export AUTH_TOKEN=fa53ed9217a7fefdcbbb561f35cfaa79