from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import requests, json

class ActionReturnWeather(Action):
    def name(self):
        return 'action_search_weather'

    def run(self, dispatcher, tracker, domain):
        print("Hi its inside")
        print(tracker.get_slot("location"))
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "a5dd0a9a776f4b9c9bbf1dcb7d377b8b"
        unit = 'metric'
        complete_url = base_url + "appid=" + api_key + "&units=" + unit + "&q=" + tracker.get_slot("location")
        response = requests.get(complete_url)
        x = response.json()
        print(x)

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            dispatcher.utter_message("Hi your city tempurature is " + str(current_temperature) + " degree celsius")
        else:
            dispatcher.utter_message("location invalid" )
        return []


