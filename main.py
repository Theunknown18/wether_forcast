import requests
import os
OWM_ENDPONIT="https://api.openweathermap.org/data/2.5/forecast"
api_key=os.environ.get("API_KEY")
phone_number=os.environ.get("PHONE_NUMBER")
api_key_for_callmebot=os.environ.get("API_FOR_CALLMEBOT")
weather_params={

"lat":"Your_lat",
"lon":"Your_lon",
"appid":api_key,
"units":"metric",
"cnt":"4",
}
whatsapp_params={
    "phone":phone_number,
    "text":"Its%20gonna%20rain%20%2C%20be%20sure%20to%20bring%20an%20umbrella%20%E2%98%94%E2%98%94%E2%9C%85",
    "aoikey":api_key_for_callmebot,
}
response=requests.get(OWM_ENDPONIT,params=weather_params)
response.raise_for_status()
weather_data=response.json()
id1=weather_data["list"][0]['weather'][0]["id"]
id_list=[weather_data["list"][number]['weather'][0]["id"] for number in range(0,4)]
for number in id_list:
    if number<700:
        whatsapp_response=requests.get("https://api.callmebot.com/whatsapp.php",params=whatsapp_params)
        response.raise_for_status()
        exit()