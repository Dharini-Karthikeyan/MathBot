

import logging
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

class ActionPerformOperation(Action):
    def name(self) -> Text:
        return "action_perform_operation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        operation = tracker.get_slot("operation")
        operand_1 = tracker.get_slot("operand_1")
        operand_2 = tracker.get_slot("operand_2")
        result = None
        if operation == "add":
            result = operand_1 + operand_2
        elif operation == "subtract":
            result = operand_1 - operand_2
        elif operation == "multiply":
            result = operand_1 * operand_2
        elif operation == "divide":
            if operand_2 == 0:
                dispatcher.utter_message(response="utter_divide_by_zero")
                return []
            result = operand_1 / operand_2
        dispatcher.utter_message(response="utter_result", operation=operation, operand_1=operand_1, operand_2=operand_2, result=result)
        return []

class ActionAskForMoreOperations(Action):
    def name(self) -> Text:
        return "action_ask_for_more_operations"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_more_operations")
        return []


class MyCustomAction(Action):
    def run(self, dispatcher, tracker, domain):
        # do some custom logic to set the slots
        return [SlotSet("operation", "add"), SlotSet("operand_1", 3), SlotSet("operand_2", 4)]
