from db_base import session
import argparse
import asyncio
import logging

from rasa_core import utils
from policy import RestaurantPolicy
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.mapping_policy import MappingPolicy

logger = logging.getLogger(__name__)


class RestaurantAPI(object):
    def search(self, params):
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

        return res


async def train_dialogue(domain_file="domain.yml",
                         model_path="models/dialogue",
                         training_data_file="data/stories.md"):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=3),
                            MappingPolicy(),
                            RestaurantPolicy(batch_size=100, epochs=400,
                                             validation_split=0.2)])

    training_data = agent.load_data(training_data_file)
    agent.train(
        training_data
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/nlu.md')
    trainer = Trainer(config.load("config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
        description='starts the bot')

    parser.add_argument(
        'task',
        choices=["train-nlu", "train-dialogue", "run"],
        help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    loop = asyncio.get_event_loop()

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        loop.run_until_complete(train_dialogue())
