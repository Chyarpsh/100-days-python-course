import requests
from datetime import datetime
import os

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "female"
WEIGHT_KG = 73
HEIGHT_CM = 165
AGE = 24

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
APP_ID = "ae148fa8"
API_KEY = "16d5ab48b7ecf5ab860b4ba88a4ec5f4"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = "https://api.sheety.co/83303377009cd7092e0b6167e5a64548/copyOfMyWorkouts/workouts"

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 1: No Auth

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "arpi",
            "Arpshchy-1099!",
        )
    )

    # Sheety Authentication Option 3: Bearer Token
    bearer_headers = {
        "Authorization": f"Bearer {'YXJwaTpBcnBzaGNoeS0xMDk5IQ'}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    

    print(f"Sheety Response: \n {sheet_response.text}")
