from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
# from bot import RestaurantAPI
from bot import RestaurantAPI


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for restaurants")

        params = {'cuisine': tracker.get_slot("cuisine"),
                  'people': tracker.get_slot("people"),
                  'location': tracker.get_slot("location"),
                  'price': tracker.get_slot("price")}
        restaurant_api = RestaurantAPI()
        restaurants = restaurant_api.search(params)
        return [SlotSet("matches", restaurants)]


class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return []
