import requests
from datetime import datetime


# Based on the user query entry - API gives out the calories burnt and informative links to the activity

APP_ID = "<>"
API_KEY = "<>"
url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

user_query = input("Tell me which exercies you did today")

param_data = {
        "query": user_query,
        "gender": "male",
        "weight_kg": 100,
        "height_cm": 200,
        "age": 100
}
hed = {
        "x-app-id":APP_ID,
        "x-app-key":API_KEY,
        "Content - Type": "application / json"
    }
response = requests.post(url, json=param_data, headers=hed)
nutrinux_response = response.json()

# Based on the results from NutritionX API, data is added to google sheets via sheety

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for ele in nutrinux_response["exercises"]:
     print(ele)
     body = {
            "sheet1": {
                "date": today_date,
                "time": now_time,
                "exercise": ele["user_input"],
                "duration": ele["duration_min"],
                "calories": ele["nf_calories"]
            }
      }
      url = "https://api.sheety.co/<>"
      hed1 = {"Authorization": "Bearer <>"}
      sheety_response = requests.post(url, json=body, headers=hed1)
      print(sheety_response.json())
