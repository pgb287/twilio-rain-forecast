from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import datetime


def get_date():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d")
    return current_date

def request_api(api_key, query):
    url_clima = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={query}&days=1&aqi=no&alerts=no"
    try:
        response = requests.get(url_clima).json()
    except Exception as e:
        print(e)
    return response

def get_forecast(response, i):
    fecha = response["forecast"]["forecastday"][0]["hour"][i]["time"].split()[0]
    hora = int(
        response["forecast"]["forecastday"][0]["hour"][i]["time"]
        .split()[1]
        .split(":")[0]
    )
    condicion = response["forecast"]["forecastday"][0]["hour"][i]["condition"]["text"]
    temperatura = response["forecast"]["forecastday"][0]["hour"][i]["temp_c"]
    lluvia = response["forecast"]["forecastday"][0]["hour"][i]["will_it_rain"]
    prob_lluvia = response["forecast"]["forecastday"][0]["hour"][i]["chance_of_rain"]
    return fecha, hora, condicion, temperatura, lluvia, prob_lluvia

def create_df(data):
    columns_name = [
        "Fecha",
        "Hora",
        "Condicion",
        "Temperatura",
        "Lluvia",
        "Prob_lluvia",
    ]
    df = pd.DataFrame(data, columns=columns_name)

    df_rain = df[(df["Lluvia"] == 1) & (df["Hora"] >= 6)]
    df_rain = df_rain[["Hora", "Condicion"]]
    df_rain = df_rain.set_index("Hora")
    return df_rain

def send_message(account_sid, auth_token, send_number, receive_number, current_date, df_rain, query):
    
    body_message = f"Hola!\nEl pronostico de lluvia para hoy {current_date} en {query} es:\n{str(df_rain)}"
    
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body = body_message,
            from_ = send_number,
            to = receive_number
        )
    return message.sid


api_key = API_KEY_WAPI
send_number = PHONE_NUMBER
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
receive_number = "+543886857117"
query = "San Salvador de Jujuy"
data = []

current_date = get_date()
response = request_api(api_key, query)

for i in tqdm(range(len(response["forecast"]["forecastday"][0]["hour"])), colour="green"):
    data.append(get_forecast(response, i))

df_rain = create_df(data)
message_id = send_message(account_sid, auth_token, send_number, receive_number, current_date, df_rain, query)
print('MENSAJE ENVIADO! ' + message_id)