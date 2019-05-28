from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data
from db_base import session
from rasa_nlu.config import RasaNLUModelConfig
# from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config


def train(data, config_file, model_dir):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='chat')


def run():
    interpreter = Interpreter.load('./models/nlu/default/chat')
    data = interpreter.parse('wants to eat indian in bangalore')
    print(data)

    params = {}
    for ent in data["entities"]:
        params[ent["entity"]] = ent["value"]
    print(params)

    query = "select Restaurant_Name FROM restaurant"
    if len(params) != 0:
        filters = ["{}='{}'".format(k, v) for k, v in params.items()]
        print(filters)
        conditions = " and ".join(filters)
        print(conditions)
        query = " WHERE ".join([query, conditions])
    print(query)
    a = session.execute(query)
    result_set = a.fetchall()
    print(result_set)
    res =[]
    for data in result_set:
        res = data['name']
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

if __name__ == '__main__':
    train('./data/nlu_data.md', './config/config.yml', './models/nlu')
    run()

# rasa-nlu-trainer -v <path to the training data file>
# python nlu_modle.py
