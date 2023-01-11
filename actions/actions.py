# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import json
 
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

with open("data/restaurants.json", "r") as f:
    restaurants = json.load(f)


class ActionSpecificKitchen(Action):

    def name(self) -> Text:
        return "action_specific_kitchen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        spoted_kitchen = next(tracker.get_latest_entity_values("restaurant_art"), None)
        msg = ""
        if spoted_kitchen:
            if spoted_kitchen in restaurants:
                if len(restaurants.get(spoted_kitchen)) > 3:                  
                    liste = list(restaurants.get(spoted_kitchen).keys())[0:3]
                    msg += f"Das sind die 3-besten {spoted_kitchen}en Restaurants in Deggendorf: {', '.join(liste)}"
                    dispatcher.utter_message(text=msg)
                    return[]
                    
                else:
                    msg += f"Das sind die {spoted_kitchen}en Restaurants in Deggendorf: {', '.join(restaurants.get(spoted_kitchen))}"                
                    dispatcher.utter_message(text=msg)
                    return[]
            else:

                msg = f"Es gibt keine {spoted_kitchen}en in Deggendorf. Probiere mal mexikanisch"
                dispatcher.utter_message(text=msg)
                return []

        msg = f"Gebe eine art von küche ein. Probiere mal mexikanisch"
        dispatcher.utter_message(text=msg)
        return[]

class ActionSpecificRestaurant(Action):

    def name(self) -> Text:
        return "action_specific_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        spoted_restaurant = next(tracker.get_latest_entity_values("restaurants"), None)
        msg = ""
        
        for arten in restaurants.keys():
            if spoted_restaurant in restaurants.get(arten).keys():
                time = restaurants.get(arten).get(spoted_restaurant).get("zeiten")
                street = restaurants.get(arten).get(spoted_restaurant).get("adresse")
                rate = restaurants.get(arten).get(spoted_restaurant).get("bewertung")
                msg = f"Die Adresse vom {spoted_restaurant} Restaurant ist: {street}. Es hat {time} auf und ist mit {rate} bewertet."
                dispatcher.utter_message(text=msg)
                return []
    
        msg = f"Das eingegebene Restaurant ist nicht in Deggendorf oder du hast vertippt. Gebe den Namen des Resaturants nochmals ein"
        dispatcher.utter_message(text=msg)
        return []

class ActionBestDishes(Action):

    def name(self) -> Text:
        return "action_best_dishes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        spoted_restaurant = next(tracker.get_latest_entity_values("restaurants"), None)
        msg = ""
        
        for arten in restaurants.keys():
            if spoted_restaurant in restaurants.get(arten).keys():
                best_dishes = restaurants.get(arten).get(spoted_restaurant).get("best_seller")
                msg = f"Das sind die Bestseller in {spoted_restaurant}: {', '.join(best_dishes)}."
                dispatcher.utter_message(text=msg)
                return []

        msg = f"Das eingegebene Restaurant ist nicht in Deggendorf oder du hast vertippt. Gebe den Namen des Resaturants nochmals ein"
        dispatcher.utter_message(text=msg)
        return []

class ActionWebsite(Action):

    def name(self) -> Text:
        return "action_website"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        spoted_restaurant = next(tracker.get_latest_entity_values("restaurants"), None)
        msg = ""
        
        for arten in restaurants.keys():
            if spoted_restaurant in restaurants.get(arten).keys():
                website = restaurants.get(arten).get(spoted_restaurant).get("website")
                msg = f"Das ist die Webseite von {spoted_restaurant} zum Online-Bestellen und für die Speisekarte: {website}."
                dispatcher.utter_message(text=msg)
                return []
    
        msg = f"Das eingegebene Restaurant ist nicht in Deggendorf oder du hast vertippt. Gebe den Namen des Resaturants nochmals ein"
        dispatcher.utter_message(text=msg)
        return []
