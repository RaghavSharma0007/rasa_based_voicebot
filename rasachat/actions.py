# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import difflib
import random

from typing import Any, Text, Dict, List

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import UserUtteranceReverted 

import sqlite3
import logging
import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


logger = logging.getLogger(__name__)


class ActionFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent_name = tracker.latest_message['intent'].get('name')
        entity_name = tracker.latest_message['entities']
        print("value of intent " + str(intent_name))
        print("value of entity "+ str(entity_name))
        if intent_name == "get_started" :
            dispatcher.utter_template("utter_payload", tracker)
            return [UserUtteranceReverted()]
        else:
            message = "कृपया आप सही जानकारी प्रदान करें"
            dispatcher.utter_message(message)
            return [UserUtteranceReverted()]


class Tractor_model(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_tractor"

    def run(self, dispatcher, tracker, domain):
        land_unit = tracker.get_slot('land_unit')
        size = int(tracker.get_slot('size'))
        crop = str(tracker.get_slot('crop'))
        print(crop)
        if (size <= 5):
            if (crop == "चावल"):
                #utter_message = "मैंने आपके द्वारा बताए गए मापदंडों के अनुसार ट्रैक्टर की सिफारिश प्रस्तुत कर दी है ।  ट्रैक्टर मॉडल  स्वराज 744 एफ ई"
                
                
                #dispatcher.utter_message(message)
                #image = "http://www.machinephd.com/wp-content/uploads/2017/08/Swaraj-744-FE.jpg"
                dispatcher.utter_template("utter_tractor_1", tracker)
                #dispatcher.utter_template(utter_message,tracker,image="http://www.machinephd.com/wp-content/uploads/2017/08/Swaraj-744-FE.jpg")
                #dispatcher.utter_message("http://www.machinephd.com/wp-content/uploads/2017/08/Swaraj-744-FE.jpg")
                return []

            elif(crop == "कपास"):
                #message = "मैंने आपके द्वारा बताए गए मापदंडों के अनुसार ट्रैक्टर की सिफारिश प्रस्तुत कर दी है । ट्रैक्टर मॉडल  स्वराज 963 एफ ई "
                #image= "https://cdn.tractorjunction.com/upload/swaraj-963-fe-494385.JPG"
                dispatcher.utter_template("utter_tractor_2", tracker)
                #dispatcher.utter_message("https://cdn.tractorjunction.com/upload/swaraj-963-fe-494385.JPG")
                return []

        elif (size > 5 and size <= 10):
            if (crop == "चावल"):
                #message = "मैंने आपके द्वारा बताए गए मापदंडों के अनुसार ट्रैक्टर की सिफारिश प्रस्तुत कर दी है । ट्रैक्टर मॉडल  स्वराज 963 एक्स एम "
                #dispatcher.utter_message(message)
                #image="http://www.swarajtractors.com/uploads/9/Swaraj-841xm.jpg"
                dispatcher.utter_template("utter_tractor_3", tracker)
                #dispatcher.utter_message("http://www.swarajtractors.com/uploads/9/Swaraj-841xm.jpg")
                return []

            elif(crop == "कपास"):
                #message = "मैंने आपके द्वारा बताए गए मापदंडों के अनुसार ट्रैक्टर की सिफारिश प्रस्तुत कर दी है । ट्रैक्टर मॉडल  स्वराज 855 एफ ई "
                #image= "https://5.imimg.com/data5/LC/NQ/MY-31780945/855-fe-swaraj-tractor-500x500.jpg"
                #dispatcher.utter_message(message)
                #dispatcher.utter_image_message("https://5.imimg.com/data5/LC/NQ/MY-31780945/855-fe-swaraj-tractor-500x500.jpg")
                dispatcher.utter_template("utter_tractor_4", tracker)
                #dispatcher.utter_attachment(image)
                return []
        else:
            message ="आप द्वारा बताया गया भूमि का आकार दिए गए विकल्पों के अनुरूप नहीं है कृपया सही विकल्प चुने"
            dispatcher.utter_message(message)
            return [UserUtteranceReverted()]











