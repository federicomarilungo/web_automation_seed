import json

class DataReader():
    def read_file(file_name):
        # Read the file
        with open("./data/" + file_name) as data_file:
            data = json.load(data_file)

        return data