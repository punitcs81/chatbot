# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
import logging
import requests
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_nlu.model import Trainer, Metadata, Interpreter
import json
from rasa_core_sdk import Action
from db_base import session

logger = logging.getLogger(__name__)

API_URL = "https://cricapi.com/api/"
API_KEY = "iD4gCvR911UmhfheUBLKF5lieGk2"


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_check_restaurants"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for restaurants")

        input = tracker.latest_message["text"]

        interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
        data = interpreter.parse(input)
        print(data)

        params = {}
        for ent in data["entities"]:
            params[ent["entity"]] = ent["value"]
        print(params)

        query = "select Restaurant_Name FROM restaurant"
        if len(params) != 0:
            filters = ["{}='{}'".format("lower(" + k + ")", v) for k, v in params.items()]
            print(filters)
            conditions = " and ".join(filters)
            print(conditions)
            query = " WHERE ".join([query, conditions])
        print(query)
        a = session.execute(query)
        result_set = a.fetchall()
        print(result_set)
        res = []
        for data in result_set:
            res = data[0]
        print(res)
        responses = [
            "I'm sorry :( I couldn't find anything like that"
            ,
            "what about {}?"
            ,
            "{} is one option, but I know others too :)"
        ]
        print(len(result_set))
        index = min(len(result_set), len(responses) - 1)
        print(responses[index].format(res))
        dispatcher.utter_message(responses[index].format(res))


        return []

