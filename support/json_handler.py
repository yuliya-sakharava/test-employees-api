import json


class JSONHandler:

    @staticmethod
    def load_json(path):
        with open(path, "r") as json_file:
            data = json.load(json_file)
        return data

    @staticmethod
    def dump_json(path, dataset):
        with open(path, "w") as json_file:
            json.dump(dataset, json_file)
