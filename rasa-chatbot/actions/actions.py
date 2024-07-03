# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionLocationSearch(Action):

#     def name(self) -> Text:
#         return "utter_ask_location"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         location = tracker.get_slot("location")
#         dispatcher.utter_message(text="Votre plainte concernant {location} a été reçue. Merci de nous en avoir informés.")

#         return []
